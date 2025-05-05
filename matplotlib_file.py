import matplotlib.pyplot as plt

import pandas as pd

# Example data for df_grouped
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