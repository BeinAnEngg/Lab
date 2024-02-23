import seaborn as sns
import matplotlib.pyplot as plt
# Load a built-in dataset from Seaborn
tips = sns.load_dataset("tips")
# Set Seaborn style and color palette
sns.set(style="whitegrid", palette="Set1")
# Create a customized scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="time", style="sex", 
s=100, palette="Set2")
plt.title("Customized Scatter Plot")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.legend(title="Time of Day")
plt.show()
# Create a customized histogram
plt.figure(figsize=(8, 6))
sns.histplot(tips["total_bill"], bins=20, kde=True, color="skyblue", 
line_kws={"color": "red"})
plt.title("Customized Histogram")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
# Create a customized box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x="day", y="total_bill", data=tips, palette="husl")
plt.title("Customized Box Plot")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()
