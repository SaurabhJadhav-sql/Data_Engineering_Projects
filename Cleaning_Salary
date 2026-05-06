#Extract Data
import pandas as pd
from sqlalchemy import create_engine

def extract():

    engine = create_engine(

        "mysql+pymysql://root:root@localhost:3306/practice"
    )

    query = "Select * From Employees_raw"

    df = pd.read_sql(query,engine)

    return df

#Now transform the data

def Transform(df):

    data = df.to_dict(orient="records")

    clean = []

    for i in data:

        salary = i["Salary"]

        if str(salary).isdigit():

            salary = int(salary)
            clean.append(salary)

    return clean

#Display Data
data = extract()

clean_data = Transform(data)

print(clean_data)
