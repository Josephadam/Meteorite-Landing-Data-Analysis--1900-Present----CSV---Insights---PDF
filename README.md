
<body>

  <h1>📊 Meteorite Landing Data Analysis (1900–Present)</h1>

  <p>This project performs a data analysis on meteorite landings using a local CSV file sourced from NASA. It utilizes Python libraries such as <code>pandas</code> and <code>matplotlib</code> to clean, process, and visualize meteorite landing data by year.</p>

  <h2>🔧 What This Project Does</h2>
  <ul>
    <li>Loads a local CSV file of meteorite landings.</li>
    <li>Cleans the data by dropping rows with missing mass or year values.</li>
    <li>Filters out records prior to the year 1900.</li>
    <li>Groups meteorite landings by year to count how many were found annually.</li>
    <li>Visualizes this information in a line chart.</li>
    <li>Exports the results to a PDF and a new CSV file.</li>
  </ul>

  <h2>📁 Files Generated</h2>
  <ul>
    <li><code>meteorites_per_year.pdf</code> - A line chart showing how many meteorites were found each year.</li>
    <li><code>meteorite_counts_by_year.csv</code> - A CSV with the count of meteorites by year.</li>
  </ul>

  <h2>📌 Example Python Code</h2>
  <pre><code>import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Meteorite_Landings.csv")
df = df.dropna(subset=["mass (g)", "year"])
df["mass (g)"] = pd.to_numeric(df["mass (g)"], errors="coerce")
df["year"] = pd.to_numeric(df["year"], errors="coerce")
df = df[df["year"] > 1900]

count_per_year = df.groupby("year")["name"].count()
count_per_year.plot()
plt.title("Meteorites Found Per Year")
plt.savefig("meteorites_per_year.pdf")
count_per_year.to_csv("meteorite_counts_by_year.csv")</code></pre>

  <h2>🚀 How to Run</h2>
  <ol>
    <li>Make sure you have Python 3 installed.</li>
    <li>Install required libraries:
      <pre><code>pip install pandas matplotlib</code></pre>
    </li>
    <li>Place the <code>Meteorite_Landings.csv</code> file in your working directory.</li>
    <li>Run the script:
      <pre><code>python your_script_name.py</code></pre>
    </li>
  </ol>

  <h2>📚 Data Source</h2>
  <p>NASA Meteorite Landings data set. You can find the original dataset <a href="https://data.nasa.gov">on NASA's open data portal</a>.</p>

  <p>Feel free to contribute or fork the project for your own use!</p>

</body>
</html>
