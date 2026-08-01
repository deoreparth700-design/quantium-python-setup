import pandas as pd
from dash import Dash, html, dcc
from plotly import express as px

# Load the processed data
df = pd.read_csv("formatted_output.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort data by date
df = df.sort_values("Date")

# Create the line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Sales"
    }
)

# Create the Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Soul Foods Pink Morsel Sales Visualiser",
        style={"textAlign": "center"}
    ),

    dcc.Graph(
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)