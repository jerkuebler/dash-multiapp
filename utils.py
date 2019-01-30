import dash
import base.layout
import dash_html_components as html


def create_dash_app(server, app):
    layout = getattr(__import__(app, fromlist=['layout']), 'layout')
    callbacks = getattr(__import__(app, fromlist=['callbacks']), 'callbacks')
    dash_app = dash.Dash(__name__, server=server, url_base_pathname=layout.pathname)

    dash_app.layout = html.Div([base.layout.navbar, layout.layout])
    callbacks.register_callbacks(dash_app)

    return dash_app
