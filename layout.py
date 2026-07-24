from dash import html, dcc
from data import df
import dash_ag_grid as dag
import plotly.io as pio

pio.templates.default = "plotly_dark"

header = html.Div(
    [
        html.Img(
            src="/assets/profile.jpg",
            className='header-image'
        ),
        html.Div(
            [
                html.H2("Alona Solianyk", className='header-heading2'),
                html.P(
                    "BSc Computer Science", className='header-paragraphs'),
                html.P(
                    "University College Cork", className='header-paragraphs'),
                html.P(
                    "Interactive dashboard analysing the impact of Generative AI on students.",
                    className='header-outline'
                ),
            ]
        ),
    ],
    className='header',
)

def create_layout():


    return html.Div(
        [
            header,
            html.H1("AI impact on students", className='center-headings'),
            html.Div(
                [
                    html.Div(
                        [
                            html.H2(
                                "Weekly Gen AI usage by different majors",
                                className='center-headings',
                            ),
                            html.Div(
                                [
                                    dcc.Dropdown(
                                        options=[
                                            "Freshman",
                                            "Sophomore",
                                            "Junior",
                                            "Senior",
                                            "All",
                                        ],
                                        value="Freshman",
                                        id="year-study-dropdown",
                                        style={
                                            "marginRight": "5px",
                                            "width": "30%"
                                        },
                                        className="dark-dropdown dropdowns",
                                    ),
                                    dcc.Dropdown(
                                        options=[
                                            {"label": "Violin Plot", "value": "violin"},
                                            {"label": "Histogram", "value": "histogram"},
                                        ],
                                        value="violin",
                                        id="graph-type-dropdown",
                                        style={"width": "30%"},
                                        className="dark-dropdown dropdowns"
                                    ),
                                ],
                                className='combined-section'
                            ),
                            dcc.Graph(
                                figure={},
                                id="Year_Of_Study_AI_Usage",
                                className='graph-height'
                            ),
                            html.Hr(className='horizontal-rule'),
                            html.P(
                                "Compare weekly Gen AI usage across different majors. "
                                "Use filters to focus on a specific year of study or switch between distribution views.",
                                className='paragraph-color'
                            ),
                        ],
                        className='graph-height',
                        style={"width": "50%"},
                    ),
                    html.Div(
                        [
                            html.H2(
                                "General information about the study program for each major",
                                className='center-headings',
                            ),
                            dcc.RadioItems(
                                options=[
                                    "Traditional_Study_Hours",
                                    "Anxiety_Level_During_Exams",
                                ],
                                value="Traditional_Study_Hours",
                                inline=True,
                                id="general-info-radio-item",
                                style={"marginLeft": "5%"},
                                labelStyle={"color": "white"},
                            ),
                            dcc.Graph(
                                figure={},
                                id="general-info-histogram",
                                className='graph-height',
                            ),
                            html.Hr(className='horizontal-rule'),
                            html.P(
                                "Compare the average traditional study hours and exam anxiety levels across different majors. "
                                "Use the selector to switch between the metrics.",
                                className='paragraph-color'
                            ),
                        ],
                        style={"width": "49%"},
                    ),
                ],
                className='double-section'
            ),
            html.H2("The impact of Gen AI on grades", style={"margin-top": "100px"}),
            dcc.RadioItems(
                options=["Humanities", "Medical", "Business", "STEM", "Arts"],
                value="Humanities",
                inline=True,
                id="majors-radio-item",
                labelStyle={"color": "white"},
            ),
            dcc.Graph(figure={}, id="GPA_Scatter"),
            html.Hr(className='horizontal-rule'),
            html.P(
                "Investigate how weekly Gen AI usage relates to post-semester GPA. "
                "Use the major filter to compare the differences in AI usage among students with varying academic performance.",
                className='paragraph-color'
            ),
            html.H2(
                "Exploring the effects of Gen AI usage on learning metrics",
                style={"marginTop": "50px"},
            ),
            dcc.Dropdown(
                options=["All", "Humanities", "Medical", "Business", "STEM", "Arts"],
                value="All",
                id="majors-dropdown",
                style={"width": "10%"},
                className="dark-dropdown dropdowns",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Graph(figure={}, id="Skill_Retention_Heatmap"),
                            html.Hr(className='horizontal-rule'),
                        ],
                        style={"width": "50%"},
                    ),
                    html.Div(
                        [
                            dcc.Graph(figure={}, id="AI_Dependency_Heatmap"),
                            html.Hr(className='horizontal-rule'),
                        ],
                        style={"width": "50%"},
                    ),
                ],
                className='double-section'
            ),
            html.P(
                "Examine how weekly Gen AI usage relates to skill retention and perceived AI dependency. "
                "Use the major filer to compare learning patterns and to identify how AI usage influences these learning metrics. ",
                className='paragraph-color'
            ),
            html.H2(
                "Does Gen AI affect stress levels during exams?",
                style={"marginTop": "50px"},
            ),
            dcc.Dropdown(
                options=["All", "Humanities", "Medical", "Business", "STEM", "Arts"],
                value="All",
                id="majors-dropdown2",
                style={"width": "10%"},
                className="dark-dropdown dropdowns",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Graph(figure={}, id="AI_Anxiety_Levels_Box"),
                            html.Hr(className='horizontal-rule'),
                        ],
                        style={"width": "50%"},
                    ),
                    html.Div(
                        [
                            dcc.Graph(figure={}, id="Trad_Anxiety_Levels_Box"),
                            html.Hr(className='horizontal-rule'),
                        ],
                        style={"width": "50%"},
                    ),
                ],
                className='double-section'
            ),
            html.P(
                "Investigate how weekly Gen AI usage and traditional study hours are distributed across different exam anxiety levels. "
                "Compare results between majors using the dropdown filter.",
                className='paragraph-color'
            ),
            html.H2(
                "How does GPA change over the semester with the use of Gen AI (Bubble size = Weekly Gen AI usage)",
                style={"margin-top": "100px"},
            ),
            dcc.RadioItems(
                options=["Humanities", "Medical", "Business", "STEM", "Arts"],
                value="Humanities",
                inline=True,
                id="majors-radio-item2",
                labelStyle={"color": "white"},
            ),
            dcc.Graph(figure={}, id="Pre_Post_GPA_Scatter"),
            html.Hr(className='horizontal-rule'),
            html.P(
                "Examine the relationship between pre- and post-semester GPA while considering weekly Gen AI usage. "
                "Larger bubbles represent students who use Gen AI more frequently.",
                className='paragraph-color'
            ),
            html.H2("Complete Student Dataset", style={"marginTop": "30px"}),
            dag.AgGrid(
                rowData=df.to_dict("records"),
                columnDefs=[{"field": i} for i in df.columns],
                style={"height": "400px"},
            ),
            html.P(
                "The table below contains the complete dataset used in this dashboard. "
                "Review individual student records, compare variables, and gain additional context for the patterns shown in the charts.",
                className='paragraph-color'
            ),
        ],
        className='whole-body'
    )