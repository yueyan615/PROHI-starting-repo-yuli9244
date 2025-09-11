import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

# Sidebar configuration
st.sidebar.image("./assets/SU_large.png")

# # Page information
st.write("# Chart Demo")

### Example of charts
st.markdown("### Example: Bar Chart")
df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.bar_chart(df)


import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)
