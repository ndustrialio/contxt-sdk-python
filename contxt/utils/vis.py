import logging

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

from contxt.utils import make_logger

logger = make_logger(__name__)


class DataVisualizer:

    def __init__(self, name='Contxt', multi_plots=True, quiet=False):
        self.name = name
        self.multi_plots = multi_plots

        if quiet:
            flask_logger = make_logger('werkzeug')
            flask_logger.setLevel(logging.ERROR)

    def run(self, labeled_graphs, title=None, x_label=None, y_label=None):
        # Create dash app
        app = dash.Dash(__name__)

        # Update dropdown with options
        options = [dict(label=k, value=k) for k in labeled_graphs.keys()]
        value = options[0]['value'] if options else ''
        if self.multi_plots:
            value = [value]
        app.layout = self.get_app_layout(options, value)

        @app.callback(
            Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
        def update_graph(selected_labels):
            # Handle single graph obj
            if not isinstance(selected_labels, list):
                selected_labels = [selected_labels]

            # Create graph
            return self.get_figure(
                labeled_graphs={
                    t: labeled_graphs.get(t)
                    for t in selected_labels
                },
                title=title,
                x_label=x_label,
                y_label=y_label)

        # Run dash
        app.run_server()

    def get_app_layout(self, options, curr_value):
        return html.Div([
            html.H1(self.name),
            dcc.Dropdown(
                id='my-dropdown',
                options=options,
                value=curr_value,
                multi=self.multi_plots),
            dcc.Graph(id='my-graph')
        ], className="container")

    def get_figure(self,
                   labeled_graphs,
                   title=None,
                   x_label=None,
                   y_label=None):
        return go.Figure(
            data=list(labeled_graphs.values()),
            layout=self.get_figure_layout(
                title=title, x_label=x_label, y_label=y_label))

    def get_figure_layout(self, title, x_label=None, y_label=None):
        return go.Layout(
            title=title,
            xaxis=dict(title=x_label),
            yaxis=dict(title=y_label),
            showlegend=True,
            margin=go.layout.Margin(l=80, r=80, t=80, b=80))


if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/'
                     'c78bf172206ce24f77d6363a2d754b59/raw/'
                     'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
                     'usa-agricultural-exports-2011.csv')
    s = go.Scatter(
        x=df['beef'].sort_values(),
        y=df['pork'],
        name='pork vs beef',
        line=dict(shape='spline', width=3)
    )
    # DashApp.run_static({'test1': s, 'test2': s})
    DataVisualizer().run({'test1': s, 'test2': s})
