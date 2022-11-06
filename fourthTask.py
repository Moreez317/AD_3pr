from firstTask import data_by_decade
import plotly.graph_objs as go

data = data_by_decade()

figure = go.Figure(go.Pie(values=data.Price,
    labels=data.index))
figure.update_traces(marker=dict(line_color="black",
    line_width=2), textfont_size=16)
figure.update_layout(
    title="Диаграмма средних цен на золото за десятилетия",
    title_font_size=20, title_x=0.5,
    height=700, margin=dict(l=0, r=0, t=30, b=0)
)

figure.show()