import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

"""
Retail Store Sales Dashboard
Tools:

NumPy: Random data gen
Pandas: GroupBy, Pivot, Resample

Features:

Generate daily sales for products
Group by category / product / customer
Monthly sales trend
Best-selling product
Export report with .to_excel()

"""
# ----------------------
# Retail Sales Analysis Dashboard
# ----------------------

np.random.seed(42)

# Step 1 : Generate sample retail store data
category_product_map = {
    "Dairy": ["Milk", "Butter", "Chees"],
    "Bakery": ["Bread"],
    "Grains": ["Rice"],
    "Pantry": ["Sugar", "Salt"],
    "Meat": ["Chicken", "Fish"],
    "Fruits": ["Apple", "Bananas", "Oranges"],
    "Vegetables": ["Tomatoes", "Potatoes", "Onions"],
    "Personal Care": ["Soap", "Shampoos", "Toothpaste"],
    "Household": ["Detergent"]
}

product_to_category = {product: category for category, products in category_product_map.items() for product in products}
all_products = list(product_to_category)
order_date = [datetime(2023, 1, 1) + timedelta(days=i) for i in range(100)]

retail_data = pd.DataFrame({
    "OrderId" : np.arange(1001, 1101),
    "CustomerID" : np.random.randint(101, 121, size=100),
    "Customer" : np.random.choice(["Amit", "Sneha", "Riya", "Vishal", "Raj", "Chirag", "Piyush", "Yogesh"], size=100),
    "OrderDate" : np.random.choice(order_date, size=100),
    "Product" : np.random.choice(all_products, size=100),
    "Quantity" : np.random.randint(1,5, size=100)
})

retail_data["Category"] = retail_data["Product"].map(product_to_category)
retail_data["UnitPrice"] = np.random.randint(100, 1000, size=100)
retail_data["Total"] = retail_data["Quantity"] * retail_data["UnitPrice"]

# set OrderDate as index
retail_data["OrderDate"] = pd.to_datetime(retail_data["OrderDate"])
retail_data.set_index("OrderDate", inplace=True)

# ----------------------
# Analysis & Insights
# ----------------------

# Generate daily sales for products
daily_sales = retail_data.resample("D")["Total"].sum().head()

# Monthly sales trend
month_sales = retail_data.resample("ME")["Total"].sum()

# Group by category / product / customer
grouped = retail_data.groupby(["CustomerID", "Product", "Category"])["Total"].sum()

# Best-selling product
group_price = retail_data.groupby("Product")["Total"].sum()
best_selling = group_price.sort_values(ascending=False).head(5)

# Top customer's
group_customer = retail_data.groupby(["Customer", "Product"])["Total"].sum()
top_cus = group_customer.sort_values(ascending=False).head(5)

# ----------------------
# Visualizations
# ----------------------

sns.set_theme(style="whitegrid")

# Count Chart - Sales by Product
plt.figure(figsize=(10, 5))
order = retail_data["Category"].value_counts().index
sns.countplot(x="Category", data= retail_data, order=order, hue=retail_data["Category"], palette="Blues", legend=False)
plt.title("Order Count by Category")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("order_count_by_category.png")
plt.show()

# Line Chart - Monthly Revenue
plt.figure(figsize=(8,5))
sns.lineplot(x=month_sales.index, y=month_sales.values, marker='o', color='blue')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.show()

# Boxplot of Total Sales by Category
plt.figure(figsize=(10, 5))
sns.boxplot(x="Category", y="Total", data=retail_data, hue="Category", palette="Set3", legend=False)
plt.title("Sales Distribution by Category")
plt.xticks(rotation=30)
plt.savefig("sales_distribution.png")
plt.show()

# Heatmap of Correlation
corr = retail_data[["Quantity", "UnitPrice", "Total"]].corr()
plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap="YlGnBu", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("corr_heatmap.png")
plt.show()

# ----------------------
# Export to CSV
# ----------------------

retail_data.to_csv("retail_store_sales.csv", index=False)
print("Retail Store Sales Dashboard completed & data exported!")