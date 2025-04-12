import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"C:\Users\Faiz Inamdar\OneDrive\Desktop\python  ca2\Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv")

# Drop rows with missing suicide rate
df_clean = df.dropna(subset=['ESTIMATE'])

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df_clean['YEAR'], df_clean['ESTIMATE'], alpha=0.6, color='teal', edgecolor='k')
plt.title('Suicide Rates Over Time')
plt.xlabel('Year')
plt.ylabel('Suicide Rate (per 100,000 population)')
plt.grid(True)
plt.tight_layout()
plt.show()
