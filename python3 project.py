import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\mdasa\Downloads\Hospital_Bed_Occupancy (3).csv")
# 3. ICU & COVID Bed Usage Trends
plt.figure(figsize=(10,5))
df[["ICU Beds", "COVID Cases"]].mean().plot(kind='bar', color=["red", "green"])
plt.title("Average ICU & COVID Bed Occupancy")
plt.xlabel("Category")
plt.ylabel("Average Beds Occupied")
plt.show()
