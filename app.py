import streamlit as st
import pandas as pd

df = pd.read_csv('startup_funding.csv')


st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup', df['Startup Name'].unique().tolist())
    st.title('Startup Analysis')
else:
    df['Investors Name'] = df['Investors Name'].fillna('Undisclosed')
    st.sidebar.selectbox('Select Investor', df['Investors Name'].unique().tolist())
    st.title('Investor Analysis')


