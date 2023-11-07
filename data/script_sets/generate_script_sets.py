import glob
import random
import pickle

all_scripts = glob.glob("data/raw_scripts_v2/*.txt")

script_labels_A = []
script_labels_B = []

for script in all_scripts:
    z = ["human", "AI"]
    random.shuffle(z)
    script_labels_A.append([script, z[0]])
    script_labels_B.append([script, z[1]])


random.shuffle(script_labels_A)
random.shuffle(script_labels_B)


with open("data/script_sets/blind_set_v2_A.pkl", "wb") as f:
    pickle.dump(script_labels_A, f)

with open("data/script_sets/blind_set_v2_B.pkl", "wb") as f:
    pickle.dump(script_labels_B, f)
