#entrypoint module/file

import streamlit as st

from streamlit.components.v1 import html


st.header("Fighting Insurance Fraud")
st.subheader("""

Using ML to identify and prevent insurance fraud

"""
)

#create a form

login_form = st.form (key = "login_form")

name = login_form.text_input(label='Name')
email = login_form.text_input(label='Email')
password = login_form.text_input(label='Password')

submit_button = login_form.form_submit_button(label='Log in')

#redirect

if password == st.secrets["password"]:
    st.write("You are logged in!")
    st.markdown('<a href="/Data" target=_top>Data</a>', unsafe_allow_html=True)

