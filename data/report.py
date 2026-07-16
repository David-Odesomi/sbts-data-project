import pandas as pd

df = pd.read_csv("../output/cleaned.csv")
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

total_revenue = df["Amount"].sum()
top_service = df["Service"].value_counts().idxmax()
top_rep = df["Sales Rep"].value_counts().idxmax()
by_status = df.groupby("Status")["Amount"].sum()
by_service = df["Service"].value_counts()

min_amount = df["Amount"].min()
max_amount = df["Amount"].max()
average_amount = df["Amount"].mean()
pending =(df["Status"] == "Pending").sum()
Cancelled=(df["Status"] == "Cancelled").sum()
Paid = (df["Status"] == "Paid").sum()


def main():
    with open("summary1.txt", "w") as f:
        f.write("--------------------\n")
        f.write("SUMMARY REPORT\n")
        f.write("------------------\n")
        f.write(f"Total number of orders made: {len(df)}\n")
        f.write("----------------------------------------\n")
        f.write(f"Total revenue: NGN{total_revenue:,.0f}\n")
        f.write("----------------------------------------\n")
        f.write(f"The top service bought: {top_service}\n")
        f.write("----------------------------------------\n")
        f.write(f"The rep with the most customers: {top_rep}\n")
        f.write("----------------------------------------\n")
        f.write(f"The minimum amount:NGN{min_amount:,.0f}\n")
        f.write("----------------------------------------\n")
        f.write(f"The maximum amount:NGN{max_amount:,.0f}\n")
        f.write("----------------------------------------\n")
        f.write(f"The average amount: NGN{average_amount:,.0f}\n")
        f.write("----------------------------------------\n")
        f.write(f"No of pending orders: {pending}\n")
        f.write("----------------------------------------\n")
        f.write(f"No of cancelled orders: {Cancelled}\n")
        f.write("----------------------------------------\n")
        f.write(f"No of paid orders: {Paid}\n")
        f.write("----------------------------------------\n")
        f.write(f"\n")
        f.write("Total revenue per status\n")
        f.write("----------------------------------------\n")
        f.write(f"{by_status}\n")
        f.write("----------------------------------------\n")
        f.write(f"\n")
        f.write("No of Orders per Service\n")
        f.write("----------------------------------------\n")
        f.write(f"{by_service}\n")

if __name__ == "__main__":
    main()