
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("output/cleaned.csv")

# Remove rows with missing Amount values
df = df.dropna(subset=["Amount"])

# Calculate total revenue by service
revenue = df.groupby("Service")["Amount"].sum()

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(revenue.index, revenue.values)

plt.title("Revenue by Service")
plt.xlabel("Service")
plt.ylabel("Revenue (NGN)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()



orders = df["Sales Rep"].value_counts()

plt.figure(figsize=(8,5))
plt.bar(orders.index, orders.values)

plt.title("Orders per Sales Representative")
plt.xlabel("Sales Representative")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


status = df["Status"].str.strip().value_counts()

plt.figure(figsize=(7,7))

plt.pie(
    status.values,
    labels=status.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Order Status Distribution")

plt.show()



df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.strftime("%b")

monthly = df.groupby("Month")["Amount"].sum()

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

monthly = monthly.reindex(months)

plt.figure(figsize=(10,5))

plt.plot(monthly.index, monthly.values, marker="o")

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (NGN)")

plt.grid(True)

plt.show()









