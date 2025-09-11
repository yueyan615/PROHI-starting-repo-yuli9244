import streamlit as st

st.set_page_config(page_title="Individual 2 yueyan li", layout="wide")

# Sidebar configuration
img1 = "./assets/SU_small.png"
st.logo(img1, size= "large", icon_image=None)  

# # Page information
st.title("Yueyan Li")
st.markdown(
"""
    During the DSHI course, I conducted a data science project analyzing factors that influence student performance in standardized exams. Using a Kaggle dataset containing 1,000 observations and 8 features, I explored demographic and educational variables such as gender, race/ethnicity, parental education level, lunch type, and test preparation courses. The goal was to understand how these factors correlate with scores in math, reading, and writing. I performed exploratory data analysis (EDA), visualized distributions, and applied statistical methods to identify meaningful patterns. The findings suggested that parental education, completion of test preparation courses, and socioeconomic indicators had noticeable impacts on exam outcomes. This project enhanced my ability to clean, analyze, and interpret educational data within a real-world context.
"""
)


