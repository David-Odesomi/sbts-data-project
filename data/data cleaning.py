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
data['Status']=data['Status'].replace({"OVERDUE":"Overdue","PAID":"Paid","pending":"Pending","paid":"Paid","cancelled":"Cancelled"})
data['Client']=data['Client'].str.title()

# Remove "NGN" and commas from the amount column
data['Amount']=data['Amount'].replace('[NGN,]','',regex=True)
#convert amount from text to numeric(float data type)
data['Amount']=data['Amount'].astype(float)
# format the amount column back in nigerian currency
data['Amount']=data['Amount'].apply(lambda x:f"NGN{x:,.2f}")
#convert the date column to a proper date format

data["Date"]=pd.to_datetime(data["Date"], format = 'mixed',errors='coerce')
# format dates as YYYY-MM-DD
data["Date"]=data["Date"].dt.strftime('%Y-%m-%d')
# checking for duplicated cells and dropping them
print(data.drop_duplicates())
#print
print(data.to_string())

data.to_csv("cleaned.csv",index=False)

