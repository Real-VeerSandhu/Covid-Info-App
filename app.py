import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Info App", page_icon="💊", layout='wide', initial_sidebar_state="collapsed")
st.write("""
    # Covid-19 Information App
    ----
    """)

def main():
    centre = pd.read_csv('data/centre.csv')
    centre = centre.drop(columns=['Unnamed: 0'])
    toronto = pd.read_csv('data/toronto_data.csv')
    toronto = toronto.drop(columns=['Unnamed: 0'])

    keys1 = list(centre['location_name'])
    values1 = list(centre['location_id'])
    location_map_centres = {keys1[i]: values1[i] for i in range(len(keys1))}

    keys2 = list(toronto['Neighbourhood Name'])
    values2 = list(toronto['Neighbourhood ID'])
    location_map_toronto = {keys2[i]: values2[i] for i in range(len(keys2))}

    col1, col2 = st.beta_columns([1,1])

    with col1:
        st.markdown(f'<h2 style="font-weight: bold; padding-bottom: 0px;">Vaccine Centre Data</h2>', unsafe_allow_html=True)

        centre_select = st.selectbox('Select Your Centre', keys1)
        centre_id = location_map_centres[centre_select]
        status =  centre['active'][centre_id-1]

        st.write('Location ID: ', centre_id)

        if status == 'Yes':
            status = 'Active'
            st.markdown(f'<p style="font-weight: bold; color:green;">Active (open to public)</p>', unsafe_allow_html=True)
        else:
            status = 'Inactive'
            st.markdown(f'Status: <p style="font-weight: bold; color:red;">Inactive (not open to public)</p>', unsafe_allow_html=True)
        st.markdown("""**Ratings (1 to 5):**""")
        st.write('Waiting Time:', random.randint(1,5))
        st.write('Service:', random.randint(1,5))
        st.write('Safety Regulations:', random.randint(1,5))
        
    with col2:
        st.markdown(f'<h2 style="font-weight: bold; padding-bottom: 0px;">Cases in Toronto by District</h2>', unsafe_allow_html=True)

        loc_select = st.selectbox('Select Your Neighbourhood', keys2)
        loc_id = location_map_toronto[loc_select]
        testing = toronto.copy()
        cases = testing.loc[testing['Neighbourhood ID'] == loc_id]['Case Count']
        per = testing.loc[testing['Neighbourhood ID'] == loc_id]['Rate per 100,000 people']
        print(type(per))
        st.write('Neighbourhood ID: ', int(loc_id))
        st.write('Total Cases: ', int(cases))
        st.write('Rate per 100,000 people: ', list(per)[0])
    st.write('----')
    col3, col4 = st.beta_columns([1,1])
    with col3:
        st.markdown(f'<h2 style="font-weight: bold; padding-bottom: 0px;">Get Vaccine Recommendation</h2>', unsafe_allow_html=True)
        st.write("""This will output the urgency of getting your vaccine (prioritization is crucial and we must target the high-risk age group)""")

        age = st.number_input('Age', 0, 100)
        conds = st.selectbox('Underlying Respiratory Conditions', ['Yes', 'No'])
        hot = st.selectbox('Located in a Hot-Spot', ['Yes', 'No'])        

        if conds == 'Yes':
            conds = 1
        else:
            conds = 0

        if hot == 'Yes':
            hot = 1
        else:
            hot = 0
            
        if st.button('Go'):
            if (conds == 1 and hot == 1):
                st.markdown(f'<p style="font-weight: bold; color:red;">High Urgency</p>', unsafe_allow_html=True)
            if (age >= 65):
                st.markdown(f'<p style="font-weight: bold; color:red;">High Urgency</p>', unsafe_allow_html=True)
            elif (age >= 55 and (conds == 1 or hot == 1)):
                st.markdown(f'<p style="font-weight: bold; color:red;">High Urgency</p>', unsafe_allow_html=True)
            elif(age >= 30):
                st.markdown(f'<p style="font-weight: bold; color:orange;">Medium Urgency</p>', unsafe_allow_html=True)
            elif (age < 30 and (conds == 0 and hot == 0)):
                    st.markdown(f'<p style="font-weight: bold; color:green;">Low Urgency</p>', unsafe_allow_html=True)
            elif (age < 30 and (conds == 0 or hot == 0)):
                    st.markdown(f'<p style="font-weight: bold; color:green;">Medium Urgency</p>', unsafe_allow_html=True)

if __name__ ==  '__main__':
    main()