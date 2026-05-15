# 📋 Hospital ETL Pipeline

## Project Overview

This project demonstrates a complete **ETL process** (Extract, Transform, and Load) for a hospital management system. The pipeline extracts data from multiple CSV files, performs comprehensive data cleaning and transformation, and loads the processed data into a MySQL database.

**Technologies Used:**
- 🐍 Python
- 🐼 Pandas
- 🛢️ MySQL
- ⚙️ SQLAlchemy
- 📄 CSV Files

---

## 💻 Prerequisites & Installation

### Required Tools

| Tool | Purpose |
|------|---------|
| Python 3.x | Core Programming Language |
| Pandas | Data manipulation and cleaning |
| SQLAlchemy | Database connection ORM |
| PyMySQL | MySQL database driver |
| MySQL Server | Data Storage |
| VS Code (Optional) | Development Environment |

### Installation Steps

```bash
# 1. Install required Python packages
pip install pandas sqlalchemy pymysql

# 2. Create MySQL database
mysql -u root -p
```

```sql
CREATE DATABASE practice;
```

---

## 🔄 ETL Pipeline Architecture

### 📥 **Extract Phase**

The pipeline extracts data from 4 CSV files:

1. **patients.csv** - Patient demographic information
2. **doctors.csv** - Doctor details and specialization
3. **appointments.csv** - Appointment records
4. **billing.csv** - Billing and transaction information

**Method Used:**
```python
pd.read_csv(filename)
```

### 🔧 **Transform Phase**

#### 👥 Patients Transformation
- ✅ Fill missing `Insurance_Status` with "Unknown"
- ✅ Standardize patient names to title case
- ✅ Categorize patients by age group:
  - **Young**: Age < 30
  - **Adult**: Age 30-50
  - **Senior**: Age > 50

#### 👩🏻‍⚕️ Doctors Transformation
- ✅ Fill missing `Consultation_Fee` with average fee
- ✅ Standardize doctor names to title case
- ✅ Categorize doctors by experience:
  - **Junior Doctor**: Experience < 5 years
  - **Mid-Level**: Experience 5-10 years
  - **Senior Doctor**: Experience > 10 years

#### 📅 Appointments Transformation
- ✅ Fill missing `Payment_Mode` with "Not Provided"
- ✅ Filter only "Completed" appointments

#### 💳 Billing Transformation
- ✅ Fill missing `Medicine_Cost` with 0
- ✅ Calculate analytics features:
  - **Total_Bill** = Treatment_Cost + Medicine_Cost + Room_Charges
  - **Discount_Amount** = (Total_Bill × Discount_Percent) / 100
  - **Final_Bill** = Total_Bill - Discount_Amount
  - **Patient_Category**: "VIP" if Final_Bill > 15,000, else "Regular"

#### 🔗 Data Merge Operations
- Merge Patients with Appointments (on `Patient_ID`)
- Merge result with Doctors (on `Doctor_ID`)
- Merge result with Billing (on `Appointment_ID`)
- Create `Insurance_Type` field based on `Insurance_Status`

#### 📊 Analytics Generated
- **Total_Revenue**: Sum of all `Final_Bill` amounts
- **Revenue_By_Department**: Grouped revenue by department

### 📤 **Load Phase**

- Load transformed data into MySQL table: `hospital_Data`
- Replace existing table if it already exists
- Connection string: `mysql+pymysql://root:root@localhost:3306/practice`

---

## 🛡️ Error Handling

The pipeline implements robust error handling:

- **FileNotFoundError**: Catches missing CSV files during extraction
- **KeyError**: Catches missing columns during transformation
- **Exception**: Catches database connection and loading errors
- **Finally Block**: Executes regardless of success/failure to log completion

---

## 🚀 How to Run the Project

### Step 1: Prepare CSV Files
Place the following CSV files in the same directory as `hospital_etl.py`:
- `patients.csv`
- `doctors.csv`
- `appointments.csv`
- `billing.csv`

### Step 2: Install Dependencies
```bash
pip install pandas sqlalchemy pymysql
```

### Step 3: Setup MySQL Database
```sql
CREATE DATABASE practice;
```

### Step 4: Run the Pipeline
```bash
python hospital_etl.py
```

### Step 5: Verify Data in MySQL
```sql
SELECT * FROM hospital_Data;
```

---

## 📁 Project Structure

```
Hospital_ETL_Pipeline/
├── hospital_etl.py          # Main ETL pipeline script
├── README.md                # Project documentation
├── patients.csv             # Patient data (input)
├── doctors.csv              # Doctor data (input)
├── appointments.csv         # Appointment data (input)
└── billing.csv              # Billing data (input)
```

---

## 📊 Output

After successful execution, the pipeline will:
1. Extract data from all 4 CSV files
2. Print **Total Revenue** to console
3. Print **Revenue by Department** to console
4. Load consolidated data to MySQL `hospital_Data` table
5. Display success/completion messages

---

## 🔍 Key Features

- ✅ **Scalable Data Pipeline**: Handles multiple data sources
- ✅ **Data Quality**: Comprehensive data cleaning and validation
- ✅ **Analytics Ready**: Pre-computed metrics and categorizations
- ✅ **Error Resilient**: Try-except-finally blocks prevent crashes
- ✅ **Database Integration**: Direct MySQL integration for persistence
- ✅ **Maintainable Code**: Clear function separation and documentation

---

## ⚠️ Important Notes

1. **Database Credentials**: Update MySQL credentials in `hospital_etl.py` if different from `root:root`
2. **CSV Format**: Ensure CSV files have correct column names as referenced in the code
3. **Directory**: Place all CSV files in the same directory as the Python script
4. **MySQL Server**: Ensure MySQL server is running before executing the pipeline

---

## 🤝 Contributing

Feel free to fork and submit pull requests for improvements!

---

## 📝 License

This project is open source and available for educational purposes.
