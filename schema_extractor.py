from sqlalchemy import inspect


def get_schema(engine):

    inspector = inspect(engine)

    schema = ""

    for table in inspector.get_table_names():

        columns = inspector.get_columns(table)

        schema += f"\nTable: {table}\n"

        for col in columns:
            schema += f"{col['name']} ({col['type']})\n"

    return schema