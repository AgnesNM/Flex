import streamlit as st
import os


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

if password == st.secrets["password"]:
    print("Yea, you are logged in")