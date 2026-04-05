from llm import llm
import re

def generate_sql(schema, question):

    prompt = f"""
        You are a SQL expert.

        Use ONLY tables from schema below.

        Database Schema:
        {schema}

        User Question:
        {question}

        Rules:
        - Use exact table names
        - Use exact column names
        - Only SELECT queries

        Return SQL only.
        """

    response = llm.invoke(prompt)\
    
    sql = response.content

    sql = re.sub(r"```sql", "", sql)
    sql = re.sub(r"```", "", sql)

        # Replace guessed table name
    if "sales_table" in sql:
            first_table = schema.split("Table:")[1].split("\n")[0].strip()
            sql = sql.replace("sales_table", first_table)

    return sql.strip()