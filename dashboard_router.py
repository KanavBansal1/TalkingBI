from llm import llm

def detect_dashboard(question):

    prompt = f"""
    Based on user question decide dashboard:

    Dashboards:
    - Sales Overview
    - Region Analysis
    - Product Analysis
    - Customer Analysis

    User Question:
    {question}

    Return only dashboard name.
    """

    response = llm.invoke(prompt)

    return response.content.strip()