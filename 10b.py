import plotly.express as px
# Sample data
locations = ['New York', 'Los Angeles', 'Chicago', 'San Francisco']
latitudes = [40.7128, 34.0522, 41.8781, 37.7749]
longitudes = [-74.0060, -118.2437, -87.6298, -122.4194]
# Create a map
fig = px.scatter_geo(lat=latitudes, lon=longitudes, locationmode='USA-states', 
text=locations)
# Customize the map
fig.update_geos(
 projection_scale=10,
 center=dict(lon=-95, lat=38),
 visible=False,
 showcoastlines=True,
 coastlinecolor="RebeccaPurple",
 showland=True,
 landcolor="LightGreen",
 showocean=True,
 oceancolor="LightBlue",
 showlakes=True,
 lakecolor="LightBlue",
)
# Set map title
fig.update_layout(
 title_text='Sample US Map',
 title_x=0.5,
)
# Show the map
fig.show()
