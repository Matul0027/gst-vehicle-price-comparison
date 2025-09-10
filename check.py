import pandas as pd

# Load your gst_slabs.xlsx file
df = pd.read_excel("gst_slabs.xlsx")

# Print all column names
print("Columns in gst_slabs.xlsx:")
print(df.columns.tolist())
