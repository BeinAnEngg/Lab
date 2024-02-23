import plotly.graph_objects as go
import numpy as np
# Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
# Define a 3D function (e.g., a surface)
Z = np.sin(np.sqrt(X**2 + Y**2))
# Create a 3D surface plot using Plotly
fig = go.Figure(data=go.Surface(z=Z, x=x, y=y))
fig.update_layout(scene=dict(zaxis_title="Z-axis", yaxis_title="Y-axis", 
xaxis_title="X-axis"),
 title="3D Surface Plot")
# Show the plot
fig.show()
