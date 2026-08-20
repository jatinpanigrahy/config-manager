import streamlit as st

if 'user_settings' not in st.session_state:
    st.session_state.user_settings = {'theme': 'dark', 'volume': 'high'}

st.title("User Settings Manager")

# Context Injection: Minimal, mature explanation of the engine
st.markdown("""
*This app shows a list of application preferences. Use the controls below to add, update, or remove settings to get your desired list of preferences. Changes are processed dynamically and reflected immediately in the active session state.*
""")

st.subheader("Current Settings")
if not st.session_state.user_settings:
    st.info("No settings available.")
else:
    st.table(st.session_state.user_settings)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Add")
    add_key = st.text_input("Setting Name", key="add_key_input").lower()
    add_value = st.text_input("Setting Value", key="add_value_input").lower()
    
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
    up_key = st.text_input("Existing Setting Name", key="up_key_input").lower()
    up_value = st.text_input("New Value", key="up_value_input").lower()
    
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
    del_key = st.text_input("Setting Name to Delete", key="del_key_input").lower()
    
    if st.button("Delete Setting"):
        if not del_key:
            st.error("Field required.")
        elif del_key not in st.session_state.user_settings:
            st.error(f"'{del_key}' not found.")
        else:
            del st.session_state.user_settings[del_key]
            st.success("Deleted!")
            st.rerun()
