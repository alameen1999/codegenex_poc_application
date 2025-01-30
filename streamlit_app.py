import streamlit as st
import requests
import os
import sys
import logging
import traceback

# Title of the Streamlit app
st.title("Error Simulator Applicaiton")

logging.basicConfig(stream=sys.stderr, level=logging.ERROR)

# col1, col2 = st.columns(2)

# with col1:


if st.button("Simulate Minor Error"):
    try:
        file_path = f"/restricted_folder_1/test.txt"
        with open(file_path, "w") as f:
            f.write("This will fail due to permission issues")
        st.success("File written successfully!")
    except PermissionError as e:
        error_message = f"Permission Error: {e}"
        st.error("An error occurred! Check Docker logs.")
        logging.error(error_message)

def add_numbers(a, b):
    return a + b

if st.button("Simulate Major Error"):
    try:
        result = add_numbers(5, 10)  # Updated to pass two arguments
        st.success(f"Result: {result}")
    except TypeError as e:
        stack_trace = traceback.format_exc().replace('\n', ' ')
        st.error(f"Function Call Error! Check Docker logs.\n{stack_trace}")
        logging.error(stack_trace)