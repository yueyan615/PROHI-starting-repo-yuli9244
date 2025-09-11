import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

pip install pandas-profiling streamlit-pandas-profiling
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

# Sidebar configuration
st.sidebar.image("./assets/SU_large.png")

# # Page information
st.write("# Data Demo")

# Create a random dataframe
st.markdown("### Example1: Dataframe")
df = pd.DataFrame(
    rng(0).standard_normal((10, 20)), columns=("col %d" % i for i in range(20))
)
st.dataframe(df.style.highlight_max(axis=0))


# Create a pandas profiling report
st.markdown("### Example2: Pandas Profiling Report")
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)