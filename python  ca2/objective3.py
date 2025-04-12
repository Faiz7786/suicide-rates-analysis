# Plotting a histogram of the suicide rate estimates

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv(r"C:\Users\Faiz Inamdar\OneDrive\Desktop\python  ca2\Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv")


plt.figure(figsize=(10, 6))
plt.hist(df['ESTIMATE'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Suicide Rates')
plt.xlabel('Suicide Rate (per 100,000 population)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()
