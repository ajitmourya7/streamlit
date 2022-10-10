import streamlit as st

display_text = "Hi new Dashboard"

st.write(f'{display_text}')

name_list = ['SBI', 'KOTAK', 'HDFC']

result = st.selectbox('Select Bank: ', name_list)

st.write(f'{result}')