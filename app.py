from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_dark"

df = pd.read_csv("ai_student_impact_dataset.csv")

app = Dash()

app.layout = html.Div([
    html.H1('AI impact on students', style={'textAlign':'center', "marginTop":"-3%"}),
    
    html.Div([
        html.Div([
            html.H2("Weekly Gen AI usage by different majors", style={"textAlign":"center"}),
            html.Div([
                dcc.Dropdown(options=['Freshman', 'Sophomore', 'Junior', 'Senior', 'All'], 
                            value='Freshman', id="year-study-dropdown", style={"width":"30%", 
                                                                            "border": "0.5px solid white",
                                                                            "borderRadius":"3px",
                                                                            "marginRight":"5px"},
                            className="dark-dropdown",),
                dcc.Dropdown(options=[{"label": "Violin Plot", "value": "violin"},
                                        {"label": "Histogram", "value": "histogram"}],
                                        value='violin', id="graph-type-dropdown", style={"width":"30%", 
                                                                         "border": "0.5px solid white",
                                                                         "borderRadius":"3px"},
                            className="dark-dropdown",)],
                style={"display": "flex",
                        "alignItems": "center",
                        "marginBottom": "15px"}
            ),
            dcc.Graph(figure={}, id="Year_Of_Study_AI_Usage", style={"height":"450px"}),

            html.Hr(style={"marginTop":"5px"}),
            
            html.P("Compare weekly Gen AI usage across different majors. " \
            "Use filters to focus on a specific year of study or switch between distribution views.", 
            style={"color":"white", "marginTop":"10px"})],

            style={"width":"50%",
                   "height":"450px"},

        ),

        html.Div([
            html.H2("General information about the study program for each major", style={"textAlign":"center"}),
            dcc.RadioItems(options=['Traditional_Study_Hours', 'Anxiety_Level_During_Exams'], 
                           value='Traditional_Study_Hours', inline=True, id='general-info-radio-item', 
                           style={'marginLeft':'5%'}, labelStyle={"color": "white"}),
            dcc.Graph(figure={}, id='general-info-histogram', style={"height":"450px"}),

            html.Hr(style={"marginTop":"5px"}),
            
            html.P("Compare the average traditional study hours and exam anxiety levels across different majors. " \
            "Use the selector to switch between the metrics.", 
            style={"color":"white", "marginTop":"10px"})],

            style={"width":"50%",
                   "height":"450px",
                   "marginLeft":"2%"}
        )],
        style={ "display": "flex",
                "alignItems":"flex-start",
                "height":"600px"}
    ),

    html.H2("The impact of Gen AI on grades", style={"margin-top":"100px"}),
    dcc.RadioItems(options=['Humanities', 'Medical', 'Business', 'STEM', 'Arts'], 
                   value='Humanities', inline=True, id='majors-radio-item', labelStyle={"color": "white"}),
    dcc.Graph(figure={}, id='GPA_Scatter'),
    html.Hr(style={"marginTop":"5px"}),

    html.P("Investigate how weekly Gen AI usage relates to post-semester GPA. " \
    "Use the major filter to compare the differences in AI usage among students with varying academic performance.", 
            style={"color":"white", "marginTop":"10px"}),

    html.H2("Exploring the effects of Gen AI usage on learning metrics", 
            style={"marginTop":"50px"}),
    dcc.Dropdown(options=['All', 'Humanities', 'Medical', 'Business', 'STEM', 'Arts'], 
                 value='All', id='majors-dropdown', style={"width":"10%",
                                                           "border": "0.5px solid white",
                                                                         "borderRadius":"3px"},
                 className="dark-dropdown"),

    html.Div([
        html.Div([
            dcc.Graph(figure={}, id='Skill_Retention_Heatmap'),

            html.Hr(style={"marginTop":"5px"})],

            style={"width":"50%"}
        ),

        html.Div([
            dcc.Graph(figure={}, id='AI_Dependency_Heatmap'),

            html.Hr(style={"marginTop":"5px"})],

            style={"width":"50%"}
        )],

        style={"display":"flex",
               "alignItems":"flex-start"}
    ),

    html.P("Examine how weekly Gen AI usage relates to skill retention and perceived AI dependency. " \
        "Use the major filer to compare learning patterns and to identify how AI usage influences these learning metrics. ", 
            style={"color":"white", "marginTop":"10px"}),

    html.H2("Does Gen AI affect stress levels during exams?", style={"marginTop":"50px"}),
    dcc.Dropdown(options=['All', 'Humanities', 'Medical', 'Business', 'STEM', 'Arts'], 
                 value='All', id='majors-dropdown2', 
                 style={"width":"10%",
                        "border": "0.5px solid white",
                        "borderRadius":"3px"}, className="dark-dropdown"),

    html.Div([
        html.Div([
            dcc.Graph(figure={}, id='AI_Anxiety_Levels_Box'),
            html.Hr(style={"marginTop":"5px"})],
            style={"width":"50%"}
        ),

        html.Div([
            dcc.Graph(figure={}, id='Trad_Anxiety_Levels_Box'),
            html.Hr(style={"marginTop":"5px"})],
            style={"width":"50%"}
        )],

        style={"display":"flex",
               "alignItems":"flex-start"}
        
    ),

    html.P("Investigate how weekly Gen AI usage and traditional study hours are distributed across different exam anxiety levels. " \
    "Compare results between majors using the dropdown filter.", 
            style={"color":"white", "marginTop":"10px"}),

    html.H2("How does GPA change over the semester with the use of Gen AI (Bubble size = Weekly Gen AI usage)", style={"margin-top":"100px"}),
    dcc.RadioItems(options=['Humanities', 'Medical', 'Business', 'STEM', 'Arts'], value='Humanities', 
                   inline=True, id='majors-radio-item2', labelStyle={"color": "white"}),
    dcc.Graph(figure={}, id="Pre_Post_GPA_Scatter"),
    html.Hr(style={"marginTop":"5px"}),

    html.P("Examine the relationship between pre- and post-semester GPA while considering weekly Gen AI usage. " \
    "Larger bubbles represent students who use Gen AI more frequently.", 
            style={"color":"white", "marginTop":"10px"}),

    html.H2("Complete Student Dataset", style={"marginTop":"30px"}),

    dag.AgGrid(
                rowData=df.to_dict('records'),
                columnDefs=[{"field": i} for i in df.columns], 
                style={"height":"400px"}),

    html.P("The table below contains the complete dataset used in this dashboard. " \
    "Review individual student records, compare variables, and gain additional context for the patterns shown in the charts.", 
            style={"color":"white", "marginTop":"10px"})

],
style={"fontFamily": "Inter, Arial, sans-serif",
        "backgroundColor":"black",
        "color":"white",
        "padding":"5%"}
)

@callback(
    Output(component_id='general-info-histogram', component_property='figure'),
    Output(component_id='GPA_Scatter', component_property='figure'),
    Output(component_id='Skill_Retention_Heatmap', component_property='figure'),
    Output(component_id='AI_Dependency_Heatmap', component_property='figure'),
    Output(component_id='AI_Anxiety_Levels_Box', component_property='figure'),
    Output(component_id='Trad_Anxiety_Levels_Box', component_property='figure'),
    Output(component_id='Pre_Post_GPA_Scatter', component_property='figure'),
    Output(component_id='Year_Of_Study_AI_Usage', component_property='figure'),
    Input(component_id='general-info-radio-item', component_property='value'),
    Input(component_id='majors-radio-item', component_property='value'),
    Input(component_id='majors-dropdown', component_property='value'),
    Input(component_id='majors-dropdown2', component_property='value'),
    Input(component_id='majors-radio-item2', component_property='value'),
    Input(component_id="year-study-dropdown", component_property='value'),
    Input(component_id="graph-type-dropdown", component_property='value')
)

def update_graph(col_chosen, radio_major, dropdown_major, dropdown_major2, radio_major2, dropdown_study, dropdown_graph):
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

    filtered_df_scatter = filter_major(radio_major2)
    pre_post_scatter = px.scatter(filtered_df_scatter, x='Post_Semester_GPA', y='Pre_Semester_GPA', size='Weekly_GenAI_Hours', opacity=0.35, trendline="ols")

    def filter_year(year):
        if year == "All":
            return df
        return df[df["Year_of_Study"]==year]

    filtered_df_fig = filter_year(dropdown_study)

    def filter_graph(type):
        if type == 'violin':
            ai_fig = px.violin(filtered_df_fig, x="Major_Category", y="Weekly_GenAI_Hours", color="Major_Category", box=True, points="outliers")
        else:
            ai_fig = px.histogram(filtered_df_fig, x="Major_Category", y="Weekly_GenAI_Hours", histfunc="avg")
        return ai_fig

    ai_fig = filter_graph(dropdown_graph)
    
    return major_histogram, gpa_scatter, skill_heatmap, ai_heatmap, ai_anxiety_box, trad_anxiety_box, pre_post_scatter, ai_fig

if __name__ == '__main__':
    app.run(debug=True)