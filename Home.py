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

LOGO_IMAGE_PATH = 'images/AIEye7.png'
st.sidebar.image(LOGO_IMAGE_PATH, use_column_width=True)

st.write('# Welcome to DREAMS! :eyes::thought_balloon:')

st.markdown(
    """
    DREAMS is an app framework built specifically to aid in the detection, managment and risk assessment of the leading cause of preventable blindness, diabetic retinopathy.

    ### About Us
    DREAMS was created by a team of graduate students at the University of Waterloo. 
    #### Team Members:
    """)

# Mini Bios
bio_col1, bio_col2, bio_col3, bio_col4 = st.columns([0.25,0.25,0.25,0.25])
with bio_col1:
    ## Hossein Aboutalebi
    st.markdown("""##### Hossein Aboutalebi""")
    st.image('images/FounderLogos/Maah1.png', caption=None, width=150, use_column_width=True, clamp=False, channels="RGB", output_format="auto")
    st.markdown("""    
        - [LinkedIn](https://www.linkedin.com/in/hossein-aboutalebi-2922a2b1/)
        - [Github](https://github.com/h-aboutalebi)
        """
        )
with bio_col2:
    ## Memoona Maah
    st.markdown("""##### Memoona Maah""")
    st.image('images/FounderLogos/Maah2.jpg', caption=None, width=150, use_column_width=True, clamp=False, channels="RGB", output_format="auto")
    st.markdown("""    
        - [LinkedIn](https://www.linkedin.com/in/memoona-maah/)
        """
        )
with bio_col3:
    ## Gina Najiman
    st.markdown("""##### Gina Najiman""")
    st.image('images/FounderLogos/NajimanLogo.png', caption=None, width=150, use_column_width=True, clamp=False, channels="RGB", output_format="auto")
    st.markdown("""    
        - [LinkedIn](https://www.linkedin.com/in/paerhati-gina-najiman-724274139/)
        """
        )
with bio_col4:
    ## Christopher Risi
    st.markdown("""##### Christopher Risi""")
    st.image('images/FounderLogos/RisiLogo.png', caption=None, width=150, use_column_width=True, clamp=False, channels="RGB", output_format="auto")
    st.markdown("""    
        - [LinkedIn](https://www.linkedin.com/in/christopherrisi/)
        - [GitHub](https://github.com/RobotPsychologist)        
        """
        )

st.markdown(    
    """
    ### More Information About Diabetic Reinopathy
    - [Diabetes Canada - Retinopathy](https://www.diabetes.ca/health-care-providers/clinical-practice-guidelines/chapter-30#panel-tab_FullText)
    - [American Diabetes Association - Retinopathy](https://www.diabetes.org/diabetes/complications/eye-complications)
    - [Continuous Glucose Monitoring](https://www.diabetes.ca/DiabetesCanadaWebsite/media/Managing-My-Diabetes/Tools%20and%20Resources/Continuous_Glucose_Monitoring_Advocacy_Pkg_4.pdf?ext=.pdf)
    - [Time in Range & Diabetic Retinopathy](https://diabetesjournals.org/care/article/41/11/2370/36582/Association-of-Time-in-Range-as-Assessed-by)
    - [The BETTER registry](https://type1better.com/en/the-better-project/the-better-registry/)
    
    ### Want to learn more about building your own app?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community forums](https://discuss.streamlit.io)
    """ 
)
