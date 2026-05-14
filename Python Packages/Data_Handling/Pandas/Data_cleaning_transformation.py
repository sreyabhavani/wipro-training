import pandas as pd

raw_data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard',
                'Laptop', 'Mouse', None],

    'Revenue': [1200, 25, 300, 75, 1150, None, 150],

    'Cost': [800, 10, 200, 40, 850, 15, 100],

    'Date': ['2025-01-10', '2025-02-15', '2025-03-20',
             '2025-10-05', '2025-11-12',
             '2025-12-25', '2025-06-01']
}

df = pd.DataFrame(raw_data)

print("\n\nOriginal DataFrame:\n")
print(df)

# 1. Handle missing values
median_revenue = df['Revenue'].median()
df['Revenue'].fillna(median_revenue, inplace=True)

df['Product'].fillna("Unknown", inplace=True)

print("\nDataFrame After Handling Missing Values:\n")
print(df)

# 2. Feature Engineering
df['Profit'] = df['Revenue'] - df['Cost']

df['Margin_Percentage'] = (df['Profit'] / df['Revenue']) * 100

print("\nDataFrame After Feature Engineering:\n")
print(df)

# 3. Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filter Q4 months (October, November, December)
q4_df = df[
    (df['Date'].dt.month.isin([10, 11, 12])) &
    (df['Profit'] > 50)
]

print("\nFiltered Q4 Data (Profit > 50):\n")
print(q4_df)
