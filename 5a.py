import matplotlib.pyplot as plt
# Sample data
data = [10, 15, 10, 20, 25, 30, 25, 30, 30, 35, 40, 45, 45, 45, 50]
# Create a histogram plot
plt.hist(data, bins=5, color='blue', edgecolor='black')
# Add labels and title
plt.xlabel('Value Bins')
plt.ylabel('Frequency')
plt.title('Histogram Plot Example')
# Show the plot
plt.grid(True)
plt.show()
