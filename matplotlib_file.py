import matplotlib.pyplot as plt

import pandas as pd

# Data for df_grouped
data = {
	"Date": ["2023-01-01", "2023-01-02", "2023-01-03"],
	"Confirmed": [100, 150, 200],
	"Deaths": [5, 7, 10],
	"Recovered": [50, 80, 120]
}
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
df_grouped = df.set_index("Date")

plt.figure(figsize=(10,5))
plt.plot(df_grouped.index, df_grouped["Confirmed"], label="Confirmed Cases", color="blue")
plt.plot(df_grouped.index, df_grouped["Deaths"], label="Deaths", color="red")
plt.plot(df_grouped.index, df_grouped["Recovered"], label="Recovered", color="green")
plt.xlabel("Date")
plt.ylabel("Count")
plt.title("Global COVID-19 Cases Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/mwang/Downloads/covid_19_clean_complete.csv")

# Convert 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Group by date to sum recovered cases globally
df_grouped = df.groupby("Date").sum()

# Plot recovered cases over time
plt.figure(figsize=(10,5))
plt.plot(df_grouped.index, df_grouped["Recovered"], label="Recovered Patients", color="green")
plt.xlabel("Date")
plt.ylabel("Number of Recovered Patients")
plt.title("Global COVID-19 Recoveries Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/mwang/Downloads/covid_19_clean_complete.csv")

# Convert 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Group by date to sum confirmed cases globally
df_grouped = df.groupby("Date").sum()

# Plot confirmed cases over time
plt.figure(figsize=(10,5))
plt.plot(df_grouped.index, df_grouped["Confirmed"], label="Confirmed Cases", color="blue")
plt.xlabel("Date")
plt.ylabel("Number of Confirmed Cases")
plt.title("Global COVID-19 Confirmed Cases Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)

# Show the plot
plt.show()


import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/mwang/Downloads/covid_19_clean_complete.csv")

# Convert 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Group by date to sum deaths globally
df_grouped = df.groupby("Date").sum()

# Plot death cases over time
plt.figure(figsize=(10,5))
plt.plot(df_grouped.index, df_grouped["Deaths"], label="Deaths", color="red")
plt.xlabel("Date")
plt.ylabel("Number of Deaths")
plt.title("Global COVID-19 Deaths Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)

# Show the plot
plt.show()