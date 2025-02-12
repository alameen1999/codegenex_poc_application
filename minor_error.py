import streamlit as st
import requests
import os
import sys
import logging
import traceback

# Title of the Streamlit app
st.title("Error Simulator Applicaiton")

logging.basicConfig(stream=sys.stderr, level=logging.ERROR)

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
