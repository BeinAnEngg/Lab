import matplotlib.pyplot as plt
# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 50, 75, 100]
# Create a bar plot
plt.bar(categories, values, color='blue')
# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')
# Show the plot
plt.show()
