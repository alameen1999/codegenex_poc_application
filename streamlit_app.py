import streamlit as st
import requests
import os
import numpy as np

# Title of the Streamlit app
st.title("Error Simulator API Caller")

# my_var = os.getenv("MY_VAR")

# Description
st.write("Click the button below to call the `/simulate-error` API and shut down the server.")

# Button to call the API
if st.button("Simulate Minor Error"):
    st.write("Here is a random number:", np.random.rand())

if st.button("Simulate Major Error1"):
    my_list = [1, 2, 3]
    print(my_list[10])  # This will raise an IndexError

if st.button("Simulate Major Error2"):
    my_dict = {"key1": "value1"}
    print(my_dict["key2"])  # This will raise a KeyError
