
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



















