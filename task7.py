import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Walmart_Sales.csv')

# Proportional share of the top 5 stores
top_5_sales = df.groupby('Store')['Weekly_Sales'].sum().nlargest(5)

plt.figure(figsize=(8, 8))

# autopct displays the percentage on each slice
plt.pie(top_5_sales, labels=top_5_sales.index, autopct='%1.1f%%', startangle=140)

plt.title('Task 7: Market Share of Top 5 Stores')
plt.show()