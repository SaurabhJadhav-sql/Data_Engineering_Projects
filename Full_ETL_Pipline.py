import pandas as pd
from sqlalchemy import create_engine

def extract():
    
    data = create_engine(

        "mysql+pymysql://root:root@localhost:3306/practice"
    )

    query = "Select * From Employees_raw"

    df = pd.read_sql(query,data)

    return df

#Now Transform using pandas

def Transform(df):

    df["Emp_City"] = df["Emp_City"].fillna("Unknown")

    df["Salary"] = pd.to_numeric(df["Salary"], errors = "coerce")

    df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

    df = df[df["Salary"].notna()]


    return df

def load(df):

    engine = create_engine(

        "mysql+pymysql://root:root@localhost:3306/practice"
    )

    df.to_sql("Employees_clean",engine,
        if_exists = "replace",index = False)
    print("Data Loaded Successfully!")

data = extract()

clean_Data = Transform(data)

load1 = load(clean_Data)

print(load1)
