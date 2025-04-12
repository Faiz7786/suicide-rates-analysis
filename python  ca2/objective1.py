# objective2:- # Line plot of suicide rate over time (all data combined)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Set seaborn style
sns.set(style="whitegrid")

# Line plot of suicide rate over time (all data combined)
plt.figure(figsize=(10, 6))
sns.lineplot(x="YEAR", y="SuicideRate", data=df_cleaned)
plt.title('Suicide Rate Over Time')
plt.xlabel('Year')
plt.ylabel('Death Rate per 100,000')
plt.grid(True)
plt.tight_layout()
plt.show()
