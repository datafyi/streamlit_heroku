import streamlit as st

st.write("""
# Substraction App (a-b) where a,b belongs to R

This app just substracts one 2nd number from first one
""")

#take user inputs
st.header('User Input Parameters')

a,b = st.number_input('A') , st.number_input('B')

st.subheader('User Input parameters')
st.write((a,b))

#display result
st.subheader('Substraction of b from a = A - B is...')
st.write(float(a)-float(b))
