from llm import llm
import re

def generate_sql(schema, question):

    prompt = f"""
You are a SQL expert.

Database Schema:
{schema}

User Question:
{question}

Rules:
- Use correct tables
- Use correct columns
- Use JOIN when data is in multiple tables
- Use table aliases
- Only return SQL query
"""

    response = llm.invoke(prompt)

    sql = response.content

    # Remove markdown
    sql = re.sub(r"```sql", "", sql)
    sql = re.sub(r"```", "", sql)

    # Keep only first SELECT statement
    match = re.search(r"(SELECT.*?;)", sql, re.DOTALL | re.IGNORECASE)

    if match:
        sql = match.group(1)

    # Remove explanation text
    sql = sql.split(";")[0] + ";"

    # Replace guessed table name
    if "sales_table" in sql:
        first_table = schema.split("Table:")[1].split("\n")[0].strip()
        sql = sql.replace("sales_table", first_table)

    return sql.strip()