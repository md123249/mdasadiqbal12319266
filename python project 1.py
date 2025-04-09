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
# 2. Seasonal Impact on Hospitalization
season_occupancy = df.groupby("Season")["Occupied Beds"].mean().sort_values()
plt.figure(figsize=(8,5))
sns.barplot(x=season_occupancy.index, y=season_occupancy.values, palette="coolwarm")
plt.title("Seasonal Hospital Bed Occupancy")
plt.xlabel("Season")
plt.ylabel("Average Occupied Beds")
plt.show()
# 3. ICU & COVID Bed Usage Trends
plt.figure(figsize=(10,5))
df[["ICU Beds", "COVID Cases"]].mean().plot(kind='bar', color=["red", "green"])
plt.title("Average ICU & COVID Bed Occupancy")
plt.xlabel("Category")
plt.ylabel("Average Beds Occupied")
plt.show()

# 4. Daily Occupancy Trends
df_daily = df.groupby("Date")["Occupied Beds"].mean()
plt.figure(figsize=(12,5))
sns.lineplot(x=df_daily.index, y=df_daily.values, color="blue")
plt.title("Daily Hospital Bed Occupancy Trend")
plt.xlabel("Date")
plt.ylabel("Average Occupied Beds")
plt.xticks(rotation=45)
plt.show()

print("Hospital bed occupancy analysis completed successfully!")
