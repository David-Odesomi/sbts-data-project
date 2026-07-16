import pandas as pd

df = pd.read_csv("../output/cleaned.csv")
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

total_revenue = df["Amount"].sum()
top_service = df["Service"].value_counts().idxmax()
top_rep = df["Sales Rep"].value_counts().idxmax()
by_status = df.groupby("Status")["Amount"].sum()

def main():
    with open("summary.txt", "w") as f:
        f.write(f"TOTAL ORDERS MADE: {len(df)}\n")
        f.write(f"TOTAL REVENUE: NGN{total_revenue}\n")
        f.write(f"THE TOP SERVICE BOUGHT: {top_service}\n")
        f.write(f"THE REP WITH THE MOST CUSTOMERS: {top_rep}\n")
        f.write(f"\n")
        f.write(f"{by_status}\n")

if __name__ == "__main__":
    main()