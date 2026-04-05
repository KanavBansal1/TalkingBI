import streamlit as st


def show_dashboard_cards(dashboards):

    st.subheader("Select Dashboard")

    cols = st.columns(len(dashboards))

    selected = None

    for i, (name, fig) in enumerate(dashboards):

        with cols[i]:

            st.markdown(f"### {name}")

            st.plotly_chart(
                fig,
                use_container_width=True,
                key=f"card_{name}"
            )

            if st.button(f"Select {name}"):

                selected = name

    return selected