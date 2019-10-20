import plotly.express as px
import dash
import dash_auth
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

tips = px.data.tips()
col_options = [dict(label=x, value=x) for x in tips.columns]
dimensions = ["x", "y", "color", "facet_col", "facet_row"]


USERNAME_PASSWORD_PAIRS = [
['JamesBond', '007'],['LouisArmstrong', 'satchmo']
]

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
server = app.server

app.layout = html.Div(
    [
        dcc.Markdown('''

            # Plotly Dash

            ## It won't get easier to create beautiful dashboards

            >My name is Maxi and I created this dashboard to visualize how easy it is
            to create dashboards using `dash`. If you have any questions feel free
            to contact me.

            >@ github: [maximusKarlson](www.github.com/maximusKarlson)


            '''),

        html.H3("Explore the dataset on your own"),

        dcc.Markdown('''Simply use the dropdowns on the left to choose which variables you want to
        visualize and compare to each other.'''),

        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "25%", "float": "left"},
        ),
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"}),

        html.H3('Do females get a higher tip on average?'),
        dcc.Markdown('The colors indicate the party size.'),
        dcc.Graph(
            id='graph2', style={'width':'100%'},
            figure = px.scatter(
                tips,
                x="total_bill",
                y="tip",
                color="size",
                facet_col="sex",
                color_continuous_scale = px.colors.sequential.Viridis)),

        html.H3('Easy animated data? No problem!'),
        dcc.Markdown('''
                To create a plot that visualizes how the tips develop
                during the different days the follwing code is sufficient:

                ```python
                dcc.Graph(
                    id = 'animated-graph', style = {'width':'100%'},
                    figure = px.scatter(
                        tips,
                        x = 'total_bill', ## x-axis
                        y = 'tip', ## y-axis
                        color = 'sex', ## sex of the waiter coded as color
                        size = 'size', ## variable size of the data points depending on the size of the group
                        animation_frame = 'day'
                    )
                ```

                The parameter `animation_frame` is enough to create the animated
                `day` axis.


        '''),
        dcc.Graph(
            id = 'animated-graph', style = {'width':'100%'},
            figure = px.scatter(
                tips,
                x = 'total_bill',
                y = 'tip',
                color = 'sex',
                size = 'size',
                animation_frame = 'day'
            )
        ),

        html.H3('Do the tips corelate with the time of the event?'),
        dcc.Graph(
            id = 'graph3', style = {'width':'100%'},
            figure = px.scatter(
                tips,
                x="total_bill",
                y="tip",
                facet_row="time",
                facet_col="day",
                color="smoker",
                trendline="ols",
                category_orders={"day": ["Thur", "Fri", "Sat", "Sun"],
                                "time": ["Lunch", "Dinner"]})
        ),

        html.H3('Wanna see a fancy way to plot every data point? Here you go:'),
        dcc.Graph(
            id='graph4', style={'width':'100%', 'display':'inline-block'},
            figure = px.parallel_categories(
                tips,
                color="size",
                color_continuous_scale=px.colors.sequential.Inferno)
        ),

        html.H3('Last but not least - a sexy violin plot:'),
        dcc.Markdown('Smoking does not seem to have an impact on the tipping behavior.'),
        dcc.Graph(
            id='graph5', style={'width':'100%'},
            figure = px.violin(
                tips,
                y="tip",
                x="smoker",
                color="sex",
                box=True,
                points="all",
                hover_data=tips.columns)
        )
    ]
)


@app.callback(Output("graph", "figure"), [Input(d, "value") for d in dimensions])
def make_figure(x, y, color, facet_col, facet_row):
    return px.scatter(
        tips,
        x=x,
        y=y,
        color=color,
        facet_col=facet_col,
        facet_row=facet_row,
        height=700,
    )

if __name__ == '__main__':
    app.run_server()
