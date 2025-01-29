import streamlit as st
import requests
import os
import sys
import logging
import traceback

# Title of the Streamlit app
st.title("Error Simulator Applicaiton")

logging.basicConfig(stream=sys.stderr, level=logging.ERROR)


col1, col2 = st.columns(2)

with col1:
    st.header('Simulation Set 1')

    if st.button("Simulate Minor Error 1"):
        try:
            file_path = f"/restricted_folder_1/test.txt"
            with open(file_path, "w") as f:
                f.write("This will fail due to permission issues")
            st.success("File written successfully!")
        except PermissionError as e:
            error_message = f"Permission Error: {e}"
            st.error("An error occurred! Check Docker logs.")
            logging.error(error_message)

    if st.button("Simulate Major Error 1"):
        try:
            my_list = [1, 2, 3]
            print(my_list[10])
        except Exception as e: 
            stack_trace = traceback.format_exc().replace('\n', ' ')
            st.error(f"An error occurred! Check Docker logs.\n{stack_trace}")
            logging.error(stack_trace)


with col2:
    st.header('Simulation Set 2')

    if st.button("Simulate Minor Error 2"):
        try:
            file_path = f"/restricted_folder_2/test.txt"
            with open(file_path, "w") as f:
                f.write("This will fail due to permission issues")
            st.success("File written successfully!")
        except PermissionError as e:
            error_message = f"Permission Error: {e}"
            st.error("An error occurred! Check Docker logs.")
            logging.error(error_message)

    if st.button("Simulate Major Error 2"):
        try:
            my_dict = {"key1": "value1"}
            print(my_dict["key2"])
            error_message = f"An error occurred: {e}"
        except Exception as e: 
            stack_trace = traceback.format_exc().replace('\n', ' ')
            st.error(f"An error occurred! Check Docker logs.\n{stack_trace}")
            logging.error(stack_trace)
import streamlit as st
import requests
import os
import sys
import logging
import traceback

# Title of the Streamlit app
st.title("Error Simulator Applicaiton")

logging.basicConfig(stream=sys.stderr, level=logging.ERROR)


col1, col2 = st.columns(2)

with col1:
    st.header('Simulation Set 1')

    if st.button("Simulate Major Error 1"):
        try:
            my_list = [1, 2, 3]
            if len(my_list) > 10:
                print(my_list[10])
            else:
                st.write("List index is out of range.")
        except Exception as e:
            stack_trace = traceback.format_exc().replace('\n', ' ')
            st.error(f"An error occurred! Check Docker logs.\n{stack_trace}")
            logging.error(stack_trace)

with col2:
    st.header('Simulation Set 2')

    if st.button("Simulate Major Error 2"):
        try:
            my_dict = {"key1": "value1"}
            print(my_dict["key2"])
            error_message = f"An error occurred: {e}"
        except Exception as e:
            stack_trace = traceback.format_exc().replace('\n', ' ')
            st.error(f"An error occurred! Check Docker logs.\n{stack_trace}")
            logging.error(stack_trace)