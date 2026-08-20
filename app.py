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
    with st.form("add_form", clear_on_submit=True):
        add_name = st.text_input("Setting Name").lower()
        add_value = st.text_input("Setting Value").lower()
        
        if st.form_submit_button("Add Setting"):
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
    with st.form("update_form", clear_on_submit=True):
        up_name = st.text_input("Existing Setting Name").lower()
        up_value = st.text_input("New Value").lower()
        
        if st.form_submit_button("Update Setting"):
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
    with st.form("delete_form", clear_on_submit=True):
        del_name = st.text_input("Setting Name to Delete").lower()
        
        if st.form_submit_button("Delete Setting"):
            if not del_name:
                st.error("Field required.")
            elif del_name not in st.session_state.user_settings:
                st.error(f"'{del_name}' not found.")
            else:
                del st.session_state.user_settings[del_name]
                st.success("Deleted!")
                st.rerun()
