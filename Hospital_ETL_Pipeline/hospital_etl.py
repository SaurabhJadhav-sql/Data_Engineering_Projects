#=====================================
#import pandas and sqlalchemy
#=====================================

import pandas as pd
from sqlalchemy import create_engine      

#======================================
#Extract Data 
#======================================

def extract():

    try:

        patients = pd.read_csv("patients.csv")             # Read patients data

        doctors = pd.read_csv("doctors.csv")               # Read doctors data

        appointements = pd.read_csv("appointments.csv")    # Read appointements data

        billings = pd.read_csv("billing.csv")              # Read billings data

        return patients,doctors,appointements,billings     
    
    except FileNotFoundError as e:

        print(f"Files  not Found!! {e}")

        return None,None,None,None
    
    finally:

        print("Extraction Process Completed")

#=======================================
# Transform Data
#=======================================

def transform(patients,doctors,appointements,billings):

    try:

        patients["Insurance_Status"] = patients["Insurance_Status"].fillna("Unknown")     # Fill Missing Insurance Status

        doctors["Consultation_Fee"] = doctors["Consultation_Fee"].fillna(doctors["Consultation_Fee"].mean())    # Replacing missing consultation fee with average fee

        appointements["Payment_Mode"] = appointements["Payment_Mode"].fillna("Not Provided")   # Fill Missing Payment Mode

        billings["Medicine_Cost"] = billings["Medicine_Cost"].fillna(0)   # Fill Missing Medicine Cost

        patients["Patient_Name"] = patients["Patient_Name"].str.title()   # Standardize Patient Name Using Title Case

        doctors["Doctor_Name"] = doctors["Doctor_Name"].str.title()   # Standardize Doctor Name Using title Case

        patients["City"] = patients["City"].str.title()   # Standardize City Names using Title Case

        billings["Total_Bill"] = billings["Treatment_Cost"] + billings["Medicine_Cost"] + billings["Room_Charges"]    # Getting total bill by adding treatment bill , medicine bill and room charges 

        billings["Discount_Amount"] = billings["Total_Bill"] * billings["Discount_Percent"] / 100         # Getting Discount amount by multipling total bills and discount percentag and divivding it with 100

        billings["Final_Bill"] = billings["Total_Bill"] - billings["Discount_Amount"]      # Getting Finall bill by subtracting total bill with discount amount

        patients["Age_Group"] = patients["Age"].apply(lambda x: "Young" if x < 30 else "Adult" if x <= 50 else "Senior")      # Categorize patients based on there age

        doctors["Doctor_Level"] = doctors["Experience_Years"].apply(lambda x: "Senior Doctor" if x > 10 else "Mid-Level" if x >= 5 else "Junior Doctor")  # Categorize doctors based on there experience

        appointements = appointements[appointements["Status"] == "Completed"]   # Filter Only Completed Appointements

        df = pd.merge(patients,appointements,       # Merge Patients Data with Appointements Data
                      on = "Patient_ID",
                      how = "inner")
        
        df = pd.merge(df,doctors,                   # Merge Doctors Details Into Master Dataframe
                      on = "Doctor_ID",
                      how = "inner")
        
        df = pd.merge(df,billings,                  # Merge Billings Details Into Final Master Dataframe
                      on = "Appointment_ID",
                      how = "inner")
        
        df["Patient_Category"] = df["Final_Bill"].apply(lambda x: "VIP" if x > 15000 else "Regula")     #Categorize patients based on final bill

        df["Insurance Type"] = df["Insurance_Status"].apply(lambda x: "Insured" if x == "Active" else "Inactive" if x == "Inactive" else "No Insurance")   # Create insurance category from insurance status

        Total_Revenue = df["Final_Bill"].sum()   #Calculate total hospital revenue
        print(Total_Revenue)

        Revenue_By_Department = df.groupby("Department")["Final_Bill"].sum()    # Aggregate revenue department-wise
        print(Revenue_By_Department)

        return df

    except KeyError as e:

        print(f"Column could not find {e}")
        
        return None

    finally:

        print("Transformation Process Completed")

#==================================
#Load Data
#==================================

def Load(df):

    try:

        conn = create_engine(
            "mysql+pymysql://root:root@localhost:3306/practice"      # Created MySQL Database connection
        )

        df.to_sql("hospital_Data",conn,                              # Load transform data into MySQL table
                  if_exists = "replace",                             # Replace existing table if already present
                  index = False)
        
        print("Data is Loaded Successfully")                         # Print successful load message 

    except Exception as e:

        print(f"Data Failed to load {e}")                            # Expected Error if Try Block Won't run

    finally:                                                         # Will run regardless try or except runs

        print("ETL Pipeline Completed Successfully")

patients,doctors,appointements,billings = extract()

clean_data = transform(patients,doctors,appointements,billings)

load = Load(clean_data)













       
