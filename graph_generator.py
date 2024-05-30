import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as p
import ast
import plotly.io as pio
import statistics
import sys


# Function to convert a string representation of an array to a numpy array
def str_to_array(arr_str):
    return np.array(ast.literal_eval(arr_str))
# Function to compute the mean of a numpy array
def mean_array(arr):
    return np.mean(arr)

def calculate_std(values):
    return round(np.std(values),2)

func_name = sys.argv[1]

# Read the CSV file into a DataFrame & transpose it
df_to_transpose = p.read_csv(func_name +'.csv')
df = df_to_transpose.set_index(func_name).transpose().reset_index()
df.rename(columns={'index': func_name}, inplace=True)
df = df.drop(df.columns[0], axis=1)

# Convert each cell from a string representation of an array to a numpy array
df = df.applymap(str_to_array)
# Apply the mean_array function to each cell in the DataFrame
df_mean = df.applymap(mean_array)
# Std deviation
df_standard_deviation = df.applymap(calculate_std)

print(df_standard_deviation)
# Plotting Joule
labels = ['Scenario 1', 'Scenario 2', 'Scenario 3', 'Scenario 4', 'Scenario 5']
joule_builtin = df_mean.loc[0].to_numpy() # joule builtin row
joule_custom = df_mean.loc[1].to_numpy() # joule custom row

fig = go.Figure()
#fig = make_subplots(rows=1, cols=1)

fig.add_trace(go.Bar(x=labels, y=joule_builtin, name='Built-in Function Energy consumption', marker_color='skyblue'))
fig.add_trace(go.Bar(x=labels, y=joule_custom, name='Custom Function Energy consumption', marker_color='lightcoral'))


fig.update_layout(
    title='Mean Energy Consumption by Scenario For function ' + func_name + ' in Joule',
    showlegend=True,
    annotations=[
        dict(text="Builtin std dev: " + str(df_standard_deviation.iloc[0,0]) + " | Custom std dev: " + str(df_standard_deviation.iloc[1,0]), x=0, y=1.1, showarrow=False, xref="paper", yref="paper"),
        dict(text="Builtin std dev: " + str(df_standard_deviation.iloc[0,1]) + " | Custom std dev: " + str(df_standard_deviation.iloc[1,1]), x=0.775, y=1.1, showarrow=False, xref="paper", yref="paper")
    ]
)

fig.update_yaxes(title_text='Mean Joule Consumption')
#fig.update_yaxes(title_text='Mean CPU Consumption', row=1, col=2)

fig.show()
pio.write_html(fig, file='plot_'+func_name+'.html', auto_open=True)
