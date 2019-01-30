import dash_html_components as html

navbar = html.Nav(className="navbar navbar-default", children=[
    html.A('Home', className="navbar-brand", href="/"),
    html.A('Data View', className="nav-link mr-auto", href="/data/"),
])
