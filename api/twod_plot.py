import altair as alt
# Function to generate the 2D plot


def generate_chart(df, xcol, ycol, color='basic', title=''):
    chart = alt.Chart(df).mark_circle(size=500).encode(
        x=alt.X(xcol,
                scale=alt.Scale(zero=False),
                axis=alt.Axis(labels=False, ticks=False, domain=False)
                ),
        y=alt.Y(ycol,
                scale=alt.Scale(zero=False),
                axis=alt.Axis(labels=False, ticks=False, domain=False)
                ),
        color=alt.value('#333293') if color == 'basic' else color,
        tooltip=['title']
    )
    result = chart.configure(background="#FDF7F0"
                             ).properties(
        width=800,
        height=500,
        title=title
    ).configure_legend(
        orient='bottom', titleFontSize=18, labelFontSize=18)
    return result
