import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------- STEP 1: LOAD DATA ----------
DATA_PATH = "data/sales_data.csv"

try:
    df = pd.read_csv(DATA_PATH)
    print("✅ Sales dataset loaded successfully.\n")
except FileNotFoundError:
    print("❌ Error: sales_data.csv not found in data folder.")
    exit()

# ---------- STEP 2: DATA EXPLORATION ----------
print("📌 Dataset Preview:")
print(df.head(), "\n")

print("📌 Dataset Info:")
print(df.info(), "\n")

# ---------- STEP 3: DATA CLEANING ----------
# Handle missing values
df.fillna(0, inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("✅ Data cleaning completed.\n")

# ---------- STEP 4: DATA ANALYSIS ----------

# Total revenue
total_revenue = df["Total_Sales"].sum()

# Total quantity sold
total_quantity = df["Quantity"].sum()

# Best-selling product (by revenue)
product_sales = df.groupby("Product")["Total_Sales"].sum()
best_selling_product = product_sales.idxmax()

# Average sales per transaction
average_sales = df["Total_Sales"].mean()

print("📊 SALES ANALYSIS RESULTS")
print("-" * 35)
print(f"💰 Total Revenue: ₹{total_revenue:,.2f}")
print(f"📦 Total Quantity Sold: {int(total_quantity)}")
print(f"🏆 Best-Selling Product: {best_selling_product}")
print(f"📈 Average Sales per Transaction: ₹{average_sales:,.2f}\n")

# ---------- STEP 5: VISUALIZATION ----------
os.makedirs("visualizations", exist_ok=True)

# Chart 1: Bar chart - Revenue per product
plt.figure()
product_sales.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("visualizations/revenue_by_product.png")
plt.close()

# Chart 2: Line chart - Sales trend (if index represents time/order)
plt.figure()
plt.plot(df["Total_Sales"])
plt.title("Sales Trend")
plt.xlabel("Transaction Index")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/sales_trend.png")
plt.close()

print("📈 Visualizations created successfully.\n")

# ---------- STEP 6: INSIGHTS ----------
print("🧠 KEY INSIGHTS")
print("-" * 35)
print(f"- {best_selling_product} generates the highest revenue.")
print("- Product-wise revenue varies significantly.")
print("- Sales show fluctuations across transactions.")
print("- Focus on high-performing products can boost revenue.\n")

print("✅ Sales Data Analysis completed successfully!")
print("🚀 Check the 'visualizations' folder for charts.")
