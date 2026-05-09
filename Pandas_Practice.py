import pandas as pd

data = {

    "Customer_Name":["Rahul","Priya","Amit","Sneha","Ravi","Suresh","Neha","Karan"],
    "City": ["Pune","Mumbai","Pune","Delhi","Bangalore","Mumbai","Pune","Delhi"],
    "Account_Type": ["Saving","Current","Saving","Current","Saving","Current","Saving","Current"],
    "Balance":[50000,150000,None,45000,200000,None,75000,30000],
    "Age":[25,35,None,28,42,38,None,30]
}

df = pd.DataFrame(data)

#Question First:Fill Missing Values
Missing_Values = df["Balance"] = df["Balance"].fillna(df["Balance"].mean())

print(Missing_Values)

#Question 2:Fill Missing With Average

Average = df["Age"] = df["Age"].fillna(df["Age"].mean())

print(Average)

#Question 3: Show Only Savings Account Customers

Saving = df[df["Account_Type"] == "Saving"]

print(Saving)

#Question 4:Show Customers With Balance > 10000

Balance = df[df["Balance"] > 100000]

print(Balance)

#Question 5:Show Customers From Pune Or Mumbai

Customers = df[(df["City"] == "Pune") | (df["City"] == "Mumbai")]

print(Customers)

#Question 6: Show Savings Customers From Pune Only

Pune_Only = df[df["City"] == "Pune"]

print(Pune_Only)

#Question 7: Show Customers From Pune,Mumbai,Delhi Using isin()

sin = df[df["City"].isin(["Pune","Mumbai","Delhi"])]

print(sin)

#Question 8:Show Only Customer_Name And Balance Columns

Customer_Balance = df[["Customer_Name","Balance"]]

print(Customer_Balance)

#Question 9: Show Savings Customers From Pune With Balance > 50000 Display Only Name And Balance

Customer = df[(df["City"] == "Pune") & (df["Account_Type"] == "Saving") & (df["Balance"] > 50000)]

print(Customer)

#Question 10:Drop Rows Where Both Balance And Age Are missing then fill remaining missing balance with mean

Drop = df =df.dropna(subset = ["Balance","Age"],how = "all")

print(Drop)
