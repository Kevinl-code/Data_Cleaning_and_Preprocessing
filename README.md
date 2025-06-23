#Task 1:  Data Cleaning and Preprocessing
  Cleaning and preprocessing marketing customer data

Task Domain: Marketing Customers Data Cleaning 

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
  
# Summary
# ============================================
#   Marketing Customers Dataset - Cleaning Log
# ============================================

# 📁 File Info:
# Input  : marketing_customers.csv
# Output : marketing_customers_cleaned.csv

# --------------------------------------------
# 1. Load & Inspect Dataset
# --------------------------------------------

# Load the CSV
import pandas as pd
df = pd.read_csv("marketing_customers.csv")

# Inspect basic structure
df.info()
df.head()

# --------------------------------------------
# 2. Add Synthetic Columns
# --------------------------------------------

# - DATE: Added sequential datetime values
# - name, gender, country_name, age: filled with random/controlled values

# --------------------------------------------
# 3. Handle Missing Values
# --------------------------------------------

# Fill missing 'age' values with median
df['age'].fillna(df['age'].median(), inplace=True)

# Ensure 'age' column is numeric and integer type
df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(df['age'].median()).astype(int)

# --------------------------------------------
# 4. Remove Duplicate Rows
# --------------------------------------------

df.drop_duplicates(inplace=True)

# --------------------------------------------
# 5. Rename Columns
# --------------------------------------------

# Clean column names: lowercase, underscores
df.columns = [col.lower().replace(' ', '_') for col in df.columns]

# --------------------------------------------
# 6. Standardize Date Format
# --------------------------------------------

# Convert 'date' column to datetime64
df['date'] = pd.to_datetime(df['date'])

# --------------------------------------------
# 7. Fix Data Types
# --------------------------------------------

# Convert potential numeric fields (if present)
# For example: store_id
if 'store_id' in df.columns:
    df['store_id'] = pd.to_numeric(df['store_id'], errors='coerce')

# --------------------------------------------
# 8. Standardize Text Columns
# --------------------------------------------

# Normalize gender values
df['gender'] = df['gender'].str.lower().replace({
    'm': 'male', 'male': 'male',
    'f': 'female', 'female': 'female'
})

# Normalize country_name values
country_map = {
    'usa': 'United States',
    'us': 'United States',
    'uk': 'United Kingdom',
    'united states': 'United States',
    'united kingdom': 'United Kingdom'
}
df['country_name'] = df['country_name'].str.lower().map(country_map).fillna(df['country_name'])

# Clean name field
df['name'] = df['name'].str.title().str.strip()

# --------------------------------------------
# 9. Export Cleaned Data
# --------------------------------------------

# Save to cleaned CSV
df.to_csv("marketing_customers_cleaned.csv", index=False)

# --------------------------------------------
# ✅ Done: Cleaned data ready for use.
# --------------------------------------------

# Author: Kevin Lazarus
# First Year M.Sc. Data Science
# Bishop Heber College, Trichy

