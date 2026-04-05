import streamlit as st


def apply_theme(theme):

    if theme == "Dark":

        st.markdown(
            """
            <style>
            .stApp {
                background-color: #0E1117;
                color: white;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    elif theme == "Blue":

        st.markdown(
            """
            <style>
            .stApp {
                background-color: #E3F2FD;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    elif theme == "Corporate":

        st.markdown(
            """
            <style>
            .stApp {
                background-color: #F5F5F5;
            }
            </style>
            """,
            unsafe_allow_html=True
        )