import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Output, Input, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Div([
        dcc.Input(id='city-state', type='text', value='Montreal'),
        dcc.Input(id='country-state', type='text', value='Canada'),
        html.Button(id='submit-button', n_clicks=0, children='Submit')
    ], style={'display': 'inline'}),

    html.Div(id='text-output')

])


@app.callback(
    Output('text-output', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('city-state', 'value'),
     State('country-state', 'value')]
)
def city_country_text(n_clicks, city, country):
    return  u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
        and Input 2 is "{}"
    '''.format(n_clicks, city, country)


if __name__ == '__main__':
    app.run_server(dev_tools_hot_reload=False, debug=True)