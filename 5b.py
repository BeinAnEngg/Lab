import matplotlib.pyplot as plt
# Sample data
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [30, 45, 15, 10]
colors = ['lightblue', 'lightcoral', 'lightgreen', 'lightsalmon']
explode = (0.1, 0, 0, 0) # Explode the first slice (Category A)
# Create a pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, 
autopct='%1.1f%%', shadow=True, startangle=140)
# Add a title
plt.title('Pie Chart Example')
# Show the plot
plt.show()
