from llm import llm

def ask_dashboard(df, dashboard, question):

    data_summary = df.head(50).to_string()

    prompt = f"""
    You are a Business Intelligence Assistant.

    Current Dashboard: {dashboard}

    Dataset:
    {data_summary}

    User Question:
    {question}

    Give business insights based on selected dashboard.
    """

    response = llm.invoke(prompt)

    return response.content