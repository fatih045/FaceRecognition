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
    "25": {
        "name": "Cristiano Ronaldo",
        "major": "Football player ",
        "starting_year": 2020,
        "total_attandance": 1,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2022-12-25 08:25:25"

    },

    "26": {
        "name": "Bill Gates",
        "major": "Business tycoon",
        "starting_year": 2021,
        "total_attandance": 2,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2022-12-26 09:26:26"

    },

    "27": {
        "name": "Oprah Winfrey",
        "major": "Actress",
        "starting_year": 2021,
        "total_attandance": 2,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2022-12-27 09:27:27"

    },

    "28": {
        "name": "Lionel Messi",
        "major": "Football player",
        "starting_year": 2021,
        "total_attandance": 2,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2022-12-28 09:28:28"

    },

    "29": {
        "name": "Justin Bieber",
        "major": "Singer",
        "starting_year": 2021,
        "total_attandance": 2,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2022-12-29 09:29:29"

    },

    "30": {
        "name": "Kylie Jenner",
        "major": "Businesswoman",
        "starting_year": 2021,
        "total_attandance": 8,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2023-12-30 09:30:30"

    },

    "31": {
        "name": "Barack Obama",
        "major": "Political man",
        "starting_year": 2022,
        "total_attandance": 7,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2023-12-31 09:31:31"

    },

    "32": {
        "name": "Beyonce",
        "major": "Singer",
        "starting_year": 2022,
        "total_attandance": 3,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2023-01-01 09:32:32"

    },

    "33": {
        "name": "Selena Gomez",
        "major": "Singer",
        "starting_year": 2022,
        "total_attandance": 3,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2023-01-01 09:33:33"

    },

    "34": {
        "name": "Vladimir Putin",
        "major": "Political man",
        "starting_year": 2022,
        "total_attandance": 3,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2023-01-01 09:34:34"

    },

    "35": {
        "name": "Rihanna",
        "major": "Singer",
        "starting_year": 2022,
        "total_attandance": 4,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2023-01-01 09:35:35"

    },

    "36": {
        "name": "Kim Kardashian",
        "major": "Model",
        "starting_year": 2022,
        "total_attandance": 4,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2023-01-01 09:36:36"

    },

    "37": {
        "name": "Will Smith",
        "major": "Actor",
        "starting_year": 2022,
        "total_attandance": 3,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2023-01-01 09:37:37"

    },

    "38": {
        "name": "Shakira",
        "major": "Singer",
        "starting_year": 2022,
        "total_attandance": 4,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2023-01-01 09:38:38"

    },

    "39": {
        "name": "Donald Trump",
        "major": "Politician man",
        "starting_year": 2022,
        "total_attandance": 2,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2023-01-01 09:39:39"

    },

    "40": {
        "name": "Mark Zuckerberg",
        "major": "Owner Of Meta Platforms",
        "starting_year": 2022,
        "total_attandance": 7,
        "standing": "G",
        "year": 3,
        "last_attandance_time": "2023-01-01 09:40:40"

    },

    "41": {
        "name": "Recep Tayyip Erdoğan",
        "major": "Politician man",
        "starting_year": 2023,
        "total_attandance": 5,
        "standing": "G",
        "year": 3,
        "last_attandance_time": "2023-01-01 09:41:41"

    },

    "42": {
        "name": "Nancy Ajram",
        "major": "Singer",
        "starting_year": 2023,
        "total_attandance": 4,
        "standing": "G",
        "year": 3,
        "last_attandance_time": "2023-01-01 09:42:42"

    },

    "43": {
        "name": "Mohamed Salah",
        "major": "Football Player",
        "starting_year": 2023,
        "total_attandance": 4,
        "standing": "G",
        "year": 3,
        "last_attandance_time": "2023-01-01 09:43:43"

    },

    "44": {
        "name": "İbrahim Tatlıses",
        "major": "Singer",
        "starting_year": 2023,
        "total_attandance": 1,
        "standing": "G",
        "year": 3,
        "last_attandance_time": "2023-01-01 09:44:44"

    },

    "45": {
        "name": "Barış Arduç",
        "major": "Actor",
        "starting_year": 2023,
        "total_attandance": 2,
        "standing": "G",
        "year": 3,
        "last_attandance_time": "2023-01-01 09:45:45"

    },

    "46": {
        "name": "Aras Bulut Iynemli",
        "major": "Actor",
        "starting_year": 2023,
        "total_attandance": 2,
        "standing": "G",
        "year": 3,
        "last_attandance_time": "2023-01-01 09:46:46"

    },

    "47": {
        "name": "Burak Özçivit",
        "major": "Actor",
        "starting_year": 2023,
        "total_attandance": 2,
        "standing": "G",
        "year": 3,
        "last_attandance_time": "2023-01-01 09:47:47"

    },

    "48": {
        "name": "Kıvanç Tatlıtuğ",
        "major": "Actor",
        "starting_year": 2023,
        "total_attandance": 2,
        "standing": "G",
        "year": 3,
        "last_attandance_time": "2023-01-01 09:48:48"

    },

    "49": {
        "name": "Mustafa Ceceli",
        "major": "Singer",
        "starting_year": 2023,
        "total_attandance": 2,
        "standing": "G",
        "year": 3,
        "last_attandance_time": "2023-01-01 09:49:49"

    },

    "50": {
        "name": "Ebru Gündeş",
        "major": "Singer",
        "starting_year": 2023,
        "total_attandance": 4,
        "standing": "G",
        "year": 3,
        "last_attandance_time": "2023-01-01 09:50:50"
    },
    "51": {
        "name": "Abdeljalil Azganin",
        "major": "Student",
        "starting_year": 2022,
        "total_attandance": 4,
        "standing": "G",
        "year": 3,
        "last_attandance_time": "2023-01-01 09:51:51"
    },

    "52": {
        "name": "Emrah Demir",
        "major": "Student",
        "starting_year": 2020,
        "total_attandance": 3,
        "standing": "G",
        "year": 3,
        "last_attandance_time": "2023-01-01 09:52:52"
    },

    "53": {
        "name": " Ümit Deniz ULUŞAR",
        "major": " Head of CSE department",
        "starting_year": 2020,
        "total_attandance": 3,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2023-01-01 09:53:53"
    },
    "55": {
        "name": " Mustafa Berkay Yılmaz",
        "major": "Image Processing",
        "starting_year": 2020,
        "total_attandance": 3,
        "standing": "G",
        "year": 4,
        "last_attandance_time": "2023-01-01 09:53:53"
    },

}
for key, value in data.items():
    ref.child(key).set(value)
