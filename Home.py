#entrypoint module/file

import streamlit as st

from streamlit.components.v1 import html


st.header("Flexie - Fighting Insurance Fraud")
st.subheader("""

We are using ML to identify and prevent insurance fraud

"""
)

st.write("Welcome to Flexie. Flexie is an Insurtech product that attempts to detect fraud in insurance.") 
st.write("Our main target is insurance companies.")       
st.write("This is an MVP to demo our idea. We are willing to have a conversation for customized solutions")

st.header("Flexie - Future Versions")

st.write("We are looking into an API and customer specific solutions")
              


# #create a form

# login_form = st.form (key = "login_form")

# name = login_form.text_input(label='Name')
# email = login_form.text_input(label='Email')
# password = login_form.text_input(label='Password')

# submit_button = login_form.form_submit_button(label='Log in')

# #redirect

# if password == st.secrets["password"]:
#     st.write("You are logged in!")
#     st.markdown('<a href="/Data" target=_top>Data</a>', unsafe_allow_html=True)

