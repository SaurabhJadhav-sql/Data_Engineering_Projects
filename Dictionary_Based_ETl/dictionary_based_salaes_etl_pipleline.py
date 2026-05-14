import pandas as pd
from sqlalchemy import create_engine

def Etl():

    data = {

    "Order_id":[101,102,103,104,105,106,107,108],
    "Customer_Name":["Rahul","Priya",None,"Amit","Sneha","Ravi",None,"Suresh"],
    "City":["pune","mumbai",None,"delhi","bangalore","mumbai",None,"delhi"],
    "Product":["Laptop","Phone","Tablet","Laptop","Phone","Earphones","Tablet","Laptop"],
    "Category":["Electronics","Electronics","Electronics","Electronics","Electronics","Accessories","Electronics","Electronics"],
    "Price":[60000,30000,None,60000,30000,2000,45000,None],
    "Quantity":[1,2,1,None,2,3,1,2],
    "Status":["delivered","pending","delivered","cancelled","delivered","pending","delivered","cancelled"]

}
    

    df = pd.DataFrame(data)

    return df

def Clean(df):

    df = df.dropna(subset = ["Customer_Name","City","Price","Quantity"])

    df["Total_Value"] = df["Price"]*df["Quantity"]

    df["Tax"] = df["Price"]*0.18

    df["Final_Amount"] = df["Price"] + df["Tax"]

    df[(df["Status"] == "delivered")]

    return df

def load(df):

    enginee = create_engine(

        "mysql+pymysql://root:root@localhost:3306/practice"
    )

    try:

       df.to_sql("Clean_Orders",enginee,
              if_exists = "replace",
              index = False)
    
        print("Data Successfully Loaded")
except Exception as e:
        print(f"Error loading the data {e}")

data = Etl()

clean_data = Clean(data)

print(load(clean_data))


