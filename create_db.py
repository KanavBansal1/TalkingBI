import pandas as pd
from sqlalchemy import create_engine

orders = pd.read_csv("data/Orders.csv")
details = pd.read_csv("data/Details.csv")

df = pd.merge(orders, details, on="Order ID")

engine = create_engine("sqlite:///sales.db")

df.to_sql("sales", engine, index=False, if_exists="replace")

print("Database Created")