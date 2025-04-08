import pandas as pd

# Replace 'your_file.csv' with the actual filename
df = pd.read_csv("data/raw/FW_Veg_Rem_Combined.csv")

# Display the first few rows
print(df.head())

# Count missing values in each column
print(df.isnull().sum())


# General info about the dataset (column types, null counts, etc.)
print(df.info())

# Summary statistics (helps spot inconsistencies)
print(df.describe())


