import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Walmart_Sales.csv')

plt.figure(figsize=(10, 6))
# bins 30 is used to provide a detailed view of the distribution frequency
plt.hist(df['Weekly_Sales'], bins=30, color='mediumpurple', edgecolor='black')

plt.title('Task 6: Frequency Distribution of Weekly Sales')
plt.xlabel('Weekly Sales Amount ($)')
plt.ylabel('Count of Weeks')
plt.show()