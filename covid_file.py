import pandas as pd

# Load the main dataset
df = pd.read_csv("C:/Users/mwang/Downloads/covid_19_clean_complete.csv")

# Preview the first few rows
print(df.head())

import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/mwang/Downloads/covid_19_clean_complete.csv")

# Display basic information
print(df.info())  # Check column names and data types
print(df.head())  # View the first few rows

print(df.columns)


print(df.describe())  # Get key metrics like min, max, mean

print("Total Confirmed Cases:", df["Confirmed"].sum())
print("Total Deaths:", df["Deaths"].sum())
print("Total Recovered:", df["Recovered"].sum())


df_grouped = df.groupby("Date").sum()
print(df_grouped[["Confirmed", "Deaths", "Recovered"]].head())


