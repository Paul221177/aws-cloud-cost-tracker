import pandas as pd
import matplotlib.pyplot as plt

# Load AWS pricing dataset
df = pd.read_csv("data/aws_pricing_data.csv")

# Display dataset
print("\n=== AWS Pricing Dataset ===")
print(df.head())

# Average estimated cost by service
average_cost = df.groupby("Service")["Estimated_Cost"].mean()

print("\n=== Average Cost Per AWS Service ===")
print(average_cost)

# Highest cost service
highest_cost = df.loc[df["Estimated_Cost"].idxmax()]

print("\n=== Highest AWS Service Cost ===")
print(highest_cost)

# Category distribution
print("\n=== AWS Service Categories ===")
print(df["Category"].value_counts())

# Visualization
plt.figure(figsize=(10,6))

plt.bar(
    average_cost.index,
    average_cost.values
)

plt.xlabel("AWS Services")
plt.ylabel("Average Estimated Cost")
plt.title("Average AWS Service Cost Analysis")

plt.tight_layout()

# Save chart
plt.savefig("screenshots/aws_cost_chart.png")

print("\nChart saved successfully.")
