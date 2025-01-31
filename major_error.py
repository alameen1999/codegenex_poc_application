import streamlit as st
import requests
import os
import sys
import logging
import traceback

# Title of the Streamlit app
st.title("Error Simulator Application")

logging.basicConfig(stream=sys.stderr, level=logging.ERROR)

def add_numbers(a, b):
    return a + b

if st.button("Simulate Major Error"):
    try:
        result = add_numbers(5, 10)  # Updated function call with two arguments
        st.success(f"Result: {result}")
    except TypeError as e:
        stack_trace = traceback.format_exc().replace('\n', ' ')
        st.error(f"Function Call Error! Check Docker logs.\n{stack_trace}")
        logging.error(stack_trace)