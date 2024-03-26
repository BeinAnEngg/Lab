from bokeh.plotting import figure, show, output_file
from bokeh.layouts import gridplot
from math import pi
from numpy import cumsum

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

output_file("bokeh_plots.html")

p1 = figure(title="Line Plot", x_axis_label='X-axis', y_axis_label='Y-axis')
p1.line(x, y, line_color='blue', line_width=2)

p2 = figure(title="Scatter Plot", x_axis_label='X-axis', y_axis_label='Y-axis')
p2.circle(x, y, size=10, color='green', alpha=0.6)

categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [30, 45, 15, 10]

p3 = figure(x_range=categories, title="Bar Plot", x_axis_label='Categories', y_axis_label='Values')
p3.vbar(x=categories, top = values, width=0.5, color='orange')

angles = [i * 2 * pi / sum(values) for i in values]

p4 = figure(title="Pie Chart")
p4.wedge(x=0, y=0, radius=0.4, start_angle=cumsum([0] + angles[:-1]), end_angle=cumsum(angles), 
         line_color="white", fill_color=['red', 'green', 'blue', 'orange'], legend_label="Categories", )
layout = gridplot([[p1, p2], [p3, p4]])
show(layout)
