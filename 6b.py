import matplotlib.pyplot as plt
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
# Create a linear plot with custom line formatting
plt.plot(x, y, marker='o', color='blue', linestyle='--', linewidth=2, 
markersize=8, label='Line Example')
# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Linear Plot with Line Formatting')
# Show a legend
plt.legend()
# Show the plot
plt.grid(True)
plt.show()
