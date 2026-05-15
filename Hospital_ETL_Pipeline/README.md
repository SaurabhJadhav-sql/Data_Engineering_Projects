
#📋 Project Overview

This project display complete ETL process (Extract , Transform And Load) for hospital management system.Build it using python,pandas and MySQL.

In this project pipeline extracts the data from multiple CSV files and perform data cleaning,business transformation and merges the datasets creates analytics 
features and finally loads the data into MySQl Database.

---
#💻 Tools Required

| Tools | Purpose |
|-------|---------|
|🐍 Python | Core Programming Language |
|🐼 Pandas | Data manipulation and cleaning |
|🛢️ MySQL | Data Storage |
|⚙️ SQlAlchemy | Database Connection |
|📄 CSV Files | Data Format Used |
|💻 VS Code | Developement Environment |
---


# 💠ETL Flow

#📥 Extract Phase

This Pipeline extracts multiple CSV files

-1) Patients
-2) Doctors
-3) Appointments
-4) Billing

Using:
```bash
pd.read_csv()
```
---

# 🔧 Transform Phase

###👥 Patients Transformation

-✔️ Filled Missing Insurance Status with "Unknown".
-✔️ Standardize the Patients Names.
-✔️ Categorize patients based on there age.

###👩🏻‍⚕️ Doctors Transformation

-✔️ Filled Missing Consultation Fee with "Average fee".
-✔️ Standardize the Doctor Names.
-✔️ Categorize doctors based on Experience.

###📅 Appointments

-✔️ Filled Missing payments mode with "Not Provided"
-✔️ Filter the data according to status.

###💳 Billings

-✔️  Filled Missing medicine cost with `0`.
-✔️ Calculated:
-1) Total Bill. ✅
-2) Discount Amount. ✅
-3) Final Bill ✅
-4) Total Revenue ✅
-5) Revenue by Departments ✅

---

##🛡️ Error Handling

Use `try` `except` and `finally` for handaling errors and avoiding the pipeline crash.

---

# 🚀 How to run Project

##1) Instal Required
   ```bash
     pip install pandas  sqlalchemy pymysql
   ```
##2) MySQL Setup
    ``` sql
     CREATE DATABASE practice;
    ```
##3) Run Pipeline
   ```bash
     Hospital_ETL_Pipeline.py
   ```
##4) Verify in MySQL
    ``` sql
     SELECT * FROM hospital_Data;
    ```   
    
---













       
