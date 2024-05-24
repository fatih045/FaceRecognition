import firebase_admin
from firebase_admin import credentials

from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-8e9b8-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')
data = {
    "1": {
        "name": "Fatih Çınar",
        "major": "AI ",
        "starting_year": 2020,
        "total_attandance": 6,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2022-12-11 00:54:34"

    },
    "2": {
        "name": "Elon Musk",
        "major": "Business Man",
        "starting_year": 1999,
        "total_attandance": 45,
        "standing": "G",
        "year": 25,
        "last_attandance_time": "2022-12-11 00:54:34"

    },
    "3": {
        "name": "Jeff Bezos",
        "major": "Business Man ",
        "starting_year": 2000,
        "total_attandance": 26,
        "standing": "G",
        "year": 24,
        "last_attandance_time": "2022-12-11 00:54:34"

    },
    "4": {
        "name": "Sam Altman",
        "major": "AI",
        "starting_year": 2010,
        "total_attandance": 20,
        "standing": "G",
        "year": 14,
        "last_attandance_time": "2022-12-11 00:54:34"

    },
    "5": {
        "name": "Arda Güler",
        "major": "Football",
        "starting_year": 2019,
        "total_attandance": 12,
        "standing": "G",
        "year": 5,
        "last_attandance_time": "2022-12-19 00:54:34"

    },
    "6": {
        "name": "Arda Turan",
        "major": "Football",
        "starting_year": 2011,
        "total_attandance": 18,
        "standing": "G",
        "year": 13,
        "last_attandance_time": "2024-12-11 00:54:34"

    },
    "7": {
        "name": "Melih Mahmutoğlu",
        "major": "Basketball",
        "starting_year": 2013,
        "total_attandance": 13,
        "standing": "G",
        "year": 11,
        "last_attandance_time": "2024-10-11 00:54:34"

    },
    "8": {
        "name": "Kenan İmirzalıoğlu",
        "major": "Actor",
        "starting_year": 2000,
        "total_attandance": 50,
        "standing": "G",
        "year": 24,
        "last_attandance_time": "2024-10-14 00:54:34"

    },
    "9": {
        "name": "Tarkan",
        "major": "Singer",
        "starting_year": 1999,
        "total_attandance": 45,
        "standing": "G",
        "year": 25,
        "last_attandance_time": "2024-10-11 00:54:34"

    },
    "10": {
        "name": "Serdar Ortaç",
        "major": "Singer",
        "starting_year": 1998,
        "total_attandance": 35,
        "standing": "G",
        "year": 27,
        "last_attandance_time": "2024-10-11 00:54:34"

    },
    "11": {
        "name": "Acun Ilıcalı",
        "major": "TV Productor",
        "starting_year": 2003,
        "total_attandance": 23,
        "standing": "G",
        "year": 21,
        "last_attandance_time": "2024-10-11 00:54:34"

    },
    "12": {
        "name": "Mesut Özil",
        "major": "Football",
        "starting_year": 2005,
        "total_attandance": 50,
        "standing": "G",
        "year": 19,
        "last_attandance_time": "2024-10-11 00:54:34"

    },
    "13": {
        "name": "Orhan Pamuk",
        "major": "Writer",
        "starting_year": 1995,
        "total_attandance": 60,
        "standing": "G",
        "year": 29,
        "last_attandance_time": "2024-10-11 00:54:34"

    },
    "14": {
        "name": "Beren Saat",
        "major": "Actress",
        "starting_year": 2010,
        "total_attandance": 23,
        "standing": "G",
        "year": 14,
        "last_attandance_time": "2024-10-11 00:54:34"

    }
    ,
    "15": {
        "name": "Aziz Sancar",
        "major": "Chemistry",
        "starting_year": 1990,
        "total_attandance": 78,
        "standing": "G",
        "year": 34,
        "last_attandance_time": "2024-10-11 00:54:34"

    },

}
for key, value in data.items():
    ref.child(key).set(value)
