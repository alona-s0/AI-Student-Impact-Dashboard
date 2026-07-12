from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

df = pd.read_csv("ai_student_impact_dataset.csv")

app = Dash()

app.layout = [
    html.Div(children='AI impact on students'),
    html.Hr(),
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[{"field": i} for i in df.columns]
    ),
    dcc.RadioItems(options=['Humanities', 'Medical', 'Business', 'STEM', 'Arts'], value='Humanities', id='majors-radio-item'),
    dcc.Graph(figure={}, id='scatter-graph1')

]

@callback(
    Output(component_id='scatter-graph1', component_property='figure'),
    Input(component_id='majors-radio-item', component_property='value')
)

def update_graph(major):
    if major == "All":
        filtered_df = df
    else:
        filtered_df = df[df["Major_Category"]==major]

    scatter_fig1 = px.scatter(filtered_df, x='Post_Semester_GPA', y='Weekly_GenAI_Hours')
    return scatter_fig1

if __name__ == '__main__':
    app.run(debug=True)