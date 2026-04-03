import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Walmart_Sales.csv')
df['Year'] = pd.to_datetime(df['Date'], format='%d-%m-%Y').dt.year

# Filter for top 3 stores to keep the chart readable
top_stores = [20, 4, 14]
yearly_data = df[df['Store'].isin(top_stores)].groupby(['Store', 'Year'])['Weekly_Sales'].sum().unstack()

x = np.arange(len(top_stores))
width = 0.25

plt.figure(figsize=(10, 6))
plt.bar(x - width, yearly_data[2010], width, label='2010')
plt.bar(x, yearly_data[2011], width, label='2011')
plt.bar(x + width, yearly_data[2012], width, label='2012')

plt.title('Task 4: Comparative Yearly Sales for Top Stores')
plt.xticks(x, top_stores)
plt.xlabel('Store Number')
plt.ylabel('Total Sales ($)')
plt.legend()
plt.show()