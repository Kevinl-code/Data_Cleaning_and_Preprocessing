import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Load the dataset
df = pd.read_csv('marketing_customers.csv')

# --- Add placeholder columns ---
num_rows = len(df)

# Generate 'DATE' column
start_date = datetime(2023, 1, 1)
df['DATE'] = [start_date + timedelta(days=i) for i in range(num_rows)]

# Generate 'name' column
df['name'] = [f"Customer {i+1}" for i in range(num_rows)]

# Generate messy 'gender' column
df['gender'] = random.choices(['Male', 'Female', 'MALE ', 'FEMALE ', 'm', 'f'], k=num_rows)

# Generate messy 'country_name' column
countries = ['USA', 'Canada', 'UK', 'Australia', 'Germany', 'France', 'India', 'Japan', 'China', 'Brazil', 'usa ', ' united kingdom']
df['country_name'] = random.choices(countries, k=num_rows)

# Generate 'age' column with NaNs
ages_raw = np.random.uniform(18, 71, size=num_rows)
num_nans = min(int(num_rows * 0.05), 5)
nan_indices = random.sample(range(num_rows), num_nans)
for idx in nan_indices:
    ages_raw[idx] = np.nan
df['age'] = ages_raw

# --- Info Before Cleaning ---
print("\n--- DataFrame Info After Adding Placeholder Columns ---")
df.info()
print("\n--- DataFrame Head ---")
print(df.head())

# --- Step 1: Handle missing values ---
print("\n--- Missing Values Before Cleaning ---")
print(df.isnull().sum())

df['age'] = pd.to_numeric(df['age'], errors='coerce')
if not df['age'].isnull().all():
    df['age'].fillna(df['age'].median(), inplace=True)
else:
    df['age'].fillna(0, inplace=True)
df['age'] = df['age'].astype(int)  # 🔒 Ensure age is integer

# --- Step 2: Remove duplicate rows ---
df_cleaned = df.drop_duplicates().copy()
print(f"\n--- Rows After Removing Duplicates: {len(df_cleaned)} ---")

# --- Step 3: Clean column headers ---
original_columns = df_cleaned.columns.tolist()
df_cleaned.columns = df_cleaned.columns.str.strip().str.lower().str.replace(' ', '_')
print("\n--- Column Headers Renamed ---")
print(f"Original: {original_columns}")
print(f"Cleaned : {df_cleaned.columns.tolist()}")

# --- Step 4: Standardize 'date' format ---
if 'date' in df_cleaned.columns:
    df_cleaned['date'] = pd.to_datetime(df_cleaned['date'], errors='coerce')
    print("\n--- 'date' column converted ---")
    print(df_cleaned[['date']].head())

# --- Step 5: Fix numeric columns (optional cleanup) ---
print("\n--- Fixing Numeric Columns ---")
numeric_cols = ['store_id', 'store_area', 'items_available', 'daily_customer_count', 'store_sales']
for col in numeric_cols:
    if col in df_cleaned.columns:
        df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce')
        if not df_cleaned[col].isnull().all():
            df_cleaned[col].fillna(df_cleaned[col].median(), inplace=True)
        else:
            df_cleaned[col].fillna(0, inplace=True)
        df_cleaned[col] = df_cleaned[col].astype(int)
        print(f"'{col}' fixed to integer.")

# 🔍 Ensure no duplicate columns
df_cleaned = df_cleaned.loc[:, ~df_cleaned.columns.duplicated()]

# --- Step 6: Standardize text values ---
print("\n--- Standardizing Text Values ---")

if 'gender' in df_cleaned.columns:
    df_cleaned['gender'] = df_cleaned['gender'].astype(str).str.strip().str.lower()
    df_cleaned['gender'] = df_cleaned['gender'].replace({
        'm': 'male', 'f': 'female', 'male ': 'male', 'female ': 'female'
    })
    print("\n'gender' column standardized. Value counts:")
    print(df_cleaned['gender'].value_counts())

if 'country_name' in df_cleaned.columns:
    df_cleaned['country_name'] = df_cleaned['country_name'].str.strip().str.title()
    country_mapping = {
        'Usa': 'United States', 'Uk': 'United Kingdom', 'United Kingdom': 'United Kingdom',
        'Usa ': 'United States', 'United States': 'United States'
    }
    df_cleaned['country_name'] = df_cleaned['country_name'].replace(country_mapping)
    print("\n'country_name' column standardized. Value counts:")
    print(df_cleaned['country_name'].value_counts())

if 'name' in df_cleaned.columns:
    df_cleaned['name'] = df_cleaned['name'].str.strip().str.title()
    print("\n'name' column standardized.")
    print(df_cleaned['name'].head())

# Final assurance for 'age' column
df_cleaned['age'] = pd.to_numeric(df_cleaned['age'], errors='coerce')
df_cleaned['age'].fillna(df_cleaned['age'].median(), inplace=True)
df_cleaned['age'] = df_cleaned['age'].astype(int)
print(f"\n✅ Confirmed 'age' column type: {df_cleaned['age'].dtype}")

# --- Final Output ---
print("\n--- Final Cleaned DataFrame Head ---")
print(df_cleaned.head())
print("\n--- Final Cleaned DataFrame Info ---")
df_cleaned.info()

# --- Save to CSV ---
df_cleaned.to_csv('marketing_customers_cleaned.csv', index=False)
print("\n✅ Cleaned data saved to 'marketing_customers_cleaned.csv'")
