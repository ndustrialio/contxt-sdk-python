import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
import plotly
from dash.dependencies import Input, Output

from contxt.utils import get_environ_var, make_logger

logger = make_logger(__name__)

# Mute flask logger
# flask_logger = make_logger('werkzeug')
# flask_logger.setLevel(logging.ERROR)

# Flask
server = flask.Flask(__name__)

# Dash
app = dash.Dash(__name__, server=server)
app.scripts.config.serve_locally = False
dcc._js_dist[0][
    'external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

# Authorize plotly
# TODO: this might not even be needed
PLOTLY_USERNAME = get_environ_var('PLOTLY_USERNAME')
PLOTLY_API_KEY = get_environ_var('PLOTLY_API_KEY')
plotly.tools.set_credentials_file(
    username=PLOTLY_USERNAME, api_key=PLOTLY_API_KEY)

# Html
app.layout = html.Div([
    html.H1('Contxt'),
    dcc.Dropdown(id='my-dropdown', options=[], value=''),
    dcc.Graph(id='my-graph')
], className="container")


# TODO: may want to change the title_to_df arg to be more object-oriented as
# opposed to a simple dict
def run_plotly(title_to_df, x_label, y_label):
    # HACK: dont like to use globals, but seems necessary here since
    # update_graph needs access to the datasets
    global label_to_df, app

    # Rename dataframes to generic x, y
    label_to_df = {
        k: v.rename(index=str, columns={
            x_label: 'x',
            y_label: 'y'
        })
        for k, v in title_to_df.items()
    }

    # Sort
    label_to_df = {
        k: v.sort_values('x')
        for k, v in label_to_df.items() if not v.empty
    }

    # Update dropdown with all options
    options = [{'label': k, 'value': k} for k in label_to_df.keys()]
    value = options[0]['value'] if options else ''
    app.layout = html.Div([
        html.H1('Contxt'),
        dcc.Dropdown(id='my-dropdown', options=options, value=value),
        dcc.Graph(id='my-graph')
    ], className="container")

    # Run dash
    app.run_server()


def define_graph(x, y, title, x_label=None, y_label=None):
    return {
        'data': [{
            'x': x,
            'y': y,
            'line': {
                'width': 3,
                'shape': 'spline'
            }
        }],
        'layout': {
            'title': title,
            'xaxis': {
                'title': x_label or ''
            },
            'yaxis': {
                'title': y_label or ''
            },
            'margin': {
                'l': 80,
                'r': 80,
                'b': 80,
                't': 80
            }
        }
    }


@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = label_to_df.get(selected_dropdown_value)
    if df.empty:
        return define_graph([], [], title=selected_dropdown_value)
    return define_graph(df.x, df.y, title=selected_dropdown_value)


if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/'
                     'c78bf172206ce24f77d6363a2d754b59/raw/'
                     'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
                     'usa-agricultural-exports-2011.csv')
    run_plotly({'test': df}, 'beef', 'pork')
