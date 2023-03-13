import streamlit as st
import pandas as pd

df = pd.read_csv('startup_funding.csv')


st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup', ['A', 'B', 'C'])
    st.title('Startup Analysis')
else:
    st.sidebar.selectbox('Select Investor', ['P', 'Q', 'R'])
    st.title('Investor Analysis')


