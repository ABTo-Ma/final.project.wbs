# Create an entry point, we will call it main_page.py
# Create the main page 
import streamlit as st

st.set_page_config (page_title = 'Hello!', page_icon = '👋')
st.write('# Welcome to our final project')
st.markdown(
    '''
    We are students at WBS Coding School and since April 2024 part of the Data Science batch 29. We have created       this multipage app so that you can see all the different things you can do with data. This app was created by     using [streamlit](https://streamlit.io/) 
    ### Please have a look at our final project and be amazed by all the featrures we have integrated! 
    **👈 Select a topic from the sidebar to start**  
    ''')