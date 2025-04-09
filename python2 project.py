import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\mdasa\Downloads\Hospital_Bed_Occupancy (3).csv")
# Convert Date to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# 1. State-Wise Bed Occupancy Analysis
state_occupancy = df.groupby("State")["Occupied Beds"].mean().sort_values(ascending=False)
plt.figure(figsize=(10,5))
sns.barplot(x=state_occupancy.index, y=state_occupancy.values, palette="Blues")
plt.xticks(rotation=45)
plt.title("Average Hospital Bed Occupancy by State")
plt.xlabel("State")
plt.ylabel("Average Occupied Beds")
plt.show()
