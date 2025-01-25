import streamlit as st
import requests
import os

# Title of the Streamlit app
st.title("Error Simulator API Caller")

# Description
st.write("Click the button below to call the `/simulate-error` API and shut down the server.")

# Button to call the API
if st.button("Simulate Minor Error"):
    os._exit(0)