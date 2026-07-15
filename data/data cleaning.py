import pandas as pd
import numpy as np
from envs.pandas.Lib.idlelib import statusbar

data = pd.read_csv("dummy_client_orders.csv")
#fill missing client rep by random sampling
valid_reps = data["Sales Rep"].dropna()
mask = data["Sales Rep"].isna()
data.loc[mask, "Sales Rep"] = np.random.choice(valid_reps, size=mask.sum())

# filling the missing status cells by random sampling
valid_reps = data["Status"].dropna()
mask = data["Status"].isna()
data.loc[mask, "Status"] = np.random.choice(valid_reps, size=mask.sum())


# standardize the status and client rep column
data['Status']=data['Status'].str.title()
data['Status']=data['Status'].replace({"OVERDUE":"Overdue","PAID":"Paid","pending":"Pending","paid":"Paid","cancelled":"Cancelled", "Canceled":"Cancelled","Pendng":"Pending"})
data['Client']=data['Client'].str.title()





data["Date"]=pd.to_datetime(data["Date"], format = 'mixed',errors='coerce')
# format dates as YYYY-MM-DD
data["Date"]=data["Date"].dt.strftime('%Y-%m-%d')
# checking for duplicated cells and dropping them
print(data.drop_duplicates())
#print

# removed the NGN and comma's then
data["Amount"] = data["Amount"].str.replace("NGN ", "", regex=False)
data["Amount"] = data["Amount"].str.replace(",", "", regex=False)
# Convert the Amount column to float
data["Amount"] = data["Amount"].astype(float)

print(data.to_string())



data.to_csv("cleaned.csv",index=False)
# calculating the total revenue
total_revenue = data["Amount"].sum()
print(f"total_revenue:NGN {total_revenue}")
# Number of  people assigned to a sales rep
print(data["Sales Rep"].value_counts())
# number of people that purchased a specific srvice
print(data["Service"].value_counts())
# number of purchases per order
print(data["Order ID"].value_counts().to_string())
# maximum number of transcations
print(data["Amount"].max())
# minimum number of transcations
print(data["Amount"].min())
# average number of transactions
print(data["Amount"].mean())