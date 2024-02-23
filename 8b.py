from bokeh.plotting import figure, show, output_file
from math import pi
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
# Create a Bokeh figure
output_file("bokeh_plots.html")
# Create a line plot
p1 = figure(title="Line Plot", x_axis_label='X-axis', y_axis_label='Y-axis')
p1.line(x, y, line_color='blue', line_width=2)
# Create a scatter plot
p2 = figure(title="Scatter Plot", x_axis_label='X-axis', y_axis_label='Y-axis')
p2.circle(x, y, size=10, color='green', alpha=0.6)
# Sample data for bar plot
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [30, 45, 15, 10]
# Create a bar plot
p3 = figure(x_range=categories, title="Bar Plot", x_axis_label='Categories', 
y_axis_label='Values')
p3.vbar(x=categories, top=values, width=0.5, color='orange')
# Sample data for a pie chart
data = {'Categories': ['Category A', 'Category B', 'Category C', 'Category D'],
 'Values': [30, 45, 15, 10]}
angles = [pi/4, pi/2, pi, 1.5*pi]
# Create a pie chart
p4 = figure(title="Pie Chart")
p4.wedge(x=0, y=0, radius=0.4, start_angle=angles, end_angle=angles[1:] + 
[2*pi],
 line_color="white", fill_color=['red', 'green', 'blue', 'orange'], 
legend_label="Categories",
 source=data)
# Show the plots
show(p1)
show(p2)
show(p3)
show(p4)
