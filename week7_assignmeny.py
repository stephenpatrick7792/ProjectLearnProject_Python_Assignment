
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ----------------------------
# Task 1: Load and Explore the Dataset
# ----------------------------

try:
    # Load iris dataset
    iris = load_iris(as_frame=True)
    df = iris.frame  # pandas DataFrame
    df['species'] = df['target'].apply(lambda i: iris.target_names[i])

    print("First five rows of the dataset:")
    print(df.head(), "\n")

    # Check structure and missing values
    print("Dataset info:")
    print(df.info(), "\n")

    print("Missing values per column:")
    print(df.isnull().sum(), "\n")

    # Clean data (Iris has no missing values, but let’s include the logic)
    df = df.dropna()

except FileNotFoundError:
    print("Error: Dataset file not found. Please check the path.")
    exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    exit(1)

# ----------------------------
# Task 2: Basic Data Analysis
# ----------------------------

# Basic statistics
print("Basic statistics:")
print(df.describe(), "\n")

# Group by species and compute mean
grouped = df.groupby("species").mean()
print("Mean values grouped by species:")
print(grouped, "\n")

# Observations
print("Observations:")
print("- Iris setosa tends to have the smallest petal and sepal sizes.")
print("- Iris virginica generally has the largest petal lengths and widths.\n")

# ----------------------------
# Task 3: Data Visualization
# ----------------------------

sns.set_style("whitegrid")

# 1. Line chart (example: cumulative petal length over index for each species)
plt.figure(figsize=(8, 5))
for species, data in df.groupby("species"):
    plt.plot(data.index, data["petal length (cm)"].cumsum(), label=species)
plt.title("Cumulative Petal Length by Species")
plt.xlabel("Index")
plt.ylabel("Cumulative Petal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(6, 5))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal length)
plt.figure(figsize=(6, 5))
plt.hist(df["sepal length (cm)"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (sepal length vs. petal length, colored by species)
plt.figure(figsize=(7, 6))
sns.scatterplot(
    x="sepal length (cm)",
    y="petal length (cm)",
    hue="species",
    palette="Set1",
    data=df
)
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
