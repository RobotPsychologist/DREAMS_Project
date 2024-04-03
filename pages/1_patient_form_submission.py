'''
This page is to pull all relevant patient data into the portal.
'''
import streamlit as st
import pandas as pd

st.set_page_config(page_title='DREAMS', page_icon=":thought_balloon:", layout="wide", initial_sidebar_state="expanded")

st.title('DREAMS: Diabetic Retinopathy AI Management System :eyes::thought_balloon:')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

st.sidebar.image("/home/cjrisi/Documents/School/Coursework/HealthData/DREAMS_Project/Logo.png", use_column_width=True)

with st.form("patient_lookup"):
    st.write("Patient Lookup Form")
    patient_id = st.text_input('Patient ID Number', '')
    patient_first_name = st.text_input('First Name', '')
    patient_last_name = st.text_input('Last Name', '')
    submitted = st.form_submit_button('Lookup Patient')
    
    if submitted:
        patient_record = pd.read_csv('patient_data/patients.csv')
        # BACKEND FLAG: If we develop a proper backend for this, 
        #               we should filter on the serveer side,
        #               not on the app side.
        patient_record = patient_record[(patient_record['patient_id'] == patient_id) | 
                                         (patient_record['patient_first_name'] == patient_first_name) | 
                                         (patient_record['patient_last_name'] == patient_last_name)]
        if len(patient_record) > 0:
            patient_lookup_id = patient_record['patient_id'].iloc[0]
            patient_lookup_ohip = patient_record['ohip_id'].iloc[0]    
            patient_lookup_first_name = patient_record['patient_first_name'].iloc[0]
            patient_lookup_last_name = patient_record['patient_last_name'].iloc[0]
            patient_lookup_dob = patient_record['date_of_birth'].iloc[0]  
            pateint_lookup_age = patient_record['age'].iloc[0]
            patient_lookup_sex = patient_record['sex'].iloc[0] 
            patient_lookup_gender = patient_record['gender'].iloc[0]
                        
            patient_lookup_address = patient_record['address'].iloc[0]
            patient_lookup_postal_code = patient_record['postal_code'].iloc[0] 
            patient_lookup_phone = patient_record['patient_primary_phone_number'].iloc[0]
            patient_lookup_email = patient_record['patient_primary_email'].iloc[0]
            patient_lookup_emergency_contact = patient_record['patient_emergency_contact'].iloc[0]
            patient_lookup_emergency_contact_phone = patient_record['patient_emergency_contact_number'].iloc[0]
            patient_lookup_primary_care_physician = patient_record['patient_primary_care_physician'].iloc[0]
            patient_lookup_primary_care_physician_phone = patient_record['patient_primary_care_physician_phone'].iloc[0]
            patient_last_visit = 'NEVER!'

            st.subheader('Patient Record:')
            patient_col1, patient_col2 = st.columns((2))
            
            with patient_col1:
                st.write(f'Patient ID: {patient_lookup_id}')
                st.write(f'OHIP: {patient_lookup_ohip}')
                st.write(f'Patient First Name: {patient_lookup_first_name}')
                st.write(f'Patient Last Name: {patient_lookup_last_name}')
                st.write(f'Date of Birth: {patient_lookup_dob}')
                st.write(f'Age: {pateint_lookup_age}')
                st.write(f'Sex: {patient_lookup_sex}')
                st.write(f'Gender: {patient_lookup_gender}')
                st.write(f'Last Visit Date: {patient_last_visit}')
            with patient_col2:
                st.write(f'Address: {patient_lookup_address}')
                st.write(f'Postal Code: {patient_lookup_postal_code}')
                st.write(f'Patient Phone #: {patient_lookup_phone}')
                st.write(f'Patient Email: {patient_lookup_email}')
                st.write(f'Emergency Contact: {patient_lookup_emergency_contact}')
                st.write(f'Emergency Contact Phone: {patient_lookup_emergency_contact_phone}')
                st.write(f'Primary Care Physician: {patient_lookup_primary_care_physician}')
                st.write(f'Primary Care Physician Phone: {patient_lookup_primary_care_physician_phone}')                    
            
        else:
            st.subheader('Patient Not Found')
            st.write('Please make sure you have written the name or id number correctly.')
    
    