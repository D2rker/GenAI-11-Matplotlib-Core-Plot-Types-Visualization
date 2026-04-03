import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Walmart_Sales.csv')
store_performance = df.groupby('Store')['Weekly_Sales'].sum().sort_values(ascending=False).head(10)

# 3a. Vertical Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(store_performance.index.astype(str), store_performance.values, color='skyblue')
plt.title('Task 3a: Top 10 Stores (Vertical Comparison)')
plt.xlabel('Store Number')
plt.ylabel('Total Sales ($)')
plt.show()

# 3b. Horizontal Bar Chart
plt.figure(figsize=(10, 5))
plt.barh(store_performance.index.astype(str), store_performance.values, color='lightcoral')
plt.title('Task 3b: Top 10 Stores (Horizontal Comparison)')
plt.xlabel('Total Sales ($)')
plt.ylabel('Store Number')
plt.gca().invert_yaxis() # Invert to show highest sales at the top
plt.show()