import matplotlib.pyplot as plt
# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 15, 13, 17, 20, 22, 25, 30, 28, 35]
# Create a scatter plot
plt.scatter(x, y, color='blue', marker='o', label='Scatter Points', alpha=0.6)
# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
# Show the plot
plt.legend()
plt.grid(True)
plt.show()
