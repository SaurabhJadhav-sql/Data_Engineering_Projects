#Extract
import pandas as pd
from sqlalchemy import create_engine

def Extract():

    enginee = create_engine(

        "mysql+pymysql://root:root@localhost:3306/Practice"
    )

    query = "Select * From Employees"

    df = pd.read_sql(query,enginee)

    return df

#Fetch Required Data

def Featch(df):

    df = df[df["Emp_Name"].str.startswith("S",na = False)]

    df=df[df["Emp_City"] == "Pune"]

    return df

#Loaded

def Load(df):

    enginee = create_engine(

        "mysql+pymysql://root:root@localhost:3306/Practice"
    )

    df.to_sql("Employees_With_S1",enginee,
              if_exists = "replace",
              index = False)
    
    print("Loaded_Successfully")

data = Extract()

clean = Featch(data)

print(Load(clean))

