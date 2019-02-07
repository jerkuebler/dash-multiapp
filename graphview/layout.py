import dash_html_components as html
import dash_core_components as dcc

pathname = '/graph/'


def get_layout(app):
    layout = html.Div([

        dcc.Graph(
            id='basic-graph',
            figure={
                'data': [
                    {
                        'x': [0, 1],
                        'y': [0, 1],
                        'type': 'line'
                    }
                ],
                'layout': {
                    'title': 'Basic Graph'
                }
            }
        ),

        html.Div([
            html.Button('Click me', id='btn'),
            html.Div(id='output')
        ])

    ])

    return layout
