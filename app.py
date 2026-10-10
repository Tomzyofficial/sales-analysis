import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Sales_transactions_2022_2025.csv.xlsx")

# This will show which sales channel generates the highest average sales amount per transaction. Using the groupby function, we can group the data by sales channel and calculate the mean sales amount for each channel. Then, we can sort the results in descending order to see which channel has the highest average sales amount.
channel_sales = df.groupby("Sales_Channel")["Sales_Amount"].mean()
channel_sales = channel_sales.sort_values(ascending=False)
print("Average Sales Amount by Sales Channel:")
print(channel_sales)

# This will show which product category generates the highest total profit. Using the groupby function, we can group the data by product category and calculate the total profit for each category. Then, we can sort the results in descending order to see which category has the highest total profit.
category_profit = df.groupby("Product_Category")["Profit"].sum()
category_profit = category_profit.sort_values(ascending=False)
print("Total Profit by Product Category:")
print(category_profit)

# Create the graph
plt.figure(figsize=(10, 6))

category_profit.plot(kind="bar")

plt.title("Total Profit by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()