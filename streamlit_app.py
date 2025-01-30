import streamlit as st

if st.button("Simulate Major Error 2"):
    try:
        my_dict = {"key1": "value1"}
        value = my_dict.get("key2", "Default value")
        print(value)
    except KeyError:
        st.error("The key 'key2' does not exist in the dictionary.")