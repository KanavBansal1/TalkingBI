import streamlit as st
import pandas as pd

from chatbot import ask_dashboard
from voice import get_voice_input, speak
from dashboard_router import detect_dashboard
from kpi_extractor import extract_kpi
from dynamic_dashboard import generate_dashboards

from database import connect_database, run_query
from sql_generator import generate_sql
from schema_extractor import get_schema
from auth import create_users_table, add_user, login_user

from themes import apply_theme
from download import download_chart
from dashboard_cards import show_dashboard_cards
from insights import generate_insights


st.set_page_config(layout="wide")

st.title("🎙️ Talking BI")


# -----------------------------
# Authentication
# -----------------------------

create_users_table()

menu = ["Login", "Signup"]
choice = st.sidebar.selectbox("Menu", menu)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    if choice == "Login":

        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            result = login_user(username, password)

            if result:
                st.success("Logged In")
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid Credentials")

    elif choice == "Signup":

        st.subheader("Signup")

        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type="password")

        if st.button("Signup"):

            add_user(new_user, new_password)
            st.success("Account Created")

    st.stop()


# Logout

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()


# -----------------------------
# Theme
# -----------------------------

st.sidebar.title("Theme")

theme = st.sidebar.selectbox(
    "Select Theme",
    ["Light", "Dark", "Blue", "Corporate"]
)

apply_theme(theme)


# -----------------------------
# Upload Dataset
# -----------------------------

st.sidebar.title("Upload Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV or Excel",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    else:
        df = pd.read_excel(uploaded_file)

    st.session_state.uploaded_df = df
    st.sidebar.success("Dataset Uploaded")


# -----------------------------
# Session State
# -----------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "engine" not in st.session_state:
    st.session_state.engine = None


# -----------------------------
# Database Connection
# -----------------------------

st.sidebar.title("Database Connection")

connection_string = st.sidebar.text_input(
    "Connection String",
    "sqlite:///sales.db"
)

if st.sidebar.button("Connect"):

    try:

        engine = connect_database(connection_string)
        schema = get_schema(engine)

        st.session_state.engine = engine
        st.session_state.schema = schema

        st.sidebar.success("Connected")

    except Exception as e:
        st.sidebar.error(str(e))


# -----------------------------
# Ask Database
# -----------------------------

st.divider()
st.subheader("🧠 Ask Database")

query = st.text_input("Ask business question")

if query:

    # Reset insights on new query
    st.session_state.pop("insights", None)

    # -----------------------------
    # Case 1 — Uploaded Dataset
    # -----------------------------

    if "uploaded_df" in st.session_state:

        df = st.session_state.uploaded_df

        st.subheader("Using Uploaded Dataset")
        st.dataframe(df)

    # -----------------------------
    # Case 2 — Database
    # -----------------------------

    else:

        with st.spinner("Generating SQL..."):

            sql = generate_sql(
                st.session_state.schema,
                query
            )

        st.code(sql, language="sql")

        with st.spinner("Fetching Data..."):

            df = run_query(
                st.session_state.engine,
                sql
            )

        st.dataframe(df)


    # -----------------------------
    # KPI Overview
    # -----------------------------

    st.subheader("📊 KPI Overview")

    col1, col2, col3 = st.columns(3)

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) >= 1:
        col1.metric("Total", round(df[numeric_cols[0]].sum(),2))

    if len(numeric_cols) >= 2:
        col2.metric("Average", round(df[numeric_cols[1]].mean(),2))

    col3.metric("Records", len(df))


    # -----------------------------
    # Dashboards
    # -----------------------------

    with st.spinner("Generating Dashboards..."):

        kpi = extract_kpi(query)

    # fallback if extraction fails
        if not kpi or "kpi" not in kpi:
            numeric_cols = df.select_dtypes(include="number").columns

            kpi = {
                "kpi": [numeric_cols[0]],
                "chart": "bar",
                "color": "blue"
            }

        charts = generate_dashboards(
            df,
            kpi["kpi"],
            kpi.get("chart", "bar"),
            kpi.get("color", "blue")
        )

    st.subheader("Select Dashboard")

    selected = show_dashboard_cards(charts)

    if selected:

        fig = dict(charts)[selected]

        st.subheader("Selected Dashboard")

        st.plotly_chart(
            fig,
            use_container_width=True,
            key=f"dashboard_{selected}"
        )

        download_chart(fig)

        st.download_button(
            "Download Data",
            df.to_csv(index=False),
            "dashboard.csv"
        )


        # -----------------------------
        # AI Insights
        # -----------------------------

        st.subheader("🧠 AI Insights")

        if "insights" not in st.session_state:

            with st.spinner("Generating Insights..."):
                st.session_state.insights = generate_insights(df)

        st.write(st.session_state.insights)


# -----------------------------
# Talking Assistant
# -----------------------------

st.divider()
st.subheader("🎙️ Talking Assistant")

col1, col2 = st.columns([3,1])

with col1:
    question = st.text_input("Ask question")

with col2:
    if st.button("🎤 Speak"):
        voice = get_voice_input()
        st.write("You said:", voice)
        question = voice


if question:

    if "uploaded_df" in st.session_state:
        data = st.session_state.uploaded_df

    elif "engine" in st.session_state:
        data = df

    else:
        st.warning("Upload dataset or connect database first")
        st.stop()

    answer = ask_dashboard(
        data,
        "general",
        question
    )

    st.session_state.chat_history.append(
        {"user": question, "bot": answer}
    )

    audio = speak(answer)

    st.write(answer)
    st.audio(audio)


# # -----------------------------
# # Chat History
# # -----------------------------

# st.divider()

# st.subheader("💬 Chat History")

# for chat in st.session_state.chat_history:

#     st.markdown(f"**User:** {chat['user']}")
#     st.markdown(f"**AI:** {chat['bot']}")
#     st.write("---")