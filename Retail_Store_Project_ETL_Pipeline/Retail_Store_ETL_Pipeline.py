#Import Pandas and Sqlalchemy
import pandas as pd
from sqlalchemy import create_engine


#Extract CSV Files
def extract():

    Customers = pd.read_csv("customers_1.csv")

    Orders = pd.read_csv("orders.csv")

    Order_items = pd.read_csv("order_items.csv")

    Products = pd.read_csv("products.csv")

    return Customers,Orders,Order_items,Products

#Transform/Filter Data 
def transform(Customers,Orders,Order_items,Products):

    Customers["Email"] = Customers["Email"].fillna("not_provided")

    Customers["City"] = Customers["City"].str.capitalize()

    Customers["Age_Group"] = Customers["Age"].apply(lambda x: "Young" if x < 30  else "Middle" if x < 40 else "Senior")

    Products["Selling_Price"] = Products["Selling_Price"].fillna(Products["Selling_Price"].mean())

    Products["Profit_Margin"] = Products["Selling_Price"] - Products["Cost_Price"]

    Products["Profit_Percent"] = Products["Profit_Margin"] / Products["Cost_Price"] * 100

    Orders["Delivery_Date"] = Orders["Delivery_Date"].fillna("Pending")

    Orders = Orders[Orders["Status"]  == "Delivered"]

    Order_items["Unit_Price"] = Order_items["Unit_Price"].fillna(Order_items["Unit_Price"].mean())

    Order_items["Total_Values"] = Order_items["Unit_Price"] * Order_items["Quantity"]

    Order_items["Tax"] = Order_items["Total_Values"] * 0.18

    Order_items["Final_Amount"] = Order_items["Total_Values"] + Order_items["Tax"]

    Order_totals = Order_items.groupby("Order_ID")["Total_Values"].sum().reset_index()

    Order_totals.columns = ["Order_ID","Order_totals"]

    Orders = pd.merge(Orders,Order_totals, on = "Order_ID", how = "left")

    Orders["Discount_Amount"] = Orders["Order_totals"] * Orders["Discount_Percent"] /100

    df = pd.merge(Customers,Orders,
                   on = "Customer_ID",
                   how = "inner")
    
    df = pd.merge(df,Order_items,
                  on = "Order_ID",
                  how = "inner")
    
    df = pd.merge(df,Products,
                  on = "Product_ID",
                  how = "inner")
    
    df["Order_Size"] = df["Final_Amount"].apply(lambda x: "High Value" if x > 100000 else "Medium Value" if x > 50000 else "Low Value")

    df["Customer_label"] = df.apply(lambda x: "VIP" if x["Customer_Type"] == "Premium" and x["Order_Size"] == "High Value" else "Regular",axis = 1)

    return df

#Now Load Data in MySQL
def load(df):

    conn = create_engine(

        "mysql+pymysql://root:root@localhost:3306/practice"
    )

    try:

    df.to_sql("Retail_Analytics",conn,
              if_exists = "replace",
              index = False)
    
    print("Data is Loaded Successfully.")

except Expection as e:

    print(f"Error loading data: {e}")

Cust_Clean,Ord_Clean,Ord_item_Clean,Prod_Clean = extract()

Clean = transform(Cust_Clean,Ord_Clean,Ord_item_Clean,Prod_Clean)

Loaded = load(Clean)

print(Clean)



