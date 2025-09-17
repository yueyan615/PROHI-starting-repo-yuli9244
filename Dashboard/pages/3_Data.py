import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng


st.set_page_config(               
    layout="wide"                
)

# Sidebar configuration
img1 = "./assets/SU_small.png"
st.logo(img1, size= "large", icon_image=None)  

# Page information
st.write("# Data Demo")

# Create a random dataframe
st.markdown("### Example1: Random Dataframe")
df = pd.DataFrame(
    rng(0).standard_normal((10, 20)), columns=("col %d" % i for i in range(20))
)
st.dataframe(df.style.highlight_max(axis=0))


# # Create a pandas profiling report
# st.markdown("### Example2: Pandas Profiling Report")
# df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
# pr = df.profile_report()

# st_profile_report(pr)


### Create a CSV viewer
st.markdown("### Example2: Titanic CSV Viewer")

DATA_URL = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
df = pd.read_csv(DATA_URL)

# display the url
st.caption(DATA_URL) 

# display the dataframe
st.dataframe(df, use_container_width=True)

# display the shape of dataframe
st.write(f"Total: **{df.shape[0]}** rows × **{df.shape[1]}** columns")