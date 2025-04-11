import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\mdasa\Downloads\Hospital_Bed_Occupancy (3).csv")

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
