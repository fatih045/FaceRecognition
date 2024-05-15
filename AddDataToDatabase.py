import firebase_admin
from firebase_admin import credentials

from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-8e9b8-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')
data = {
    "11": {
        "name": "Fatih Bey",
        "major": "AI ",
        "starting_year": 2020,
        "total_attandance": 6,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2022-12-11 00:54:34"

    },
    "2": {
        "name": "Elon  Bey",
        "major": "AI ",
        "starting_year": 1999,
        "total_attandance": 6,
        "standing": "G",
        "year": 20,
        "last_attandance_time": "2022-12-11 00:54:34"

    },
    "5": {
        "name": "Jeff  Bey",
        "major": "AI ",
        "starting_year": 2000,
        "total_attandance": 6,
        "standing": "G",
        "year": 25,
        "last_attandance_time": "2022-12-11 00:54:34"

    }

}
for key, value in data.items():
    ref.child(key).set(value)

