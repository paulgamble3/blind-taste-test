import streamlit as st
import json
from firebase.firebase_utils import write_task_item
import datetime
import random
import os
import pickle
import glob


subjective_yes_no_qs = [
        "Was the nurse appropriately polite?",
        "Did the nurse give the patient space to go 'off topic' - i.e. discuss something that may not be directly relevant to the questions the nurse asked?",
        "Did the nurse repeat herself inappropriately?",
        "Did the nurse appropriately drive the discussion forward?",
        "Did the nurse vary the opening of each of her turns in the conversation?",
        "Does the nurse avoid quizzing the patient on information in the record?",
        "Did the nurse appropriately use transition statements, like 'first', 'next', 'then', 'finally', etc.?",
        "Was the nurse appropriately concise?",
        "Overall, how would you rate the subjective quality of the nurse's language?",
    ]


with st.form("SL-eval"):

    feedback_object = {
        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    def capture_score():
        
        feedback_object["username"] = st.session_state["username"]

        for i in range(len(subjective_yes_no_qs)):
            key_name = subjective_yes_no_qs[i]
            feedback_object["subj_" + str(i)] = str(st.session_state[key_name])
            st.session_state[key_name] = "1"
        
        write_task_item(feedback_object, 'SL-eval')

    def sample_transcript():
        transcript_dir = './data/SL_transcripts/*.txt'
        transcript_files = glob.glob(transcript_dir)
        transcript_fn = random.choice(transcript_files)
        with open(transcript_fn, 'r') as f:
            transcript_text = f.read()
        return transcript_fn, transcript_text
    
    transcript_fn, transcript_text = sample_transcript()
    feedback_object["transcript_fn"] = transcript_fn
    feedback_object["transcript_text"] = transcript_text

    username = st.text_input("Please enter your name:", key="username")

    st.header("The following transcript is a conversation between a patient and a nurse. Please read the transcript and answer the following questions.")
    st.write("Note that there may be errors in the transcript")
    st.write("")
    
    turns = transcript_text.split('\n')
    for turn in turns:
        st.write(turn)

    for key_name in subjective_yes_no_qs:
        #print(key_name)
        st.radio(key_name, ("1", "2","3","4","5","6","7"), key=key_name, horizontal=True)

    st.form_submit_button("Submit", on_click=capture_score)