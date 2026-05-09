import pandas as pd
import numpy as np

data = {

    "Emp_Name":["Rahul","Priya","Amit","Sneha","Ravi","Suresh"],
    "Emp_City":["pune","mumbai","pune","delhi","bangalore","mumbai"],
    "Salary":[50000,60000,30000,45000,70000,80000],
    "Dept": ["IT","HR","IT","Finance","IT","HR"]
}

df = pd.DataFrame(data)

#Add Column "Annual_Salary" = Salary * 12


df["Annual_Salary"] = df["Salary"]*12

print(df)

#Add Column "Tax" = 10% of Salary

df["Tax"] = df["Salary"]*0.10

print(df)

#Add Column "Net_Salary"=Salary -Tax

df["Net_Salary"] = df["Salary"] - df["Tax"]

print(df)

#Add Column "Country" = "India for all rows"

df["Country"] = "India"

print(df)

#Fix Emp_City Column Make all cities Capitalized "pune" = "Pune"

df["Emp_City"] = df["Emp_City"].str.capitalize()

print(df)

#Add Column "Salary_Grade" Salary > 60000 = "High"
#Salary > 40000 = "Medium"
#else "low"

df["Salary_Grade"] = np.where(df["Salary"] > 60000, "High",np.where(df["Salary"] > 40000,"Medium","Low"))

print(df)

#rename the Columns  Emp_Name:Name And Emp_City:City

df.rename(columns = {"Emp_Name":"Name","Emp_City":"City"},inplace = True)

print(df)

#Drop Column Tax

df.drop(columns = ["Tax"],inplace = True)

print(df)
