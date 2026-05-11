import pandas as pd
import numpy as np
from sqlalchemy import create_engine
#Extract Data From MySQl
def Extract():

    connection = create_engine(

        "mysql+pymysql://root:root@localhost:3306/Ecommerce_etl"
    )

    Customers = pd.read_sql("Select * From Customers",connection)

    Orders = pd.read_sql("Select * From Orders",connection)

    Order_Items = pd.read_sql("Select * From Order_Items",connection)

    Products = pd.read_sql("Select * From Products",connection)

    return Customers,Orders,Order_Items,Products

def Cleaning(Customers,Orders,Order_Items,Products):

    Customers["Email"] = Customers["Email"].fillna("not_provided@gmail.com")

    Customers["City"] = Customers["City"].str.title()

    Products["Stock"] = Products["Stock"].fillna(0)

    df = pd.merge(Customers,Orders,
                  on = "Customer_ID",
                  how = "inner")
    
    df = pd.merge(df,Order_Items,
                  on = "Order_ID",
                  how = "inner")
    
    df = pd.merge(df,Products,
                  on = "Product_ID",
                  how = "inner")
    
    df["Total_Values"] = df["Price"] * df["Quantity"]

    df["Tax"] = df["Total_Values"]*0.18

    df["Final_Value"] = df["Total_Values"] + df["Tax"]

    df = df[df["Status"] == "delivered"]

    df["Order_Size"] = np.where(df["Total_Values"] > 100000,"High", np.where(df["Total_Values"] > 50000,"Medium","Low"))

    
    
    return df
def Load(df):

    conn = create_engine(

        "mysql+pymysql://root:root@localhost:3306/Ecommerce_etl"
    )

    df.to_sql("Clean_Data",conn,
              if_exists = "replace",
              index = False)
    
    print("Data Sucessfully loaded")

Customers,Orders,Order_Items,Products = Extract()

Clean = Cleaning(Customers,Orders,Order_Items,Products)

loaded = Load(Clean)

print(loaded)
