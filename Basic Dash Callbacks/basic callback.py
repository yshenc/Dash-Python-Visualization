import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Output, Input

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Div([
        dcc.Input(id='city', type='text', value='Montreal'),
        dcc.Input(id='country', type='text', value='Canada')
    ], style={'display': 'inline'}),

    html.Div(id='text-output')

])


@app.callback(
    Output('text-output', 'children'),
    [Input('city', 'value'),
     Input('country', 'value')]
)
def city_country_text(city, country):
    return 'Input 1 is \"' + city + '\" and Input 2 is \"' + country +'\"'


if __name__ == '__main__':
    app.run_server(dev_tools_hot_reload=False, debug=True)