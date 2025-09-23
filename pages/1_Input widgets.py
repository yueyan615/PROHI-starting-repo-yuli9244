import streamlit as st

# Sidebar configuration
img1 = "./assets/SU_small.png"
st.logo(img1, size= "large", icon_image=None)  

# # Page information
st.write("# Input Widgets Demo")



### Example of input widgets
st.markdown("### Example1: Form")

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")


### Example of input widgets
st.markdown("### Example2: Selectbox")
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)


### Example of input widgets
st.markdown("### Example3: Toggle")
on = st.toggle("Activate feature")

if on:
    st.write("Feature activated!")


### Example of input widgets
st.markdown("### Example4: Pills")
options = ["North", "East", "South", "West"]
selection = st.pills("Directions", options, selection_mode="single")
st.markdown(f"Your selected options: {selection}.")