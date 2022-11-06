from firstTask import data_by_year
import plotly.graph_objs as go
import plotly.express as px

data = data_by_year()

figure = go.Figure(px.bar(x=data.index, y=data.Price))
figure.update_traces(marker=dict(color=data.Price,
    coloraxis="coloraxis")) 
figure.update_traces(marker=dict(line_color="black",
    line_width=2)) 
figure.update_layout(
    title="Диаграмма среднегодовых цен на золото",
    title_font_size=20, title_x=0.5,
    xaxis_title="год", xaxis_title_font_size=16,
    xaxis_tickangle=315, 
    yaxis_title="цена", yaxis_title_font_size=16,
    xaxis_tickfont_size=14, yaxis_tickfont_size=14,
    height=700, 
    margin=dict(l=0, r=0, 
    t=30, b=0) 
    )

figure.show()

