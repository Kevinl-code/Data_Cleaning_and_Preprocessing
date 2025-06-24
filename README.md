# Data Cleaning and Preprocessing  
**Cleaning and preprocessing marketing customer data**

## 🔍 Objective
Clean and preprocess the `marketing_customers.csv` dataset to ensure it is ready for analysis by:
- Handling missing values  
- Fixing data types  
- Standardizing text fields  
- Adding placeholder values for testing  

## ✅ Key Steps
- Handled missing values in `gender`, `country`, and `age`.
- Added placeholder fields: `date`, `name`, `gender`, `country_name`, `age`.
- Removed duplicate rows.
- Renamed columns for consistency (lowercase + snake_case).
- Standardized text fields (e.g., gender values like 'Male'/'Female', full country names).
- Ensured the `age` column contains integers only.
- Exported the cleaned dataset as `marketing_customers_cleaned.csv`.

## 📁 Files Included
| File | Description |
|------|-------------|
| `marketing_customers.csv` | Raw input CSV file |
| `task1.py` | Python script for data cleaning |
| `marketing_customers_cleaned.csv` | Cleaned output CSV file |
| `README.md` | This documentation |

## 🛠 Tools Used
- **Python 3.12**
- **Pandas** – For data manipulation
- **NumPy** – For numerical operations

## 🧾 Summary

### Marketing Customers Data Cleaning

This project performs comprehensive data cleaning and preprocessing on the `marketing_customers.csv` dataset to prepare it for further analysis or modeling.

Key actions performed:
- Loaded and inspected the dataset using Pandas.
- Added synthetic columns such as `date`, `name`, `gender`, `country_name`, and `age` with logical or random placeholder values.
- Filled missing values in the `age` column using the median value and converted the column to integer type.
- Removed duplicate rows.
- Renamed all columns to lowercase with underscores (`snake_case`) for consistency.
- Converted date columns to proper `datetime` format.
- Validated and corrected data types (e.g., ensuring numeric fields like `store_id` are correct).
- Standardized textual fields including gender (`Male`/`Female`), country names (full names instead of codes), and formatted names properly.
- Saved the final cleaned dataset to `marketing_customers_cleaned.csv`.

## 🧠 Author
<p>
  <img src="./kevin.jpg" width="100" height="100">          
</p>    

**Kevin Lazarus**  
*First-Year M.Sc. Data Science Student*  
*Bishop Heber College, Tiruchirappalli (Trichy), Tamil Nadu, India*

This data cleaning process task was completed as part of internship and skill development in the field of Data Science. It demonstrates core competencies in data preprocessing, Python scripting, and data manipulation using libraries such as Pandas and NumPy.

🔗 *Connect & Learn More:*  
📧 Email: kevinlazarus2003@example.com  
🐙 LinkedIn: https://www.linkedin.com/in/kevinlazarusb 
