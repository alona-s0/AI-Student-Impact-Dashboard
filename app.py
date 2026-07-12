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

    dcc.RadioItems(options=['Weekly_GenAI_Hours', 'Traditional_Study_Hours', 'Anxiety_Level_During_Exams'], value='Weekly_GenAI_Hours', id='general-info-radio-item'),
    dcc.Graph(figure={}, id='histogram-graph1'),
    html.Hr(),

    dcc.RadioItems(options=['Humanities', 'Medical', 'Business', 'STEM', 'Arts'], value='Humanities', inline=True, id='majors-radio-item'),
    dcc.Graph(figure={}, id='scatter-graph1'),
    html.Hr(),

    dcc.Dropdown(options=['All', 'Humanities', 'Medical', 'Business', 'STEM', 'Arts'], value='All', id='majors-dropdown'),
    dcc.Graph(figure={}, id='heatmap-graph1'),
    dcc.Graph(figure={}, id='heatmap-graph2'),
    html.Hr(),

    dcc.Dropdown(options=['All', 'Humanities', 'Medical', 'Business', 'STEM', 'Arts'], value='All', id='majors-dropdown2'),
    dcc.Graph(figure={}, id='box-graph1'),
    dcc.Graph(figure={}, id='box-graph2')
]

@callback(
    Output(component_id='histogram-graph1', component_property='figure'),
    Output(component_id='scatter-graph1', component_property='figure'),
    Output(component_id='heatmap-graph1', component_property='figure'),
    Output(component_id='heatmap-graph2', component_property='figure'),
    Output(component_id='box-graph1', component_property='figure'),
    Output(component_id='box-graph2', component_property='figure'),
    Input(component_id='general-info-radio-item', component_property='value'),
    Input(component_id='majors-radio-item', component_property='value'),
    Input(component_id='majors-dropdown', component_property='value'),
    Input(component_id='majors-dropdown2', component_property='value')
)

def update_graph(col_chosen, radio_major, dropdown_major, dropdown_major2):
    hist_fig1 = px.histogram(df, x='Major_Category', y=col_chosen, histfunc='avg')

    if radio_major == "All":
        filtered_df = df
    else:
        filtered_df = df[df["Major_Category"]==radio_major]

    scatter_fig1 = px.scatter(filtered_df, x='Post_Semester_GPA', y='Weekly_GenAI_Hours')

    if dropdown_major == "All":
        filtered_df_heatmap = df
    else:
        filtered_df_heatmap= df[df["Major_Category"]==dropdown_major]

    heatmap_fig1 = px.density_heatmap(filtered_df_heatmap, x='Skill_Retention_Score', y='Weekly_GenAI_Hours')

    heatmap_fig2 = px.density_heatmap(filtered_df_heatmap, x='Perceived_AI_Dependency', y='Weekly_GenAI_Hours')

    if dropdown_major2 == "All":
        filtered_df_box = df
    else:
        filtered_df_box = df[df["Major_Category"]==dropdown_major2]

    box_fig1 = px.box(filtered_df_box, x='Anxiety_Level_During_Exams', y='Weekly_GenAI_Hours', points ='outliers')
    box_fig2 = px.box(filtered_df_box, x='Anxiety_Level_During_Exams', y='Traditional_Study_Hours', points ='outliers')
    
    return hist_fig1, scatter_fig1, heatmap_fig1, heatmap_fig2, box_fig1, box_fig2

if __name__ == '__main__':
    app.run(debug=True)