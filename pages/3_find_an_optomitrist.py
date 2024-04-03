'''This is the main file for the DREAMS dashboard. 
It is a web application that allows users to upload retinal 
images and get a prediction of the severity of diabetic retinopathy. 
It also allows users to track their retinal health over time. 
The dashboard is built using Streamlit and Plotly.'''

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='DREAMS', page_icon=":thought_balloon:", layout="wide", initial_sidebar_state="expanded")

st.title('DREAMS: Diabetic Retinopathy AI Management System :eyes::thought_balloon:')

LOGO_IMAGE_PATH = 'images/AIEye4.jpeg'
st.sidebar.image(LOGO_IMAGE_PATH, use_column_width=True)

st.markdown(
    """
    This map does not show real data yet, but someday it will!
    """
)
df = pd.DataFrame(
    np.random.randn(15, 2) / [50, 50] + [43.46, -80.52],
    columns=['lat', 'lon'])

st.map(df)