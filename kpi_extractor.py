from llm import llm
import json

def extract_kpi(query):

    prompt = f"""
    User query: {query}

    Extract:
    1. KPI column
    2. Chart type (bar, line, pie, scatter)
    3. Color

    Return JSON:
    {{
        "kpi": ["column"],
        "chart": "bar",
        "color": "blue"
    }}
    """

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)
    except:
        return None