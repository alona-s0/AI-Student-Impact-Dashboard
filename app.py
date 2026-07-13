from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

df = pd.read_csv("ai_student_impact_dataset.csv")

app = Dash()

app.layout = [
    html.H1('AI impact on students', style={'textAlign':'center'}),
    html.Hr(),
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[{"field": i} for i in df.columns]
    ),

    html.H2("Time spent on Gen AI per week by each major"),
    dcc.RadioItems(options=['Weekly_GenAI_Hours', 'Traditional_Study_Hours', 'Anxiety_Level_During_Exams'], value='Weekly_GenAI_Hours', inline=True, id='general-info-radio-item'),
    dcc.Graph(figure={}, id='general-info-histogram'),
    html.Hr(),

    html.H2("The impact of Gen AI on grades"),
    dcc.RadioItems(options=['Humanities', 'Medical', 'Business', 'STEM', 'Arts'], value='Humanities', inline=True, id='majors-radio-item'),
    dcc.Graph(figure={}, id='GPA_Scatter'),
    html.Hr(),

    html.H2("Exploring the effects of AI usage on learning metrics"), #for the last graph
    dcc.Dropdown(options=['All', 'Humanities', 'Medical', 'Business', 'STEM', 'Arts'], value='All', id='majors-dropdown'),
    dcc.Graph(figure={}, id='Skill_Retention_Heatmap'),
    dcc.Graph(figure={}, id='AI_Dependency_Heatmap'),
    html.Hr(),

    html.H2("Does AI affect stress levels during exams?"),
    dcc.Dropdown(options=['All', 'Humanities', 'Medical', 'Business', 'STEM', 'Arts'], value='All', id='majors-dropdown2'),
    dcc.Graph(figure={}, id='AI_Anxiety_Levels_Box'),
    dcc.Graph(figure={}, id='Trad_Anxiety_Levels_Box')
]

@callback(
    Output(component_id='general-info-histogram', component_property='figure'),
    Output(component_id='GPA_Scatter', component_property='figure'),
    Output(component_id='Skill_Retention_Heatmap', component_property='figure'),
    Output(component_id='AI_Dependency_Heatmap', component_property='figure'),
    Output(component_id='AI_Anxiety_Levels_Box', component_property='figure'),
    Output(component_id='Trad_Anxiety_Levels_Box', component_property='figure'),
    Input(component_id='general-info-radio-item', component_property='value'),
    Input(component_id='majors-radio-item', component_property='value'),
    Input(component_id='majors-dropdown', component_property='value'),
    Input(component_id='majors-dropdown2', component_property='value')
)

def update_graph(col_chosen, radio_major, dropdown_major, dropdown_major2):
    def filter_major(major):
        if major == "All":
            return df
        return df[df["Major_Category"]==major]
    
    major_histogram = px.histogram(df, x='Major_Category', y=col_chosen, histfunc='avg')

    filtered_df = filter_major(radio_major)
    gpa_scatter = px.scatter(filtered_df, x='Post_Semester_GPA', y='Weekly_GenAI_Hours')

    filtered_df_heatmap = filter_major(dropdown_major)
    skill_heatmap = px.density_heatmap(filtered_df_heatmap, x='Skill_Retention_Score', y='Weekly_GenAI_Hours')

    ai_heatmap = px.density_heatmap(filtered_df_heatmap, x='Perceived_AI_Dependency', y='Weekly_GenAI_Hours')

    filtered_df_box = filter_major(dropdown_major2)
    ai_anxiety_box = px.box(filtered_df_box, x='Anxiety_Level_During_Exams', y='Weekly_GenAI_Hours', points ='outliers')
    trad_anxiety_box = px.box(filtered_df_box, x='Anxiety_Level_During_Exams', y='Traditional_Study_Hours', points ='outliers')
    
    return major_histogram, gpa_scatter, skill_heatmap, ai_heatmap, ai_anxiety_box, trad_anxiety_box

if __name__ == '__main__':
    app.run(debug=True)