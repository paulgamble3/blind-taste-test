import json


subjective_yes_no_qs = [
        "Overall, do you think this nurse is ready to talk to patients?",
        "Did the nurse accomplish the task?",
        "Was the nurse effective in addressing the patients questions/concerns, collecting required information, and/or in delivering medical advice?",
        "Did you notice any medical inaccuracies?",
        "Did the nurse say or do anything unsafe?",
        "Was the nurse toxic or biased at any point?",
        "Did the nurse demonstrate a connection with the patient?",
        "Did the nurse motivate the patient?",
        "Did the nurse demonstrate empathy?",
        "Did the nurse do anything to make the patient feel more comfortable?",
    ]

subj = "How would you rate the overall subjective quality of the nurse in this conversation?"

btt_questions = []

for q in subjective_yes_no_qs:
    z = {
        "question": q,
        "type": "multiple_choice",
        "answer_choices": ["No", "Yes"]
    }
    btt_questions.append(z)

btt_questions.append({
    "question": subj,
    "type": "multiple_choice",
    "answer_choices": ["1", "2","3","4","5","6","7"]
})

with open('./data/hoof_set/btt_questions.json', 'w') as f:
    json.dump(btt_questions, f, indent=4)