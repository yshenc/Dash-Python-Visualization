import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': ['Montreal', 'Toronto', 'Ottawa']
}

app.layout = html.Div([

    dcc.RadioItems(
        id='country-select',
        options=[{'label': i, 'value': i} for i in all_options.keys()],
        value='America'
    ),

    html.Hr(),

    dcc.RadioItems(id='city-select'),

    html.Hr(),

    html.Div(children=[], id='text-output')
])


@app.callback(
    Output('city-select', 'options'),
    [Input('country-select', 'value')]
)
def set_cities_options(country):
    return [{'label': i, 'value': i} for i in all_options[country]]



@app.callback(
    Output('city-select', 'value'),
    [Input('city-select', 'options')]
)
def set_cities_value(city_options):
    return city_options[0]['value']



@app.callback(
    Output('text-output', 'children'),
    [Input('city-select', 'value'),
     Input('country-select', 'value')]
)
def set_text(city_selected, country_selected):
    return u'{} is a city in {}'.format(
        city_selected, country_selected
    )


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=False)