import streamlit as st
import pandas as pd
import random
# from joblib import load

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

    # print(location_map_toronto, location_map_centres)

    

    col1, col2 = st.beta_columns([1,1])

    with col1:
        st.markdown(f'<h2 style="font-weight: bold; padding-bottom: 0px;">Vaccine Centre Status</h2>', unsafe_allow_html=True)

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
        st.write('---')
        st.markdown("""**Ratings (1 to 5):**""")
        st.write('Waiting Time:', random.randint(1,5))
        st.write('Service:', random.randint(1,5))
        st.write('Safety Regulations:', random.randint(1,5))
    centre
    with col2:
        st.markdown(f'<h2 style="font-weight: bold; padding-bottom: 0px;">Toronto Cases by Location</h2>', unsafe_allow_html=True)

        loc_select = st.selectbox('Select Your Neighbourhood', keys2)
        loc_id = location_map_toronto[loc_select]

        cases = toronto.loc[toronto['Neighbourhood ID'] == loc_id]['Case Count']
        per = toronto.loc[toronto['Neighbourhood ID'] == loc_id]['Rate per 100,000 people']

        st.write('Neighbourhood ID: ', int(loc_id))
        st.write('Total Cases: ', int(cases))
        st.write('Rate per 100,000 people: ', per[0])
    toronto


if __name__ ==  '__main__':
    main()
