import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng


# Sidebar configuration
st.sidebar.image("./assets/SU_large.png")

# Page information
st.write("# Data Demo")

# Create a random dataframe
st.markdown("### Example1: Dataframe")
df = pd.DataFrame(
    rng(0).standard_normal((10, 20)), columns=("col %d" % i for i in range(20))
)
st.dataframe(df.style.highlight_max(axis=0))


# # Create a pandas profiling report
# st.markdown("### Example2: Pandas Profiling Report")
# df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
# pr = df.profile_report()

# st_profile_report(pr)


### 
st.markdown("### Example2: Titanic CSV Viewer")

DATA_URL = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"

@st.cache_data
def load_data(url: str) -> pd.DataFrame:
    return pd.read_csv(url)

st.caption(DATA_URL)

df = load_data(DATA_URL)
st.write(f"Total: **{df.shape[0]}** rows × **{df.shape[1]}** columns")
st.dataframe(df, use_container_width=True)