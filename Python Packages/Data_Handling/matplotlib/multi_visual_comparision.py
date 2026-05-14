import matplotlib.pyplot as plt


cities=["Chennai","Mumbai","Delhi","Bangalore","Hyderabad"]
sales_values=[450,500,550,600,650]
categories=["Electronics","Fashion","Groceries","Home Decor"]
market_share=[35,25,30,15]

# Create a single figure with 1 row and 2 columns of subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 1. Subplot 1: Bar Chart (Cities vs Sales)
axes[0].bar(cities, sales_values, color='teal')
axes[0].set_title('Sales Value by City')
axes[0].set_xlabel('Cities')
axes[0].set_ylabel('Sales (in Units)')
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# 2. Subplot 2: Pie Chart (Market Share by Category)
explode_values = [0.1, 0, 0, 0]
axes[1].pie(
    market_share,
    labels=categories,
    explode=explode_values,
    autopct='%1.0f%%',
    startangle=140,
    colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
)
axes[1].set_title('Market Share Categories')

# 3. Add Main Figure Subtitle and adjust layout spacing
plt.suptitle("Regional Sales & Category Analysis", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()