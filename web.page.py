import streamlit as st

st.set_page_config(page_title="My Webpage",page_icon=",tada:",layout="wide")

st.subheader("Hi Im a Robot")
st.title("Webpage")
st.write("Welcome to my webpage")
st.write("[Learn MOre >](https://www.youtube.com/)")

with st.container():
    st.write("---")
    left_column, right_column=st.columns(2)
    with left_column:
        st.write("What I Do")
        st.write("##")
    
