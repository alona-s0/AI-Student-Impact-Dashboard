from dash import callback, Output, Input
from data import df
import plotly.express as px

def filter_major(major):
    """Return only rows matching the selected major."""
    if major == "All":
        return df
    return df[df["Major_Category"] == major]

def filter_year(year):
    """Return only rows matching the selected year of study."""
    if year == "All":
        return df
    return df[df["Year_of_Study"] == year]

def register_callbacks(app):

    @app.callback(
        Output(component_id="general-info-histogram", component_property="figure"),
        Input(component_id="general-info-radio-item", component_property="value")
    )
    def update_general_info(col_chosen):
        major_histogram = px.histogram(df, x="Major_Category", y=col_chosen, histfunc="avg")
        return major_histogram
    
    @app.callback(
        Output(component_id="GPA_Scatter", component_property="figure"),
        Input(component_id="majors-radio-item", component_property="value")
    )

    def update_GPA_scatter(radio_major):
         
        filtered_df = filter_major(radio_major)
        gpa_scatter = px.scatter(filtered_df, x="Post_Semester_GPA", y="Weekly_GenAI_Hours")
        return gpa_scatter

    @app.callback(
        Output(component_id="Skill_Retention_Heatmap", component_property="figure"),
        Output(component_id="AI_Dependency_Heatmap", component_property="figure"),
        Input(component_id="majors-dropdown", component_property="value")
    )

    def update_skill_heatmaps(dropdown_major):
        filtered_df_heatmap = filter_major(dropdown_major)

        skill_heatmap = px.density_heatmap(
            filtered_df_heatmap, x="Skill_Retention_Score", y="Weekly_GenAI_Hours"
        )

        ai_heatmap = px.density_heatmap(
            filtered_df_heatmap, x="Perceived_AI_Dependency", y="Weekly_GenAI_Hours"
        )
        return skill_heatmap, ai_heatmap
    
    @app.callback(
        Output(component_id="AI_Anxiety_Levels_Box", component_property="figure"),
        Output(component_id="Trad_Anxiety_Levels_Box", component_property="figure"),
        Input(component_id="majors-dropdown2", component_property="value")
    )

    def update_anxiety_box_graphs(dropdown_major2):
        filtered_df_box = filter_major(dropdown_major2)
        ai_anxiety_box = px.box(
            filtered_df_box,
            x="Anxiety_Level_During_Exams",
            y="Weekly_GenAI_Hours",
            points="outliers",
        )
        trad_anxiety_box = px.box(
            filtered_df_box,
            x="Anxiety_Level_During_Exams",
            y="Traditional_Study_Hours",
            points="outliers",
        )
        return ai_anxiety_box, trad_anxiety_box
    
    @app.callback(
        Output(component_id="Pre_Post_GPA_Scatter", component_property="figure"),
        Input(component_id="majors-radio-item2", component_property="value")
    )

    def update_prePost_GPA_scatter(radio_major2):
        filtered_df_scatter = filter_major(radio_major2)
        pre_post_scatter = px.scatter(
            filtered_df_scatter,
            x="Post_Semester_GPA",
            y="Pre_Semester_GPA",
            size="Weekly_GenAI_Hours",
            opacity=0.35,
            trendline="ols",
        )
        return pre_post_scatter

    @app.callback(
        Output(component_id="Year_Of_Study_AI_Usage", component_property="figure"),
        Input(component_id="year-study-dropdown", component_property="value"),
        Input(component_id="graph-type-dropdown", component_property="value")
    )

    def update_AI_usage_graph(dropdown_study, dropdown_graph):
        filtered_df_fig = filter_year(dropdown_study)
        def filter_graph(type):
            if type == "violin":
                ai_fig = px.violin(
                    filtered_df_fig,
                    x="Major_Category",
                    y="Weekly_GenAI_Hours",
                    color="Major_Category",
                    box=True,
                    points="outliers",
                )
            else:
                ai_fig = px.histogram(
                    filtered_df_fig,
                    x="Major_Category",
                    y="Weekly_GenAI_Hours",
                    histfunc="avg",
                )
            return ai_fig

        ai_fig = filter_graph(dropdown_graph)

        return ai_fig