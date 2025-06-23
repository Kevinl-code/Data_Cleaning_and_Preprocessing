# Task 1:   Data Cleaning and Preprocessing
  Cleaning and preprocessing marketing customer data

## 🔍 Objective
  Clean and preprocess the `marketing_customers.csv` dataset to ensure it is analysis-ready by handling missing values, fixing data types, standardizing text fields, and adding placeholder values for  testing.

# ✅ Key Steps
- Handled missing values in `gender`, `country`, and `age`.
- Added placeholder fields: `date`, `name`, `gender`, `country_name`, `age`.
- Removed duplicates.
- Renamed columns for consistency.
- Standardized text (e.g., gender values, country names).
- Ensured `age` column is integer type.
- Exported cleaned dataset.

# 📁 Files Included
- `marketing_customers.csv` – Raw input file.
- `task1.py` – Full Python cleaning script.
- `marketing_customers_cleaned.csv` – Final cleaned output.
- `README.md` – This file.

# 🛠 Tools Used
- Python 3.12
- Pandas
- NumPy
  
## Marketing Customers Data Cleaning

This project performs data cleaning and preprocessing on the `marketing_customers.csv` dataset to prepare it for further analysis or modeling.

---

## Input and Output

```bash
# Input File
marketing_customers.csv

# Output File
marketing_customers_cleaned.csv
## 1. Load and Inspect Dataset

# Import libraries and load data
import pandas as pd
df = pd.read_csv("marketing_customers.csv")

# Inspect structure
df.info()
df.head()
## 2. Add Synthetic Columns

# Add columns: DATE, name, gender, country_name, age
# (Values generated logically/randomly)
## 3. Handle Missing Values

# Fill missing 'age' with median
df['age'].fillna(df['age'].median(), inplace=True)

# Convert 'age' to integer
df['age'] = df['age'].astype(int)
## 4. Remove Duplicates

# Drop duplicate rows
df.drop_duplicates(inplace=True)
## 5. Rename Columns

# Standardize column names to lowercase with underscores
df.columns = [col.lower().replace(" ", "_") for col in df.columns]
## 6. Date Standardization

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])
## 7. Data Type Fixes

# Convert 'store_id' to numeric if exists
df['store_id'] = pd.to_numeric(df.get('store_id'), errors='ignore')
## 8. Text Standardization

# Standardize 'gender' values
df['gender'] = df['gender'].str.lower().replace({
    'm': 'male', 'male': 'male', 'f': 'female', 'female': 'female'
})

# Standardize 'country_name' values
country_map = {
    'usa': 'United States',
    'us': 'United States',
    'uk': 'United Kingdom',
    'united states': 'United States'
}
df['country_name'] = df['country_name'].str.lower().map(country_map).fillna(df['country_name'])

# Format 'name' properly
df['name'] = df['name'].str.title().str.strip()
## 9. Save Cleaned Data

# Export cleaned DataFrame to CSV
df.to_csv("marketing_customers_cleaned.csv", index=False)
```
# Author
Kevin Lazarus
First Year M.sc Data Science
Bishop Heber College, Trichy
