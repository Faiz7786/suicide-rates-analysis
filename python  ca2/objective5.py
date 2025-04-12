import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset

df = pd.read_csv(r"C:\Users\Faiz Inamdar\OneDrive\Desktop\python  ca2\Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv")

# Filter for all ages and select only male and female entries
df_filtered = df[(df['AGE'] == 'All ages') & (df['STUB_LABEL'].isin(['Male', 'Female']))]

# Group by sex and calculate the mean suicide rate
grouped = df_filtered.groupby('STUB_LABEL')['ESTIMATE'].mean()

# Plot the pie chart
plt.figure(figsize=(6, 6))
plt.pie(grouped, labels=grouped.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'salmon'])
plt.title('Average Suicide Rate Distribution by Sex (All Years)')
plt.axis('equal')  # Ensures pie is a circle
plt.tight_layout()
plt.show()
