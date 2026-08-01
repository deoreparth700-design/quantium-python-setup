import pandas as pd
import glob

# Read all CSV files from the data folder
files = glob.glob("data/*.csv")

# Combine all CSV files
df = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Remove the $ sign from price and convert to float
df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

# Calculate Sales
df["Sales"] = df["quantity"] * df["price"]

# Keep only required columns
output = df[["Sales", "date", "region"]]

# Rename columns
output.columns = ["Sales", "Date", "Region"]

# Save the output
output.to_csv("formatted_output.csv", index=False)

print("✅ formatted_output.csv created successfully!")