import streamlit as st
import requests
import os

# Title of the Streamlit app
st.title("Error Simulator Applicaiton")

logging.basicConfig(stream=sys.stderr, level=logging.ERROR)

st.header('Simulation Set 1')

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

if st.button("Simulate Major Error"):
    my_list = [1, 2, 3]
    print(my_list[10])  # This will raise an IndexError
    
st.header('Simulation Set 2')

if st.button("Simulate Minor Error"):
    try:
        file_path = f"/restricted_folder_2/test.txt"
        with open(file_path, "w") as f:
            f.write("This will fail due to permission issues")
        st.success("File written successfully!")
    except PermissionError as e:
        error_message = f"Permission Error: {e}"
        st.error("An error occurred! Check Docker logs.")
        logging.error(error_message)

if st.button("Simulate Major Error"):
    my_dict = {"key1": "value1"}
    print(my_dict["key2"])  # This will raise a KeyError
