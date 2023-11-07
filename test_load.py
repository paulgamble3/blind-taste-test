import pickle


z = './data/script_sets/blind_set_v2_A.pkl'

with open(z, 'rb') as f:
    labels = pickle.load(f)

print(labels)