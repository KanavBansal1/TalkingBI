import plotly.express as px


def detect_columns(df):

    numeric_cols = df.select_dtypes(include="number").columns
    categorical_cols = df.select_dtypes(include="object").columns

    if len(numeric_cols) == 0:
        numeric_cols = [df.columns[-1]]

    if len(categorical_cols) == 0:
        categorical_cols = [df.columns[0]]

    return categorical_cols[0], numeric_cols[0]


def generate_dashboards(df, kpi, chart, color):

    dashboards = []

    x, y = detect_columns(df)

    # Bar Chart
    fig1 = px.bar(
        df,
        x=x,
        y=y,
        title=f"{y} by {x}",
        color_discrete_sequence=[color]
    )

    dashboards.append(("Bar Chart", fig1))


    # Line Chart
    fig2 = px.line(
        df,
        x=x,
        y=y,
        title=f"{y} Trend"
    )

    dashboards.append(("Line Chart", fig2))


    # Pie Chart
    fig3 = px.pie(
        df,
        names=x,
        values=y,
        title=f"{y} Distribution"
    )

    dashboards.append(("Pie Chart", fig3))


    # Scatter Chart
    fig4 = px.scatter(
        df,
        x=x,
        y=y,
        title=f"{y} Scatter"
    )

    dashboards.append(("Scatter Chart", fig4))

    return dashboards