import pandas as pd
from sqlalchemy import create_engine, text


def connect_database(connection_string):

    engine = create_engine(connection_string)

    return engine


def run_query(engine, query):

    # Read only protection
    if not query.lower().strip().startswith("select"):
        raise Exception("Only SELECT queries allowed")

    df = pd.read_sql(text(query), engine)

    return df