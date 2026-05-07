#Handle City
import pandas as pd
from sqlalchemy import create_engine

# Extract Process
def extract():

    engine = create_engine(

        "mysql+pymysql://root:root@localhost:3306/practice"
    )

    query = "Select * From Employees_raw"

    df = pd.read_sql(query,engine)

    return df

#Transform Process
def Transform(df):

    df["Emp_City"] = df["Emp_City"].fillna("Unknown")

    df["Emp_City"] = df["Emp_City"].replace("","Unknown")

    return df

#Display the Outcome

result = extract()

clean_data = Transform(result)

print(clean_data)

