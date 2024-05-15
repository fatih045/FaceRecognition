import os

import cv2
import face_recognition
import face_recognition_models
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

from firebase_admin import db

import pickle

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-8e9b8-default-rtdb.firebaseio.com/",
    'storageBucket': "facerecognition-8e9b8.appspot.com"
})

# importing the student iamges
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))

    studentIds.append(os.path.splitext(path)[0])

    #fileName = os.path.join(folderPath, path)
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


def findEncoding(imagesList):
    encodeList = []

    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding started")
encodeListKnown = findEncoding(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding complete")

file = open("Encodefile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File saved")
