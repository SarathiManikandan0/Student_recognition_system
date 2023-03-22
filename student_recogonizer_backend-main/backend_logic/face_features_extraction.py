import codecs
from click import File
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import json
# from PIL import ImageGrab


class FaceFeatureExtraction():
    np.random.seed(42)
    def __init__(self):
        
        pass
    def initilize(self):
        self.path = 'E:\Projects\hackathon\\test_app\\backend_logic\student_images'
        student_face_extraction = {}
        for student in os.listdir(self.path):
            face_extraction_list = []
            for cl in os.listdir(f"{self.path}\{student}"):
                # print(f'{self.path}\{cl}')
                curImg = cv2.imread(f'{self.path}\{student}\{cl}')
                img = cv2.cvtColor(curImg, cv2.COLOR_BGR2RGB)
                tmp = face_recognition.face_encodings(img)
                if(len(tmp) == 0):
                    continue
                encode = tmp[0]
                face_extraction_list.append(encode.tolist())
            student_face_extraction[student] = face_extraction_list
        with open("backend_logic\\features\\face_features.json", "w") as outfile:
            json.dump(student_face_extraction, outfile, indent=4, sort_keys=True)
        

   

    def detectFace(self,tempPath : str) -> str:
        if(os.path.isfile('backend_logic\\features\\face_features.json') == False):
            self.initilize()
        detected_face = None
        with open('backend_logic\\features\\face_features.json') as json_file:
            data = json.load(json_file)
            img = cv2.imread(tempPath)
            img = cv2.resize(img,(0,0),None,0.25,0.25)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    
            facesCurFrame = face_recognition.face_locations(img)
            encodesCurFrame = face_recognition.face_encodings(img,facesCurFrame)
            list_detected = []
            list_detected_names = []
            for studentName in data:
                if(len(data[studentName]) == 0):
                    continue
                for encodeFace in encodesCurFrame:
                    matches = face_recognition.compare_faces(np.asarray(data[studentName]),encodeFace)
                    faceDis = face_recognition.face_distance((data[studentName]),encodeFace)
                    matchIndex = np.argmin(faceDis)
                    if matches[matchIndex]:
                        for i in data[studentName]:
                            list_detected.append(i)
                            list_detected_names.append(studentName)
            for encodeFace in encodesCurFrame:
                matches1 = face_recognition.compare_faces(np.asarray(list_detected),encodeFace)
                faceDis1 = face_recognition.face_distance(list_detected,encodeFace)
                matchIndex1 = np.argmin(faceDis1)
                # print(len(list_detected))
                # print(len(list_detected_names))
                # print(len(matches1))
                # print(len(faceDis1))
                # print(matchIndex1)
                

                if matches1[matchIndex1]:
                    detected_face = list_detected_names[matchIndex1]
        return detected_face
        
    
# # if __name__ == "__main__":
fr = FaceFeatureExtraction()
# fr.detectFace("backend_logic\images\IMG20230308071333.jpg")
fr.initilize()
# print(fr.detectFace("E:\Projects\hackathon\sarathipics.png"))
# print(fr.detectFace("E:\Projects\hackathon\\test_app\\backend_logic\student_Images\\bhuvanesh\\bhuvanesh.jpg"))


