import os
import pickle

import cv2
import cvzone
import face_recognition
import numpy as np

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

from firebase_admin import db
from datetime import datetime

import pickle

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-8e9b8-default-rtdb.firebaseio.com/",
    'storageBucket': "facerecognition-8e9b8.appspot.com"
})

bucket = storage.bucket()

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread("Resources/backround.jpeg")

folderModePath = 'Resources/Model'
modelPath = os.listdir(folderModePath)
imgModelList = []

for path in modelPath:
    imgModelList.append(cv2.imread(os.path.join(folderModePath, path)))

# LOAD the encoding file
print("Loading encoded File")

file = open("Encodefile.p", 'rb')
encodeListKnownWithIds = pickle.load(file)

file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print("Encoded file loaded")

modeType = 0  # 1 mi
counter = 0
id = -1
imgStudent = []

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facecurrentFrame = face_recognition.face_locations(imgS)
    encodeCurrentFrame = face_recognition.face_encodings(imgS, facecurrentFrame)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModelList[modeType]

    if facecurrentFrame:
        for encodeFace, faceLoc in zip(encodeCurrentFrame, facecurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDistance = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print("matches",matches)
            # print("faceDistance",faceDistance)

            matchIndex = np.argmin(faceDistance)

            print("Match Index :", matchIndex)

            if matches[matchIndex]:
                # print("Known face detected")
                #
                # print(studentIds[matchIndex])
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                id = studentIds[matchIndex]

                if counter == 0:
                    cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                    cv2.imshow("Face attandance system", imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 2

        # cvoze loading için
        if counter != 0:

            if counter == 1:
                studentInfo = db.reference(f'Students/{id}').get()

                print(studentInfo)
                # get the image from the storage

                blob = bucket.get_blob(f'Images/{id}.jpeg')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)

                # update data of attandance

                datetimeObject = datetime.strptime(studentInfo['last_attandance_time'], "%Y-%m-%d %H:%M:%S")

                secondElapsed = (datetime.now() - datetimeObject).total_seconds()
                #
                if secondElapsed > 30:
                    ref = db.reference(f'Students/{id}')
                    studentInfo['total_attandance'] += 1
                    ref.child('total_attandance').set(studentInfo['total_attandance'])
                    ref.child('last_attandance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

                #


                # print(secondElapsed)
                #
                # ref = db.reference(f'Students/{id}')
                # studentInfo['total_attandance'] += 1
                # ref.child('last_attandance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            # bu else bozuk
            else:
                modeType = 0
                counter = 0
                imgBackground[44:44 + 633, 808:808 + 414] = imgModelList[modeType]

        if modeType != 0:

            if 10 < counter < 20:
                modeType = 3

            imgBackground[44:44 + 633, 808:808 + 414] = imgModelList[modeType]
            if counter <= 10:
                cv2.putText(imgBackground, str(studentInfo['total_attandance']), (861, 125),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

                cv2.putText(imgBackground, str(studentInfo['major']), (1006, 550),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(imgBackground, str(id), (1006, 493),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(imgBackground, str(studentInfo['standing']), (910, 625),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 100, 100), 1)
                cv2.putText(imgBackground, str(studentInfo['year']), (1025, 625),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 100, 100), 1)

                (w, h), _ = cv2.getTextSize(studentInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                offset = (414 - w) // 2

                cv2.putText(imgBackground, str(studentInfo['name']), (808 + offset, 445),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 50), 1)

                imgBackground[175:175 + 216, 909:909 + 216] = imgStudent

                counter += 1

                if counter >= 20:
                    counter = 0
                    modeType = 1
                    studentInfo = []
                    imgStudent = []

                    imgBackground[44:44 + 633, 808:808 + 414] = imgModelList[modeType]
    else:
        modeType = 1
        counter = 0
    # ÜST TARAF İŞE YARAMADI
    cv2.imshow("Webcam", img)
    cv2.imshow("Face attandance system", imgBackground)
    cv2.waitKey(1)
