import plotly.graph_objects as go
import pandas as pd
# Sample time series data
data = {
 'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
 'Value': [10, 15, 12, 18, 22, 24, 30, 28, 35, 40, 45, 48, 52, 50, 60, 58, 65, 
70, 75, 80, 78, 85, 90, 95, 100, 95, 105, 110, 115, 120]
}
df = pd.DataFrame(data)
# Create a time series line plot
fig = go.Figure(data=go.Scatter(x=df['Date'], y=df['Value'], 
mode='lines+markers', name='Time Series'))
# Set axis labels and plot title
fig.update_layout(xaxis_title='Date', yaxis_title='Value', title='Time Series 
Plot')
# Show the plot
fig.show()
