import streamlit as st
import plotly.io as pio


def download_chart(fig):

    try:
        img = pio.to_image(fig, format="png")

        st.download_button(
            label="Download Chart",
            data=img,
            file_name="dashboard.png",
            mime="image/png"
        )

    except Exception:

        st.info("Chart download not supported in cloud. Download data instead.")