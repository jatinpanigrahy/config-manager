import streamlit as st

if 'user_settings' not in st.session_state:
    st.session_state.user_settings = {'theme': 'dark', 'volume': 'high'}

st.title("User Settings Manager")

st.info("This is a simple settings dashboard. By default, the app starts with a 'theme' and 'volume' setting. You can add, update, or delete your preferences using the forms below. Any changes you make will instantly update the table.")

st.subheader("Current Settings")
if not st.session_state.user_settings:
    st.warning("No settings available.")
else:
    st.table(st.session_state.user_settings)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Add")
    add_name = st.text_input("Setting Name", key="add_name_input").lower()
    add_value = st.text_input("Setting Value", key="add_value_input").lower()
    
    if st.button("Add Setting"):
        if not add_name or not add_value:
            st.error("Both fields are required.")
        elif add_name in st.session_state.user_settings:
            st.error(f"'{add_name}' already exists.")
        else:
            st.session_state.user_settings[add_name] = add_value
            st.success("Added!")
            st.rerun()

with col2:
    st.subheader("Update")
    up_name = st.text_input("Existing Setting Name", key="up_name_input").lower()
    up_value = st.text_input("New Value", key="up_value_input").lower()
    
    if st.button("Update Setting"):
        if not up_name or not up_value:
            st.error("Both fields are required.")
        elif up_name not in st.session_state.user_settings:
            st.error(f"'{up_name}' not found.")
        else:
            st.session_state.user_settings[up_name] = up_value
            st.success("Updated!")
            st.rerun()

with col3:
    st.subheader("Delete")
    del_name = st.text_input("Setting Name to Delete", key="del_name_input").lower()
    
    if st.button("Delete Setting"):
        if not del_name:
            st.error("Field required.")
        elif del_name not in st.session_state.user_settings:
            st.error(f"'{del_name}' not found.")
        else:
            del st.session_state.user_settings[del_name]
            st.success("Deleted!")
            st.rerun()
