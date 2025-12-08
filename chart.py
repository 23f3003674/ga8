import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Synthetic Data Generation
np.random.seed(42)

segments = ["Budget", "Regular", "Premium", "VIP"]
data = {
    "Customer_Segment": np.repeat(segments, 200),
    "Purchase_Amount": np.concatenate([
        np.random.normal(50, 10, 200),   # Budget
        np.random.normal(120, 25, 200),  # Regular
        np.random.normal(250, 40, 200),  # Premium
        np.random.normal(500, 80, 200)   # VIP
    ])
}

df = pd.DataFrame(data)

# Create 512x512 figure (8x8 inches @ 64 dpi)
plt.figure(figsize=(8, 8))

# Boxplot
sns.boxplot(
    data=df,
    x="Customer_Segment",
    y="Purchase_Amount",
    palette="Set2"
)

# Titles and labels
plt.title("Purchase Amount Distribution by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Purchase Amount ($)")

# Save with required output
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
