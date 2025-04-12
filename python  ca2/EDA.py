# Performed Eda On the Data set :- Objective 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\Faiz Inamdar\OneDrive\Desktop\python  ca2\Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv")

# Display first few rows
print(df.head())
# Overview of dataset
print(df.info())

# Summary statistics
print(df.describe(include='all'))

# Check for missing values
print(df.isnull().sum())
# Drop unnecessary columns (example: UNIT, UNIT_NUM, STUB_NAME_NUM, etc.)
df_cleaned = df.drop(columns=["UNIT", "UNIT_NUM", "STUB_NAME_NUM", "STUB_LABEL_NUM", "YEAR_NUM", "AGE_NUM", "FLAG"])

# Rename for clarity
df_cleaned.rename(columns={
    "STUB_LABEL": "Demographic",
    "AGE": "AgeGroup",
    "ESTIMATE": "SuicideRate"
}, inplace=True)

# Check cleaned dataset
print(df_cleaned.head())
