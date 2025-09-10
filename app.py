import streamlit as st
import pandas as pd
import numpy as np
import re

# ==============================
# Load Data
# ==============================
@st.cache_data
def load_data():
    vehicles = pd.read_excel("vehicles_prices_updated.xlsx")
    gst_slabs = pd.read_excel("gst_slabs.xlsx")
    states = pd.read_excel("states.xlsx")
    return vehicles, gst_slabs, states

vehicles, gst_slabs, states = load_data()

# ==============================
# Helper: Condition Parser
# ==============================
def check_condition(value, condition):
    """
    Parse conditions like <=1200, >1500, 4000, All (string from Excel)
    and check if value satisfies it.
    """
    if pd.isna(condition) or str(condition).lower() == "all":
        return True

    cond_str = str(condition).strip()

    # Handle <=, >=, <, > cases
    if cond_str.startswith("<="):
        return value <= float(cond_str[2:])
    elif cond_str.startswith(">="):
        return value >= float(cond_str[2:])
    elif cond_str.startswith("<"):
        return value < float(cond_str[1:])
    elif cond_str.startswith(">"):
        return value > float(cond_str[1:])
    else:
        # Exact match
        try:
            return float(value) == float(cond_str)
        except:
            return False


# ==============================
# GST Rate Finder
# ==============================
def get_gst_rate(row, gst_slabs):
    for _, slab in gst_slabs.iterrows():
        fuel_cond = (
            str(row["fuel_type"]).lower() == str(slab["fuel_type"]).lower()
        ) if pd.notna(slab["fuel_type"]) else True

        cc_cond = check_condition(row["engine_cc"], slab["engine_cc"])
        length_cond = check_condition(row["length_mm"], slab["length_mm"])

        if fuel_cond and cc_cond and length_cond:
            return slab["gst_pre"], slab["gst_post"]

    # default fallback
    return 28.0, 18.0


# ==============================
# On-road price calculation
# ==============================
def calculate_onroad_price(base_price, gst_rate, state_row):
    if pd.isna(base_price):
        return None
    price_gst = base_price * (1 + gst_rate / 100)
    road_tax = price_gst * (state_row["road_tax_pct"] / 100)
    insurance = price_gst * (state_row["insurance_pct"] / 100)
    reg_fee = state_row["reg_fee"]
    return round(price_gst + road_tax + insurance + reg_fee, -2)


# ==============================
# Streamlit UI (Single Car View)
# ==============================
st.set_page_config(page_title="GST 2.0 Vehicle Price Dashboard", layout="wide")
st.title("🚘 GST 2.0 Vehicle Price Impact")

# Sidebar filters
brand = st.sidebar.selectbox("Select Brand", sorted(vehicles["brand"].dropna().unique().tolist()))
model = st.sidebar.selectbox(
    "Select Model",
    sorted(vehicles[vehicles["brand"] == brand]["model"].dropna().unique().tolist())
)
state_name = st.sidebar.selectbox("Select State/UT", sorted(states["state"].dropna().unique().tolist()))

# Get selected car
selected_car = vehicles[(vehicles["brand"] == brand) & (vehicles["model"] == model)].iloc[0]
state_row = states[states["state"] == state_name].iloc[0]

# Get GST rates
gst_pre, gst_post = get_gst_rate(selected_car, gst_slabs)

# Calculate On-road prices
pre_price = calculate_onroad_price(selected_car["ex_showroom_base"], gst_pre, state_row)
post_price = calculate_onroad_price(selected_car["ex_showroom_base"], gst_post, state_row)

# ==============================
# Show Results
# ==============================
st.subheader(f"{brand} {model} in {state_name}")

saving = pre_price - post_price
saving_pct = (saving / pre_price) * 100 if pre_price else 0

st.metric("Pre-GST On-road Price", f"₹{pre_price:,.0f}")
st.metric("Post-GST On-road Price", f"₹{post_price:,.0f}")
st.metric("Saving After GST 2.0", f"₹{saving:,.0f} ({saving_pct:.2f}%)")

# Charts
chart_df = pd.DataFrame({
    "Price Type": ["Pre-GST", "Post-GST"],
    "Price": [pre_price, post_price]
})

st.bar_chart(chart_df.set_index("Price Type"))

pie_df = pd.DataFrame({
    "Category": ["Saving", "Final Price"],
    "Value": [saving, post_price]
})
st.subheader("Savings Distribution")
st.write("Cost showing is only for comparison, This is not a final price.")
st.dataframe(pie_df)

