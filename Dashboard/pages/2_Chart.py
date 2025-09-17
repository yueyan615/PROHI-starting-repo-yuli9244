import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng
import altair as alt


# Sidebar configuration
img1 = "./assets/SU_small.png"
st.logo(img1, size= "large", icon_image=None)  

# # Page information
st.write("# Chart Demo")

### Example of charts
st.markdown("### Example1: Bar Chart")
df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.bar_chart(df)



### Example of charts
st.markdown("### Example2: Scatter Chart")



URL = "https://vega.github.io/vega-datasets/data/cars.json"
source = pd.read_json(URL)

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N',
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    st.altair_chart(chart, theme="streamlit", use_container_width=True)

with tab2:
    st.altair_chart(chart, theme=None, use_container_width=True)



### Example of charts
st.markdown("### Example3: Scatter Chart")

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

point_selector = alt.selection_point("point_selection")
interval_selector = alt.selection_interval("interval_selection")
chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(
        x="a",
        y="b",
        size="c",
        color="c",
        tooltip=["a", "b", "c"],
        fillOpacity=alt.condition(point_selector, alt.value(1), alt.value(0.3)),
    )
    .add_params(point_selector, interval_selector)
)

event = st.altair_chart(chart, key="alt_chart", on_select="rerun")

event
