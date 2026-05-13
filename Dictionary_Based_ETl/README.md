## 📌 About This Project

A fully functional **ETL (Extract, Transform, Load) Pipeline** built using
Python, Pandas, and MySQL as part of my Data Engineering learning journey.

This pipeline:
- **Extracts** raw data into a Pandas DataFrame
- **Transforms** it by cleaning missing values, fixing data types,
  and adding calculated columns
- **Loads** the clean data into a MySQL database

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core programming language |
| Pandas | Data manipulation & cleaning |
| SQLAlchemy | Database connection |
| MySQL | Data storage |
| VS Code | Development environment |

---

## 📊 Pipeline Architecture

```
Raw Data (with missing values)
        ↓
   Extract()
   → Load into Pandas DataFrame
        ↓
   Clean/Transform()
   → Drop rows with missing Customer_Name
   → Fill missing Price with mean
   → Fill missing Quantity with 1
   → Add Total_Value (Price × Quantity)
   → Add Tax (18% of Total_Value)
   → Add Final_Amount (Total_Value + Tax)
        ↓
   Load()
   → Push clean data to MySQL
   → Table: clean_orders
        ↓
   ✅ Clean Data Ready for Analysis!
```

---

## 🧹 Data Cleaning Steps

| Step | Action | Method |
|------|--------|--------|
| Missing Customer | Drop rows | `dropna(subset=["Customer_Name"])` |
| Missing Price | Fill with average | `fillna(mean())` |
| Missing Quantity | Fill with 1 | `fillna(1)` |
| City formatting | Capitalize | `str.title()` |
| New column | Total Value | `Price × Quantity` |
| New column | Tax | `Total_Value × 0.18` |
| New column | Final Amount | `Total_Value + Tax` |

---

## 💻 Code Structure

```
Etl_Pipeline.py
├── def Etl()        → Extract raw data
├── def Clean(df)    → Transform & clean
└── def load(df)     → Load to MySQL
```

---

## 🚀 How to Run

### 1. Install Requirements
```bash
pip install pandas  sqlalchemy pymysql
```

### 2. Setup MySQL
```sql
CREATE DATABASE practice;
```

### 3. Run Pipeline
```bash
python Etl_Pipeline.py
```

### 4. Verify in MySQL
```sql
SELECT * FROM clean_orders;
```

---

## 📸 Output

### Before Cleaning
| Order_id | Customer_Name | Price | Status |
|----------|--------------|-------|--------|
| 103 | None | None | delivered |
| 107 | None | 45000 | delivered |

### After Cleaning & Loading to MySQL
| Order_id | Customer_Name | City | Price | Total_Value | Tax | Final_Amount |
|----------|--------------|------|-------|-------------|-----|--------------|
| 101 | Rahul | Pune | 60000 | 60000 | 10800 | 70800 |
| 102 | Priya | Mumbai | 30000 | 60000 | 5400 | 35400 |
| 105 | Sneha | Bangalore | 30000 | 60000 | 5400 | 35400 |
| 106 | Ravi | Mumbai | 2000 | 6000 | 360 | 2360 |

---

## 📚 What I Learned

- Building end-to-end ETL pipelines
- Data cleaning with Pandas (fillna, dropna, to_numeric)
- Handling missing and inconsistent data
- Connecting Python to MySQL using SQLAlchemy
- Adding calculated columns with NumPy
- Real-world data engineering workflow

---

## 👨‍💻 About Me

I am **Saurabh**, an aspiring Data Engineer actively learning:
- Python & Pandas
- SQL (MySQL)
- ETL Pipelines
- Data Engineering concepts

Currently building projects to strengthen my skills and
working towards becoming a professional Data Engineer! 🚀

---

⭐ **If you found this helpful, give it a star!** ⭐
