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
  
# Summary
  ## Marketing Customers Data Cleaning

  This project performs data cleaning and preprocessing on the `marketing_customers.csv` dataset to prepare it for further analysis or modeling.
   - The input file used is marketing_customers.csv.
   - The output file generated is marketing_customers_cleaned.csv.
   - The dataset was loaded and inspected using pandas, with initial information and sample rows displayed.
   - Synthetic columns were added, including date, name, gender, country name, and age, with logical or random values.
   - Missing age values were handled by filling them with the median and converting the column to integers.
   - Duplicate rows were removed from the dataset.
   - Column names were renamed to lowercase with underscores for consistency.
   - Date columns were standardized by converting them to proper datetime format.
   - Data types were validated and fixed, particularly numeric fields like store_id (if present).
   - Text fields were standardized, including gender values, country names, and proper formatting of names.
   - The cleaned dataset was saved to a new CSV file named marketing_customers_cleaned.csv.

# Author
### Kevin Lazarus
### First Year M.sc Data Science
### Bishop Heber College, Trichy
