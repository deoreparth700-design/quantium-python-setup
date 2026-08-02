import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_output.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f9",
        "padding": "30px",
        "fontFamily": "Arial"
    },
    children=[

        html.H1(
            "📊 Soul Foods Pink Morsels Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "30px"
            }
        ),

        html.H3("Filter by Region"),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"marginBottom": "25px"}
        ),

        dcc.Graph(id="sales-chart")

    ]
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):

    if region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title="Pink Morsels Sales Over Time"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        xaxis_title="Date",
        yaxis_title="Sales ($)"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)