## 📌 About This Project

A fully functional **ETL (Extract, Transform, Load) Pipeline** built for
Manufacturing and Supply Chain domain using Python, Pandas, NumPy and MySQL.

This pipeline processes **4 data sources** and delivers clean,
analytics-ready data with business KPIs.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core programming language |
| Pandas | Data manipulation & transformation |
| NumPy | Numerical calculations (Defect Rate) |
| SQLAlchemy | MySQL database connectivity |
| MySQL | Data storage & persistence |
| Logging | Pipeline monitoring & error tracking |
| VS Code | Development environment |
| GitHub | Version control & portfolio |

---

## 📊 Pipeline Architecture

```
4 CSV Data Sources
        ↓
   extract()
   → suppliers.csv
   → inventory.csv
   → purchase_orders.csv
   → production.csv
        ↓
   transform()
   → Clean missing values
   → Standardize text data
   → Calculate business KPIs
   → Filter active/completed records
   → Merge all 4 tables
   → Add Total_Value column
        ↓
   load()
   → Push to MySQL
   → Table: supply_chain_analytics
        ↓
   ✅ Analytics Ready Data!
```

---

## 🧹 Data Cleaning & Transformation

### 🏢 Suppliers
| Step | Action | Method |
|------|--------|--------|
| Missing Email | Fill with "not_provided" | `fillna()` |
| Missing Contact | Fill with "Unknown" | `fillna()` |
| City Names | Standardize casing | `str.capitalize()` |
| Filter | Active suppliers only | Boolean filter |

### 📦 Inventory
| Step | Action | Method |
|------|--------|--------|
| Missing Selling_Price | Fill with mean | `fillna(mean())` |
| Missing Unit_Cost | Fill with mean | `fillna(mean())` |
| Profit_Margin | Selling - Cost | Calculated column |
| Profit_Percent | Margin/Cost × 100 | Calculated column |
| Stock_Status | Reorder check | `apply(lambda)` |

### 🛒 Purchase Orders
| Step | Action | Method |
|------|--------|--------|
| Missing Delivery | Fill with "Pending" | `fillna()` |
| Missing Quality | Fill with "Pending" | `fillna()` |
| Missing Unit_Price | Fill with mean | `fillna(mean())` |
| Delivery_Status | On Time/Delayed/Not Delivered | `apply(lambda)` |

### 🏗️ Production
| Step | Action | Method |
|------|--------|--------|
| Missing Actual_Quantity | Fill with 0 | `fillna(0)` |
| Missing Production_Cost | Fill with mean | `fillna(mean())` |
| Defect_Rate | Defects/Quantity × 100 | `np.where()` |
| Quality_Grade | Excellent/Good/Needs Improvement | `apply(lambda)` |

---

## 📈 Business KPIs Generated

```
→ Profit Margin per Product
→ Profit Percentage per Product
→ Stock Status (Reorder Needed / Sufficient)
→ Delivery Performance (On Time / Delayed)
→ Defect Rate per Production Run
→ Quality Grade per Production Run
→ Total Purchase Value per Order
```

---

## 💻 Code Structure

```
Manufacturing_Supply_Chain.py
├── extract()      → Read 4 CSV files with error handling
├── transform()    → Clean, calculate KPIs, merge tables
└── load()         → Push analytics data to MySQL
```

---

## 🔒 Error Handling

```python
# File not found handling
except FileNotFoundError as e:
    logging.error(f"File is not available!! {e}")

# Column missing handling
except KeyError as e:
    logging.error(f"Column not found {e}")

# Database load handling
except Exception as e:
    logging.error(f"Data Failed to load!! {e}")

# Cleanup always runs
finally:
    logging.info("Process completed")
```

---

## 📝 Logging

```
Pipeline uses Python logging module
for monitoring all ETL stages:

INFO  → Extraction started/completed
INFO  → Transformation started/completed
INFO  → Data loading started
ERROR → File not found
ERROR → Column missing
ERROR → Database connection failed
```

---

## 🚀 How to Run

### 1. Install Requirements
```bash
pip install pandas numpy sqlalchemy pymysql
```

### 2. Setup MySQL Database
```sql
CREATE DATABASE practice;
```

### 3. Place CSV Files
```
Place these files in project folder:
→ suppliers.csv
→ inventory.csv
→ purchase_orders.csv
→ production.csv
```

### 4. Run Pipeline
```bash
python Manufacturing_Supply_Chain.py
```

### 5. Verify in MySQL
```sql
SELECT * FROM supply_chain_analytics;
```

---

## 📸 Data Sources

| File | Records | Description |
|------|---------|-------------|
| suppliers.csv | 10 | Supplier master data |
| inventory.csv | 15 | Product & stock data |
| purchase_orders.csv | 15 | PO transactions |
| production.csv | 15 | Manufacturing runs |

---

## 🎯 Key Concepts Used

```
✅ ETL Pipeline Architecture
✅ CSV Data Extraction
✅ Missing Value Handling (fillna, dropna)
✅ Data Type Conversion
✅ Lambda Functions for Categorization
✅ np.where() for Conditional Logic
✅ apply() with axis=1 for Row-wise Logic
✅ Multi-table Merge with Suffixes
✅ Business KPI Calculations
✅ try/except/finally Error Handling
✅ Python Logging Module
✅ SQLAlchemy MySQL Integration
✅ DataFrame Column Operations
```

---

## 📚 What I Learned

- Building production-style ETL pipelines
- Handling real-world messy data from multiple sources
- Implementing proper error handling with specific exceptions
- Using Python logging for pipeline monitoring
- Calculating business KPIs using Pandas and NumPy
- Merging multiple DataFrames with suffix handling
- Loading transformed data to MySQL using SQLAlchemy

---

## 🗺️ What's Next

- [ ] Add Apache Airflow for pipeline scheduling
- [ ] Deploy to AWS/GCP cloud
- [ ] Add data validation layer
- [ ] Build dashboard using Power BI / Tableau
- [ ] Implement PySpark for large-scale data

---

## 👨‍💻 About Me

I am **Saurabh Jadhav**, an aspiring Data Engineer actively learning:
- Python & Pandas for data engineering
- SQL (MySQL) — advanced queries & stored procedures
- ETL Pipeline development
- Error handling & logging best practices
- Data Engineering tools & concepts

Currently pursuing **BCA** and building real-world projects
to strengthen my data engineering skills! 🚀


⭐ **If you found this helpful, give it a star!** ⭐






      

   


   




    

