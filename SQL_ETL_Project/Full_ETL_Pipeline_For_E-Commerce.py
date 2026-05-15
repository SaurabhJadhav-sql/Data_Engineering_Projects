#Import Pandas ,Numpy and sqlalchemy

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

#Transforming the data by using pandas (pd) and numpy (np)

def Cleaning(Customers,Orders,Order_Items,Products):

    Customers["Email"] = Customers["Email"].fillna("not_provided@gmail.com")  #Using pandas fillna function to set perticular value to null Emails

    Customers["City"] = Customers["City"].str.title()   #Capitalizing the City names by using pandas function title()

    Products["Stock"] = Products["Stock"].fillna(0)   #Giving 0 value to the empty stock.

    df = pd.merge(Customers,Orders,
                  on = "Customer_ID",
                  how = "inner")
    
    df = pd.merge(df,Order_Items,
                  on = "Order_ID",
                  how = "inner")
    
    df = pd.merge(df,Products,
                  on = "Product_ID",
                  how = "inner")
    
    df["Total_Values"] = df["Price"] * df["Quantity"]  #Caluclating the total_values by product price and the quantity 

    df["Tax"] = df["Total_Values"]*0.18  #Calculated the Tax by using column Total_value and multipling the value by 0.18 to add tax on each product of 18%

    df["Final_Value"] = df["Total_Values"] + df["Tax"]  #Calculating the final value by total value + tax 

    df = df[df["Status"] == "delivered"] #Displaying only those data that are delivered

    df["Order_Size"] = np.where(df["Total_Values"] > 100000,"High", np.where(df["Total_Values"] > 50000,"Medium","Low")) #Use Numpy np conditional statement to categorize the order size into high medium or low based on total values

    
    
    return df

#load the data into sql

def Load(df):

    conn = create_engine(

        "mysql+pymysql://root:root@localhost:3306/Ecommerce_etl"
    )

    try:

        df.to_sql("Clean_Data",conn,
              if_exists = "replace",
              index = False)
    
        print("Data Sucessfully loaded")
    except Exception as e:

        print(f"Data Loading error {e}")

Customers,Orders,Order_Items,Products = Extract()

Clean = Cleaning(Customers,Orders,Order_Items,Products)

loaded = Load(Clean)

print(loaded)
