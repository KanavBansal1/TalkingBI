from llm import llm
import json
import re

def extract_kpi(user_query):

    prompt = f"""
    Extract KPI, Chart Type and Color from user query.

    Dataset columns:
    - Amount
    - Profit
    - Quantity
    - Category
    - Sub-Category
    - State
    - City
    - PaymentMode
    - CustomerName

    User Query:
    {user_query}

    Return ONLY JSON format:

    {{
    "kpi": [],
    "chart": "",
    "color": ""
    }}
    """

    response = llm.invoke(prompt)

    text = response.content

    # Extract JSON safely
    try:
        json_match = re.search(r"\{.*\}", text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
    except:
        pass

    # Intelligent fallback (dynamic)
    return intelligent_fallback(user_query)


def intelligent_fallback(query):

    query = query.lower()

    kpi = []
    
    if "profit" in query:
        kpi.append("Profit")

    if "quantity" in query:
        kpi.append("Quantity")

    if "sales" in query or "amount" in query:
        kpi.append("Amount")

    if not kpi:
        kpi = ["Amount"]

    chart = "bar"

    if "line" in query or "trend" in query:
        chart = "line"

    elif "pie" in query or "distribution" in query:
        chart = "pie"

    color = "blue"

    if "red" in query:
        color = "red"

    elif "green" in query:
        color = "green"

    elif "purple" in query:
        color = "purple"

    return {
        "kpi": kpi,
        "chart": chart,
        "color": color
    }