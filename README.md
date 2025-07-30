# 🛍️ Retail Sales Analysis Dashboard

This project simulates and analyses retail store sales data using **Pandas**, **NumPy**, **Seaborn**, and **Matplotlib**. It encompasses data generation, sales analysis, and various visualisations to reveal key business insights.

---

## 📦 Features

- Generate realistic product sales data
- Analyse daily and monthly sales
- Identify top-performing products and customers
- Group by Category, Customer, and Product
- Visualise:
  - Count of orders by category
  - Monthly revenue trends
  - Sales distribution using box plots
  - Correlation using heatmaps

---

## 📊 Tech Stack

- Python 🐍
- Pandas
- NumPy
- Seaborn
- Matplotlib

---

## 📁 Dataset Structure

| Column     | Description                  |
| ---------- | ---------------------------- |
| OrderId    | Unique ID per order          |
| CustomerID | Customer identifier          |
| Customer   | Customer name                |
| OrderDate  | Date of the order            |
| Product    | Product sold                 |
| Category   | Product category             |
| Quantity   | Number of units sold         |
| UnitPrice  | Price per unit               |
| Total      | Total = Quantity × UnitPrice |

---

## 📈 Visualizations

1. **Countplot**: Orders by category
2. **Lineplot**: Monthly revenue trends
3. **Boxplot**: Distribution of total sales by category
4. **Heatmap**: Correlation between Quantity, Price, and Total

---

## 🔍 Insights Summary

### ✅ What's Performing Well

- Products like **Milk** and **Rice** generate the highest revenue.
- Categories like **Dairy** and **Grains** are top-performing.
- Customers such as **Sneha** and **Vishal** are frequent high-value buyers.

### ⚠️ What Needs Attention

- Categories like **Household** and **Bakery** have low sales.
- Revenue dips are observed during some months (e.g., March).
- Outliers in sales might indicate bulk orders or data entry issues.

### 📊 Trends & Surprises

- Sales spike in months like **January** and **April**, showing seasonal effects.
- High correlation between quantity and total confirms clean data generation.

---

## 📤 Output

- Retail dataset exported as: `retail_store_sales.csv`
- Ready to integrate with BI tools (Power BI / Tableau)

---

## 🚀 How to Run

```bash
pip install pandas numpy seaborn matplotlib
python retail_sales_dashboard.py
```

---

## 📌 Author

**Vishal Patil**\
Salesforce + Data Analyst Enthusiast 🌐

---

##
