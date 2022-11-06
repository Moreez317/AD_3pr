from firstTask import data_by_year
import plotly.graph_objs as go

data = data_by_year()

figure = go.Figure(go.Scatter(x=data.index, y=data.Price,
    line=dict(color="crimson"),
    marker=dict(color="white",
    size=8, line=dict(color="black", width=2)),
    mode="lines+markers"))
figure.update_xaxes(gridwidth=2, gridcolor="ivory")
figure.update_yaxes(gridwidth=2, gridcolor="ivory")
figure.update_layout(
    title="Диаграмма средних цен на золото за десятилетия",
    title_font_size=20, title_x=0.5
)

figure.show()