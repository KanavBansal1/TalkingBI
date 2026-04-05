from llm import llm


def generate_insights(df):

    data = df.head(20).to_string()

    prompt = f"""
    You are a Business Intelligence Expert.

    Data:
    {data}

    Generate 3 business insights.
    """

    response = llm.invoke(prompt)

    return response.content