import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("./firebase/iso-eval-firebase-adminsdk-zs022-968af88ead.json")

if not firebase_admin._apps:
    default_app = firebase_admin.initialize_app(cred, {
        'databaseURL':"https://iso-eval-default-rtdb.firebaseio.com/"
        })

def write_task_item(item, task_name):
    ref = db.reference(task_name)
    ref.push(item)


def retrieve_feedback(db_ref):
    ref = db.reference(db_ref)
    # Read the data at the posts reference (this is a blocking operation)
    result_ids = ref.get()
    results = []
    print("result ids:", len(result_ids))
    for i, id in enumerate(result_ids):
        if i%100 == 0:
            print(i)
        z = db.reference(db_ref + '/' + id)
        result = z.get()
        results.append(result)
    return results