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

if st.button("Simulate Major Error1"):
    my_list = [1, 2, 3]
    print(my_list[10])  # This will raise an IndexError

if st.button("Simulate Major Error2"):
    my_dict = {"key1": "value1"}
    print(my_dict["key2"])  # This will raise a KeyError
