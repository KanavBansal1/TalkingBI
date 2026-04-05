import plotly.express as px
import pandas as pd


# Dashboard 1
def sales_overview(df):

    sales_trend = px.line(
        df,
        x="Order Date",
        y="Amount",
        title="Sales Trend"
    )

    category_sales = px.bar(
        df,
        x="Category",
        y="Amount",
        title="Sales by Category",
        color="Category"
    )

    return sales_trend, category_sales


# Dashboard 2
def region_analysis(df):

    state_sales = px.bar(
        df,
        x="State",
        y="Amount",
        title="Sales by State",
        color="State"
    )

    state_profit = px.bar(
        df,
        x="State",
        y="Profit",
        title="Profit by State",
        color="State"
    )

    return state_sales, state_profit


# Dashboard 3
def product_analysis(df):

    category = px.pie(
        df,
        names="Category",
        values="Amount",
        title="Category Distribution"
    )

    subcategory = px.bar(
        df,
        x="Sub-Category",
        y="Amount",
        title="Sub Category Sales"
    )

    return category, subcategory


# Dashboard 4
def customer_analysis(df):

    top_customers = px.bar(
        df,
        x="CustomerName",
        y="Amount",
        title="Customer Sales"
    )

    return top_customers