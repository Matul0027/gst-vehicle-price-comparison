🚘 GST 2.0 Vehicle Price Dashboard

A Streamlit-powered dashboard to analyze the impact of GST 2.0 reforms on vehicle prices in India. The tool helps users compare Pre-GST vs Post-GST on-road costs, visualize savings, and understand the new taxation including BH Series registration rules.

 ✨ Features:
 🔍 Select brand, model, fuel type, and state for customized analysis.
 📊 Compare Ex-Showroom vs On-Road prices (Pre-GST vs Post-GST).
 📉 Calculate how much cheaper vehicles become after GST 2.0 (in %).
 🧾 Includes BH Series road tax calculation.
 📈 Interactive bar charts and pie charts to visualize savings.
 💾 Export results to CSV/Excel for reporting.

 🛠️ Tech Stack

 Python 3.11+
 Streamlit – Interactive UI
 Pandas – Data processing
 OpenPyXL – Excel integration
 Matplotlib/Altair – Charts

 Project Structure
📁 Project_GST
 ┣ 📄 app.py                      Streamlit app
 ┣ 📊 vehicles_prices_updated.xlsx    Vehicle dataset
 ┣ 📊 gst_slabs.xlsx              GST 2.0 slabs
 ┣ 📊 states.xlsx                 State taxes/fees
 ┣ 📄 README.md                   Documentation
```
 🚀 Getting Started
 1. Clone this repository
```bash
git clone(https://github.com/Matul0027/gst-vehicle-price-comparison)
cd gst-vehicle-dashboard
```
 2. Install dependencies
```bash
pip install -r requirements.txt
```
 3. Run the app
```bash
streamlit run app.py
 4. Open in Browser

Go to 👉 [http://localhost:8501](http://localhost:8501)

 📊 Example Use Case
 A user selects Hyundai Creta Petrol in Maharashtra.
 Dashboard shows:
   Ex-showroom: ₹1,500,000
   On-road Pre-GST: ₹1,950,000
   On-road Post-GST 2.0: ₹1,750,000
   Savings: \~10.3%
(This is for demonstration, actual prices depend on dataset.)

 ⚠️ Disclaimer
The cost figures are only for comparison & analysis.
They do not represent official prices.



 🧑‍💻 Author
Atul Maurya
Data Analytics Enthusiast | Python & Streamlit Developer

 ⭐ Contribute
If you find this useful, give the repo a ⭐ and feel free to fork & improve!




