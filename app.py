from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

df = pd.read_csv("ai_student_impact_dataset.csv")

app = Dash()

app.layout = [
    html.Div(children='AI impact on students'),
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[{"field": i} for i in df.columns]
    )
    ]

if __name__ == '__main__':
    app.run(debug=True)