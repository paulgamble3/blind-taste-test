import streamlit as st
from components.BlindForm import BlindForm

if 'username' not in st.session_state:
    with st.form("login"):
        name = st.text_input("Enter your name:")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.username = name
            st.experimental_rerun()

else:
    # check firebase for username
    # if its NOT there
    # create a new user in firebase + task status object
    # for now just populate it with this iso eval task
    #get_user_task_state('paul', 'iso-eval')


    st.write("Welcome", st.session_state.username)
    st.button("Logout", on_click=lambda: st.session_state.pop("username"))
    st.divider()

    BlindForm()