import pandas as pd
import matplotlib.pyplot as plt

# ✅ Step 1: Load local CSV file
df = pd.read_csv(
    "/Users/joseph/Downloads/Websites/python/dataproject/nasa-data-project/Meteorite_Landings.csv"
)


# ✅ Step 2: Clean and prepare the data
df = df.dropna(subset=["mass (g)", "year"])
df["mass (g)"] = pd.to_numeric(df["mass (g)"], errors="coerce")
df["year"] = pd.to_numeric(df["year"], errors="coerce")
df = df[df["year"] > 1900]

# ✅ Step 3: Create a count plot (how many fell each year)
count_per_year = df.groupby("year")["name"].count()

plt.figure(figsize=(12, 6))
count_per_year.plot()
plt.title("Meteorites Found Per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()

# ✅ Step 4: Save the plot as PDF
plt.savefig("meteorites_per_year.pdf")

# ✅ Step 5: Show the plot
plt.show()

# ✅ Step 6: Save the raw count data to CSV
count_per_year.to_csv("meteorite_counts_by_year.csv", header=True)
