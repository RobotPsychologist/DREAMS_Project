'''This is the main file for the DREAMS dashboard. 
It is a web application that allows users to upload retinal 
images and get a prediction of the severity of diabetic retinopathy. 
It also allows users to track their retinal health over time. 
The dashboard is built using Streamlit and Plotly.'''

import streamlit as st

st.set_page_config(
    page_title='DREAMS',
    page_icon=':thought_balloon:',
    layout='wide'
)

st.write('# Welcome to DREAMS! :eyes::thought_balloon:')

st.sidebar.image("/home/cjrisi/Documents/School/Coursework/HealthData/DREAMS_Project/Logo.png", use_column_width=True)
st.sidebar.success("Patient Submission Form")

st.markdown(
    """
    DREAMS is an open-source app framework built specifically to aid in the detection, managment and risk assessment of the leading cause of preventable blindness, diabetic retinopathy.
    **👈 Patient Submission Form** to see how our app works!
    ### About Us
    DREAMS was created by a team of graduate students at the University of Waterloo. 
    ### Want to learn more about building your own app?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### More Information About Diabetic Reinopathy
    - [Diabetes Canada - Retinopathy](https://www.diabetes.ca/health-care-providers/clinical-practice-guidelines/chapter-30#panel-tab_FullText)
    - [American Diabetes Association - Retinopathy](https://www.diabetes.org/diabetes/complications/eye-complications)
    - [Continuous Glucose Monitoring](https://www.diabetes.ca/DiabetesCanadaWebsite/media/Managing-My-Diabetes/Tools%20and%20Resources/Continuous_Glucose_Monitoring_Advocacy_Pkg_4.pdf?ext=.pdf)
    - [Time in Range & Diabetic Retinopathy](https://diabetesjournals.org/care/article/41/11/2370/36582/Association-of-Time-in-Range-as-Assessed-by)
    - [The BETTER registry](https://type1better.com/en/the-better-project/the-better-registry/)
    """ 
)
