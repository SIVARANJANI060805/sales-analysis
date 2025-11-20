# ---------------------------------------
# 1. Import Libraries
# ---------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------
# 2. Load the CSV file
# ---------------------------------------
df = pd.read_csv("sales.csv")   # Your CSV file name
print("First 5 rows of the data:")
print(df.head())

# ---------------------------------------
# 3. Total sales by Product
# ---------------------------------------
product_sales = df.groupby("Product")["Sales"].sum()
print("\nTotal Sales by Product:")
print(product_sales)

# Plot Product Sales
plt.figure(figsize=(7,5))
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# ---------------------------------------
# 4. Total sales by Month
# ---------------------------------------
monthly_sales = df.groupby("Month")["Sales"].sum()
print("\nTotal Sales by Month:")
print(monthly_sales)

# Plot Monthly Sales
plt.figure(figsize=(7,5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Total Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# ---------------------------------------
# 5. Overall Total Sales
# ---------------------------------------
total_sales = df["Sales"].sum()
print("\nOverall Total Sales:", total_sales)
