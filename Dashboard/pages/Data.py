import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

# Sidebar configuration
st.sidebar.image("./assets/SU_large.png")

# # Page information
st.write("# Data Demo")

# Create a random dataframe
st.markdown("### Example: Dataframe")
df = pd.DataFrame(
    rng(0).standard_normal((10, 20)), columns=("col %d" % i for i in range(20))
)
st.dataframe(df.style.highlight_max(axis=0))

# Create a random dataframe