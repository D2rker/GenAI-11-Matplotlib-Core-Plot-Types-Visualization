import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Walmart_Sales.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Grouping by date to get total sales across all stores per week
sales_over_time = df.groupby('Date')['Weekly_Sales'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(sales_over_time['Date'], sales_over_time['Weekly_Sales'], color='tab:blue', marker='o', markersize=3)

plt.title('Task 1: Total Walmart Sales Over Time (2010-2012)')
plt.xlabel('Timeline')
plt.ylabel('Total Sales ($)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()