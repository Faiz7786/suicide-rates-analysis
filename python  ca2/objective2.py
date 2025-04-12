# Heatmap of Suicide Rate by Age Group & Year

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"C:\Users\Faiz Inamdar\OneDrive\Desktop\python  ca2\Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv")

# Drop unnecessary columns
df_cleaned = df.drop(columns=[
    "UNIT", "UNIT_NUM", "STUB_NAME_NUM", "STUB_LABEL_NUM", "YEAR_NUM", "AGE_NUM", "FLAG"
])

# Rename columns for clarity
df_cleaned.rename(columns={
    "STUB_LABEL": "Demographic",
    "AGE": "AgeGroup",
    "ESTIMATE": "SuicideRate"
}, inplace=True)

# Create a pivot table: rows = AgeGroup, columns = YEAR, values = SuicideRate (mean across demographics)
pivot_table = df_cleaned.pivot_table(
    index='AgeGroup', 
    columns='YEAR', 
    values='SuicideRate', 
    aggfunc='mean'
)

# Plotting the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, cmap='YlOrBr', annot=True, fmt=".1f", linewidths=.5)
plt.title('Average Suicide Rate by Age Group and Year')
plt.xlabel('Year')
plt.ylabel('Age Group')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
