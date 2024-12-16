import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the dataset
df = pd.read_csv('metadata.csv')  # Make sure to use the correct path if necessary

# Display the first few rows to understand the structure of the data
print(df.head())

# Remove rows with missing values in the key columns
df = df.dropna(subset=['Battery_impedance', 'Re', 'Rct', 'Cycle'])

# Create subplots for Battery Impedance, Re, and Rct
fig = make_subplots(rows=3, cols=1, shared_xaxes=True,
                    subplot_titles=("Battery Impedance vs Cycle", "Re (Electrolyte Resistance) vs Cycle", "Rct (Charge Transfer Resistance) vs Cycle"))

# Plot Battery Impedance vs Cycle
fig.add_trace(go.Scatter(x=df['Cycle'], y=df['Battery_impedance'], mode='lines', name='Battery Impedance'),
              row=1, col=1)

# Plot Re (Electrolyte Resistance) vs Cycle
fig.add_trace(go.Scatter(x=df['Cycle'], y=df['Re'], mode='lines', name='Re (Electrolyte Resistance)'),
              row=2, col=1)

# Plot Rct (Charge Transfer Resistance) vs Cycle
fig.add_trace(go.Scatter(x=df['Cycle'], y=df['Rct'], mode='lines', name='Rct (Charge Transfer Resistance)'),
              row=3, col=1)

# Update layout with titles and axis labels
fig.update_layout(title="Battery Parameters vs Cycle",
                  xaxis_title="Cycle",
                  yaxis_title="Value",
                  showlegend=True)

# Show the plot
fig.show()
