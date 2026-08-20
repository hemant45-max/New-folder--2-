import pandas as pd
import matplotlib.pyplot as plt

filename = "synthetic_online_retail_data.csv"
df = pd.read_csv(filename)

plt.figure(figsize=(8,5))

plt.hist(df['age'], bins=15, color='skyblue', edgecolor='black')

plt.title('Customer Age Distribution', fontsize=14)
plt.xlabel('Age of Customer', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)

plt.savefig('age_distribution.png')
plt.savefig('age_distribution.png')

print("--- BUSINESS INSIIGHTS BREAKDOWN ---")

print(df['payment_method'].value_counts())