Battery Aging Analysis with Plotly
This project analyzes the NASA Battery Dataset to visualize the change in battery parameters (Battery Impedance, Electrolyte Resistance (Re), and Charge Transfer Resistance (Rct)) as a battery ages through repeated charge/discharge cycles. The dataset contains data from Li-ion batteries subjected to various operational profiles and temperatures, and impedance measurements were made via Electrochemical Impedance Spectroscopy (EIS) to study battery aging.

Project Description
As batteries go through charge/discharge cycles, their internal parameters change, which can be observed through impedance measurements. This project uses the metadata.csv file to create interactive plots with Plotly that demonstrate how the following parameters evolve over cycles:

Battery Impedance: Represents the overall resistance of the battery to current flow.
Re (Electrolyte Resistance): Represents the resistance of the electrolyte inside the battery.
Rct (Charge Transfer Resistance): Represents the resistance related to the movement of ions at the electrode interface.
These parameters are plotted against the cycle number to observe how the battery’s internal conditions change as it ages.

Requirements
Before running the code, make sure you have the following Python libraries installed:

pandas: For data manipulation and handling.
plotly: For creating interactive visualizations.
You can install these libraries via pip:

bash
Copy code
pip install pandas plotly
Dataset
The dataset used in this project is metadata.csv, which contains various battery parameters measured during charge/discharge cycles. The relevant columns used in this project are:

Battery_impedance: Battery impedance at each cycle.
Re: Electrolyte resistance at each cycle.
Rct: Charge transfer resistance at each cycle.
Cycle: The number of cycles the battery has undergone.
Code Overview
1. Data Loading:
The code loads the metadata.csv file using Pandas' read_csv() function to create a DataFrame.

2. Data Preprocessing:
The script removes rows containing missing values in the relevant columns (Battery_impedance, Re, Rct, Cycle).

3. Plotting with Plotly:
Subplots: The code creates three subplots to visualize each of the parameters: Battery_impedance, Re, and Rct against the cycle number.
Interactive Line Plots: The data for each parameter is plotted using Plotly's go.Scatter() method.
Layout: The layout is updated to include titles for each subplot, axis labels, and a main title for the entire figure.
4. Display:
The interactive plot is displayed using fig.show(), which allows zooming, hovering, and data inspection.

Usage
Download the metadata.csv file from the dataset provided.
Place the metadata.csv file in the same directory as the Python script or update the file path in the script.
Run the Python script. It will load the dataset, preprocess the data, and generate interactive plots showing how the battery parameters change over cycles.
bash
Copy code
python battery_analysis.py
Example Output
The script will generate an interactive Plotly figure with three subplots:

Battery Impedance vs Cycle
Re (Electrolyte Resistance) vs Cycle
Rct (Charge Transfer Resistance) vs Cycle
Each plot will show how the respective parameter evolves as the battery undergoes repeated charge/discharge cycles, allowing you to observe the aging process.
