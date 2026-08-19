import streamlit as st

if 'user_settings' not in st.session_state:
    st.session_state.user_settings = {'theme': 'dark', 'volume': 'high'}

st.title("User Settings Manager")

st.subheader("Current Settings")
if not st.session_state.user_settings:
    st.info("No settings available.")
else:

    st.table(st.session_state.user_settings)

st.divider()


col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Add")
    add_key = st.text_input("New Key Name", key="add_key_input").lower()
    add_value = st.text_input("New Value", key="add_value_input").lower()
    
    if st.button("Add Setting"):
        if not add_key or not add_value:
            st.error("Both fields are required.")
        elif add_key in st.session_state.user_settings:
            st.error(f"'{add_key}' already exists.")
        else:
            st.session_state.user_settings[add_key] = add_value
            st.success("Added!")
            st.rerun() 

with col2:
    st.subheader("Update")
    up_key = st.text_input("Existing Key", key="up_key_input").lower()
    up_value = st.text_input("Updated Value", key="up_value_input").lower()
    
    if st.button("Update Setting"):
        if not up_key or not up_value:
            st.error("Both fields are required.")
        elif up_key not in st.session_state.user_settings:
            st.error(f"'{up_key}' not found.")
        else:
            st.session_state.user_settings[up_key] = up_value
            st.success("Updated!")
            st.rerun()

with col3:
    st.subheader("Delete")
    del_key = st.text_input("Key to Delete", key="del_key_input").lower()
    
    if st.button("Delete Setting"):
        if not del_key:
            st.error("Field required.")
        elif del_key not in st.session_state.user_settings:
            st.error(f"'{del_key}' not found.")
        else:
            del st.session_state.user_settings[del_key]
            st.success("Deleted!")
            st.rerun()
