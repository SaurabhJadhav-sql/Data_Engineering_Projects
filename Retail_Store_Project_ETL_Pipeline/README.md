# 🛒 Retail Store Analytics ETL Pipeline

## 📌 Project Overview

This project is a complete **ETL (Extract, Transform, Load) Pipeline** built using **Python, Pandas, and MySQL** for retail store analytics.

The pipeline extracts raw CSV data from multiple sources, performs data cleaning and business transformations, merges datasets, creates analytical features, and finally loads the processed data into a MySQL database.

🚀 This project simulates a real-world beginner-level Data Engineering workflow.

---

# 🛠️ Technologies Used

- 🐍 Python
- 🐼 Pandas
- 🗄️ MySQL
- ⚙️ SQLAlchemy
- 📄 CSV Files
- 💻 VS Code

---

# 🔄 ETL Workflow

## 📥 1. Extract Phase

The pipeline reads multiple CSV files:

- 👥 Customers Data
- 📦 Orders Data
- 🧾 Order Items Data
- 🛍️ Products Data

Using:

```python
pd.read_csv()
🔧 2. Transform Phase
👥 Customer Transformations

✔️ Filled missing email values
✔️ Standardized city names
✔️ Created customer age groups:

Young
Mid
Senior
🛍️ Product Transformations

✔️ Filled missing selling prices
✔️ Calculated:

Profit Margin
Profit Percentage
📦 Order Transformations

✔️ Filtered only delivered orders
✔️ Handled missing delivery dates

🧾 Order Items Transformations

✔️ Filled missing unit prices
✔️ Calculated:

Total Values
Tax
Final Amount
🧠 Business Logic Implemented
💰 Order Classification

Orders are categorized as:

🔥 High Value
⚡ Medium Value
📉 Low Value

Based on final order amount.

👑 Customer Labeling

Customers are labeled as:

VIP
Regular
Logic:

✅ Premium customer + High Value order = VIP
❌ Otherwise = Regular

📊 Data Aggregation

Used Pandas aggregation functions:

groupby()
sum()
reset_index()

To calculate:

Order totals
Revenue analytics
🔗 Data Merging

Merged multiple datasets using:

pd.merge()

Similar to SQL JOIN operations.

🗄️ 3. Load Phase

The final transformed dataset is loaded into a MySQL database using:

to_sql()
🚀 Skills Demonstrated

✅ ETL Pipeline Development
✅ Data Cleaning
✅ Feature Engineering
✅ Data Transformation
✅ Data Aggregation
✅ Data Merging
✅ MySQL Integration
✅ Business Logic Implementation
✅ Pandas Operations
✅ SQL Concepts

📌 Features Created
Feature	Description
Profit_Margin	Product profit calculation
Profit_Percent	Profit percentage
Total_Values	Total order value
Tax	Tax calculation
Final_Amount	Final payable amount
Order_Size	High/Medium/Low order classification
Customer_Label	VIP/Regular customer classification
📈 Future Improvements
⚠️ Add exception handling
📝 Add logging system
🔐 Use environment variables for credentials
📂 Export cleaned data to CSV/Parquet
⏰ Schedule pipeline execution
📊 Build dashboard integration
☁️ Use Apache Airflow for orchestration
🎯 Project Outcome

Successfully built a beginner-friendly real-world ETL pipeline capable of:

✅ Extracting raw retail data
✅ Cleaning and transforming datasets
✅ Applying business rules
✅ Merging multiple data sources
✅ Loading analytical data into MySQL

👨‍💻 Author
Saurabh Jadhav

🚀 Aspiring Cloud Data Engineer 
     
