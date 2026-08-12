import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data_clean.csv")

print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())

region_sales = df.groupby("Region")["Total Sales"].sum().sort_values(ascending=False)
print(region_sales)

plt.figure(figsize=(8,5))
sns.barplot(x=region_sales.index, y=region_sales.values)
plt.title("Total Sales by Region")
plt.ylabel("Total Sales")
plt.xlabel("Region")
plt.savefig("region_sales.png")
plt.show()

# ============ PRODUCT-WISE ANALYSIS ============
product_sales = df.groupby("Products")["Total Sales"].sum().sort_values(ascending=False)
print(product_sales)

plt.figure(figsize=(8,5))
sns.barplot(x=product_sales.index, y=product_sales.values)
plt.title("Total Sales by Product")
plt.ylabel("Total Sales")
plt.xlabel("Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("product_sales.png")
plt.show()

# ============ MONTHLY TREND ============
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month_name()
df["Month_Num"] = df["Date"].dt.month

monthly_sales = df.groupby(["Month_Num", "Month"])["Total Sales"].sum().reset_index().sort_values("Month_Num")
print(monthly_sales)

plt.figure(figsize=(10,5))
sns.lineplot(x=monthly_sales["Month"], y=monthly_sales["Total Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.ylabel("Total Sales")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_trend.png")
plt.show()

# ============ CORRELATION: Units Sold vs Unit Price ============
correlation = df["Units Sold"].corr(df["Unit Price"])
print(f"\nCorrelation between Units Sold and Unit Price: {correlation:.3f}")

plt.figure(figsize=(7,5))
sns.scatterplot(data=df, x="Unit Price", y="Units Sold", hue="Region")
plt.title("Units Sold vs Unit Price")
plt.tight_layout()
plt.savefig("price_vs_units.png")
plt.show()

# ============ CUSTOMER TYPE BREAKDOWN ============
customer_sales = df.groupby("Customer Type")["Total Sales"].sum().sort_values(ascending=False)
print(customer_sales)

plt.figure(figsize=(6,6))
plt.pie(customer_sales.values, labels=customer_sales.index, autopct='%1.1f%%')
plt.title("Sales Share by Customer Type")
plt.tight_layout()
plt.savefig("customer_type_share.png")
plt.show()