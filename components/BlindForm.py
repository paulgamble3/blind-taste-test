import streamlit as st
import json
from firebase.firebase_utils import write_task_item
import datetime
import random
import os
import pickle

# take the next object in the list, with the human/ai label
# display it
# collect feedback
# write feedback and remove the item from the list
# if list is empty, show a message

def get_user_task_state(username, task_name):
    fn = './data/user_task_state/user_task_states.json'
 
    with open(fn, 'r') as f:
        user_states = json.load(f)

    if username in user_states:
        user_state = user_states[username]
        
    else:
        label_set = random.choice(['A', 'B'])
        label_name = './data/script_sets/blind_set_' + label_set + '.pkl'
        labels = pickle.load(open(label_name, 'rb'))
        user_state = {
            'username': username,
            'task_name': task_name,
            'task_items': labels
        }
        user_states[username] = user_state
        with open(fn, 'w') as f:
            json.dump(user_states, f)
    return user_state
   

def get_item(user_state):
    fn = './data/user_task_state/user_task_states.json'
    with open(fn, 'r') as f:
        user_states = json.load(f)

    user_state = user_states[user_state['username']]

    if len(user_state["task_items"]) > 0:
        item = user_state['task_items'].pop()

        user_states[user_state['username']] = user_state
        with open(fn, 'w') as f:
            json.dump(user_states, f)
        return item
    else:
        return None



def BlindForm():

    def capture_score():
        feedback_object["Overall Subjective Quality"] = st.session_state["Overall Subjective Quality"]
        write_task_item(feedback_object, 'blind-taste-test')
        st.session_state["Overall Subjective Quality"] = "1"
        st.experimental_rerun()

    
    user = st.session_state.username
    user_state = get_user_task_state(user, 'blind-taste-test')
    item = get_item(user_state)
    label = item[1]
    script_fn = item[0]

    feedback_object = {
        'username': user,
        'task_name': 'blind-taste-test',
        'label': label,
        'script_fn': script_fn,
        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open(script_fn, 'r') as f:
        script_text = f.read()

    turns = script_text.split('\n')

    st.write(f"The following transcript is a conversation between a patient and **{label} nurse**. Please read the script and answer the following questions.")
    st.write("[Somes lines may have been omitted for brevity.]")

    for turn in turns:
        st.write(turn)

    st.write("Please answer the following questions about the script you just read.")

    with st.form("my_form"):
        key_name = "Overall Subjective Quality"
        feedback_object[key_name] = st.radio("How would you rate the overall subjective quality of the nurse in this conversation?", ("1", "2","3","4","5","6","7"), key=key_name, horizontal=True)

        st.form_submit_button("Submit", on_click=capture_score)