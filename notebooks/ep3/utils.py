import plotly.offline as py
import plotly.graph_objs as go
import numpy as np


def plot(image, title="", width=400, height=400):
    image = np.rot90(image.reshape((20, 20)), 1)
    data = [
        go.Heatmap(
            z=-image,
            colorscale='Greys', zsmooth="best", showscale = False
        )
    ]

    layout = go.Layout(
        title=title,
        autosize=False,
        width=width,
        height=height,
        yaxis=dict(
            showticklabels=False,
            ticks=""
        ),
        xaxis=dict(
            showticklabels=False,
            ticks=""
        )
    )

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig)



