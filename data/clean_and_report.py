import pandas as pd
import numpy as np

data = pd.read_csv("dummy_client_orders.csv")

# fill missing sales rep by random sampling from existing reps
valid_reps = data["Sales Rep"].dropna()
mask = data["Sales Rep"].isna()
data.loc[mask, "Sales Rep"] = np.random.choice(valid_reps, size=mask.sum())

# fill missing status with "Unknown" rather than guessing —
# randomly assigning Paid/Overdue would quietly distort revenue numbers
data["Status"] = data["Status"].fillna("Unknown")

# standardize the Status and Client columns
data["Status"] = data["Status"].str.strip().str.title()
data["Status"] = data["Status"].replace({
    "Pendng": "Pending",
    "Canceled": "Cancelled",
})
data["Client"] = data["Client"].str.strip().str.title()

# standardize dates to YYYY-MM-DD
data["Date"] = pd.to_datetime(data["Date"], format="mixed", errors="coerce")
data["Date"] = data["Date"].dt.strftime("%Y-%m-%d")

# drop duplicate rows (and actually keep the result this time)
data = data.drop_duplicates()

# clean Amount: remove "NGN " and commas, then convert to float
data["Amount"] = data["Amount"].astype(str)
data["Amount"] = data["Amount"].str.replace("NGN ", "", regex=False)
data["Amount"] = data["Amount"].str.replace(",", "", regex=False)
data["Amount"] = pd.to_numeric(data["Amount"], errors="coerce")

# save the fully cleaned data — after all cleaning steps, not before
data.to_csv("cleaned.csv", index=False)

print(data.to_string())

# ---- summary numbers ----
total_revenue = data["Amount"].sum()
print(f"\nTotal revenue: NGN {total_revenue:,.0f}")

print("\nOrders per sales rep:")
print(data["Sales Rep"].value_counts())

print("\nOrders per service:")
print(data["Service"].value_counts())

print("\nOrders per Order ID (should mostly be 1 after deduping):")
print(data["Order ID"].value_counts().to_string())

print(f"\nMax transaction: NGN {data['Amount'].max():,.0f}")
print(f"Min transaction: NGN {data['Amount'].min():,.0f}")
print(f"Average transaction: NGN {data['Amount'].mean():,.0f}")