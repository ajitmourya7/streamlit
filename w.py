import streamlit as st

display_text = "new Dashboard"

st.write(f'Hi {display_text}')

name_list = ['SBI', 'KOTAK', 'HDFC']

result = st.selectbox('Select Bank: ', name_list)

st.write(f'{result}')