import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Walmart_Sales.csv')

plt.figure(figsize=(10, 6))

# Using scatter to see the distribution of points
plt.scatter(df['Fuel_Price'], df['Weekly_Sales'], alpha=0.3, color='forestgreen')

plt.title('Task 2: Impact of Fuel Price on Weekly Sales')
plt.xlabel('Fuel Price ($)')
plt.ylabel('Weekly Sales ($)')
plt.grid(True)
plt.show()