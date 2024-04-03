'''This is the main file for the DREAMS dashboard. 
It is a web application that allows users to upload retinal 
images and get a prediction of the severity of diabetic retinopathy. 
It also allows users to track their retinal health over time. 
The dashboard is built using Streamlit and Plotly.'''

import warnings
import streamlit as st
import plotly.express as px 
import pandas as pd
import numpy as np
from streamlit_image_comparison import image_comparison
from PIL import Image
warnings.filterwarnings('ignore')

st.set_page_config(page_title='DREAMS',
                   page_icon=":thought_balloon:",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.title('DREAMS: Diabetic Retinopathy AI Management System :eyes::thought_balloon:')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

LOGO_IMAGE_PATH = 'images/AIEye7.jpeg'

def glucose_categorizer(blood_glucose_level):
    '''This function categorizes the blood glucose level into 4 categories: 
            Low, Normal, High, Very High.'''
    if blood_glucose_level < 3.9:
        return '1_Low'
    elif blood_glucose_level >= 3.9 and blood_glucose_level<= 10.0:
        return '2_Normal'
    elif blood_glucose_level > 10.0 and blood_glucose_level <= 13.3:
        return '3_High'
    elif blood_glucose_level > 13.3:
        return '4_Very High'
    else:
        return '0_Unknown'

def time_in_range_calculator(tir_df):
    '''This function calculates the time in range for the glucose levels.'''
    total_time = tir_df[tir_df['Glucose Level'] == '1_Low'| 
                        tir_df['Glucose Level'] == '2_Normal'|
                        tir_df['Glucose Level'] == '3_High'|
                        tir_df['Glucose Level'] == '4_Very High'].count()
    low_percent = tir_df[tir_df['Glucose Level'] == '1_Low'].count()/total_time
    normal_percent = tir_df[tir_df['Glucose Level'] == '2_Normal'].count()/total_time
    high_percent = tir_df[tir_df['Glucose Level'] == '3_High'].count()/total_time
    very_high_percent = tir_df[tir_df['Glucose Level'] == '4_Very High'].count()/total_time
    
    return [low_percent, normal_percent, high_percent, very_high_percent]

# Data Uploader
data_col1, data_col2 = st.columns([0.85,0.1])
with data_col1:
    fl = st.file_uploader(':file_folder: Upload your Continuous Glucose Monitor data',
                          type=['csv', 'txt', 'xlsx','xls'])
with data_col2:
    with st.popover("Help Finding CGM Data",  
                    help="Click here for step-by-step instructions to find your CGM data."):
        st.markdown("Instructions:")

if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding='ISO-8859-1')
else:
    #os.chdir(r'/home/cjrisi/Documents/School/Coursework/HealthData/DREAMS_Project') # fix this later
    df = pd.read_csv('patient_data/cgm_tables/CJR000001/20240309_Patient_glucose.csv', skiprows=1) #Make this general

# Add Glucose Level Labels
df['Glucose Level'] = df['Historic Glucose mmol/L'].apply(np.vectorize(glucose_categorizer))  
df_time_in_range = df.groupby('Glucose Level').size().reset_index(name='counts')

col1, col2 = st.columns((2))
df["Device Timestamp"] = pd.to_datetime(df["Device Timestamp"])

# Getting the min and max data
startDate = pd.to_datetime(df["Device Timestamp"].min())
endDate = pd.to_datetime(df["Device Timestamp"].max())

with col1:
    date1 = pd.to_datetime(st.date_input('Start Date', startDate))
with col2:
    date2 = pd.to_datetime(st.date_input('End Date', endDate))

df = df[(df["Device Timestamp"] >= date1) & (df["Device Timestamp"] <= date2)].copy()

# Create for CGM device
st.sidebar.image(LOGO_IMAGE_PATH, use_column_width=True)
st.sidebar.header("Choose your filter: ")
device = st.sidebar.multiselect("Select the device", df["Device"].unique())

if not device:
    df2 = df.copy()
else:
    df2 = df[df["Device"].isin(device)]
    
# Create for Serial Number
serial = st.sidebar.multiselect("Select the App serial number", df2["Serial Number"].unique())

if not serial:
    df3 = df2.copy()
else:
    df3 = df2[df2["Serial Number"].isin(serial)]
   
# Create for record type
record = st.sidebar.multiselect("Select the record type", df3["Record Type"].unique())

# Create for filter based on Device and App Serial Number
if not device and not serial and not record:
    filtered_df = df
elif not serial and not record:
    filtered_df = df[df['Device'].isin(device)]
elif not device and not record:
    filtered_df = df[df['Serial Number'].isin(serial)]
elif serial and record:
    filtered_df = df3[ df['Serial Number'].isin(serial) & df3['Record Type'].isin(record)]
elif device and record:
    filtered_df = df3[ df['Device'].isin(device) & df3['Record Type'].isin(record)]
elif device and serial:
    filtered_df = df3[ df['Device'].isin(device) & df3['Serial Number'].isin(serial)]
elif record:
    filtered_df = df3[ df3['Record Type'].isin(record)]
else:
    filtered_df = df3[ df3['Device'].isin(device) & df3['Serial Number'].isin(serial) &  df3['Record Type'].isin(record)]
    
    
#category_df = filtered_df.groupby(by = ['Record Type'], as_index=False)["Historic Glucose mmol/L"].mean()

with col1:
    st.subheader("Glucose Level Distribution")
    fig = px.histogram(filtered_df, x='Historic Glucose mmol/L', color='Glucose Level', template='seaborn')
    st.plotly_chart(fig, use_container_width=True, height = 200)
    
with col2:
    st.subheader("DR Risk Assessment")
    st.dataframe(df_time_in_range) 
    #dra_col0, dra_col1, dra_col2, dra_col3 = st.columns(4)
    #tir_metrics = time_in_range_calculator(df_time_in_range)
    #dra_col0.metric("Low", tir_metrics[0], "1.2 °F")
    #dra_col1.metric("Normal", tir_metrics[0], "-8%")
    #dra_col2.metric("High", tir_metrics[0], "4%")
    #dra_col3.metric("Very High", tir_metrics[0], "4%")
    
tab1, tab2, tab3, tab4 = st.tabs(["Raw Fundas Images", "Visit Comparison", "AI Segmentation", "AI Comparison"])

with tab1:
    fundus_col1, fundus_col2, fundus_col3, fundus_col4 = st.columns((4))    
    with fundus_col1:
        st.subheader("Prev. Visit Left Fundus")
        left_eye_prev = Image.open(
            'sample/10_left.jpeg')
        st.image(left_eye_prev, caption='**Left Eye** Status: 0 No DR', use_column_width=True)

    with fundus_col2:
        st.subheader("Prev. Visit Right Fundus")
        right_eye_prev = Image.open(
            'sample/10_right.jpeg')
        st.image(right_eye_prev, caption='**Right Eye:** Status: 0 No DR', use_column_width=True)

    with fundus_col3:
        st.subheader("Curr. Visit Left Fundus")
        left_eye_curr = Image.open(
            'sample/15_left.jpeg')
        st.image(left_eye_curr, caption='**Left Eye** Status: 1 Mild DR', use_column_width=True)

    with fundus_col4:
        st.subheader("Curr. Visit Right Fundus")
        right_eye_curr = Image.open(
            'sample/15_right.jpeg')
        st.image(right_eye_curr, caption='**Right Eye:** 2 Moderate DR', use_column_width=True)

with tab2:        
    fundus_left_compare, fundus_right_compare = st.columns((2))
    with fundus_left_compare:
        st.subheader("Left Fundus")
        image_comparison(
            img1 = Image.open('sample/10_left.jpeg'),
            img2 = Image.open('sample/15_left.jpeg'),
            make_responsive=True,
            label1="Prev. Visit",
            label2="Curr. Visit")

    with fundus_right_compare:
        st.subheader("Right Fundus")
        image_comparison(
            img1 = Image.open('sample/10_right.jpeg'),
            img2 = Image.open('sample/15_right.jpeg'),
            make_responsive=True,
            label1="Prev. Visit",
            label2="Curr. Visit")
        
with tab3:
    fundus_col1, fundus_col2, fundus_col3, fundus_col4 = st.columns((4))    
    with fundus_col1:
        st.subheader("Prev. Visit Left Fundus")
        left_eye_prev = Image.open('sample/10_left.jpeg')
        st.image(left_eye_prev, caption='**Left Eye** Status: 0 No DR', use_column_width=True)

    with fundus_col2:
        st.subheader("Prev. Visit Right Fundus")
        right_eye_prev = Image.open('sample/10_right.jpeg')
        st.image(right_eye_prev, caption='**Right Eye:** Status: 0 No DR', use_column_width=True)

    with fundus_col3:
        st.subheader("Curr. Visit Left Fundus")
        left_eye_curr = Image.open('sample/15_left.jpeg')
        st.image(left_eye_curr, caption='**Left Eye** Status: 1 Mild DR', use_column_width=True)

    with fundus_col4:
        st.subheader("Curr. Visit Right Fundus")
        right_eye_curr = Image.open('sample/15_right.jpeg')
        st.image(right_eye_curr, caption='**Right Eye:** 2 Moderate DR', use_column_width=True)

with tab4:
    fundus_col1, fundus_col2, fundus_col3, fundus_col4 = st.columns((4))    
    with fundus_col1:
        st.subheader("Prev. Visit Left Fundus")
        left_eye_prev = Image.open('sample/10_left.jpeg')
        st.image(left_eye_prev, caption='**Left Eye** Status: 0 No DR', use_column_width=True)

    with fundus_col2:
        st.subheader("Prev. Visit Right Fundus")
        right_eye_prev = Image.open('sample/10_right.jpeg')
        st.image(right_eye_prev, caption='**Right Eye:** Status: 0 No DR', use_column_width=True)

    with fundus_col3:
        st.subheader("Curr. Visit Left Fundus")
        left_eye_curr = Image.open('sample/15_left.jpeg')
        st.image(left_eye_curr, caption='**Left Eye** Status: 1 Mild DR', use_column_width=True)

    with fundus_col4:
        st.subheader("Curr. Visit Right Fundus")
        right_eye_curr = Image.open('sample/15_right.jpeg')
        st.image(right_eye_curr, caption='**Right Eye:** 2 Moderate DR', use_column_width=True)        