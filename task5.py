import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Walmart_Sales.csv')
# Analyze top 5 stores
top_5 = df.groupby('Store')['Weekly_Sales'].sum().nlargest(5).index
holiday_split = df[df['Store'].isin(top_5)].groupby(['Store', 'Holiday_Flag'])['Weekly_Sales'].sum().unstack()

plt.figure(figsize=(10, 6))
# Using the 'bottom' parameter to stack holiday sales on top of non-holiday
plt.bar(holiday_split.index.astype(str), holiday_split[0], label='Non-Holiday', color='silver')
plt.bar(holiday_split.index.astype(str), holiday_split[1], bottom=holiday_split[0], label='Holiday', color='orange')

plt.title('Task 5: Holiday vs. Non-Holiday Contribution')
plt.xlabel('Store Number')
plt.ylabel('Total Sales ($)')
plt.legend()
plt.show()