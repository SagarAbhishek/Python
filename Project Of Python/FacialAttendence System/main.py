import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

#capture the video
video_capture=cv2.VideoCapture(0)

# load the known faces
sagar_image=face_recognition.load_image_file("Project Of Python\\FacialAttendence System\\Known_Faces\\Sagar.JPG"
                                             )
sagar_encoding=face_recognition.face_encodings(sagar_image)[0]
shalani_image=face_recognition.load_image_file("Project Of Python\\FacialAttendence System\\Known_Faces\\Shalani.jpg"
                                             )
shalani_encoding=face_recognition.face_encodings(shalani_image)[0]
reyance_image=face_recognition.load_image_file("Project Of Python\\FacialAttendence System\\Known_Faces\\Reyance.JPG"
                                             )
reyance_encoding=face_recognition.face_encodings(reyance_image)[0]


Known_face_encodings=[sagar_encoding,shalani_encoding,reyance_encoding]
Known_face_name=["Sagar","Shalani","Reyance"]

#list of expected student
students=Known_face_name.copy()

face_locations=[]
face_encodings=[]

#for current date
now=datetime.now()
current_date=now.strftime("%d-%m-%y")

#CSV file for attendence
f=open(f"Project Of Python\\FacialAttendence System\\{current_date}.csv","w+",newline="")
lnwriter=csv.writer(f)

while True:
    _, frame =video_capture.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame=cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)

    #Recognize Faces
    face_location=face_recognition.face_locations(rgb_small_frame)
    face_encodings=face_recognition.face_encodings(rgb_small_frame,face_location)

    for face_encoding in face_encodings:
        matches=face_recognition.compare_faces(Known_face_encodings,face_encoding)
        face_distance=face_recognition.face_distance(Known_face_encodings,face_encoding)
        best_match_index=np.argmin(face_distance)

        if(matches[best_match_index]):
            name=Known_face_name[best_match_index]


        #Add the text if a person is present
        if name in Known_face_name:
            font=cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText=(10,100)
            fontScale=1.5
            fontColor=(255,0,0)
            thinkness=3
            lineType=2
            cv2.putText(frame,name +" Present",bottomLeftCornerOfText,font,fontScale,fontColor,thinkness,lineType)

            if name in students:
                students.remove(name)
                current_time=now.strftime("%H-%M%S")
                lnwriter.writerow([name,current_time])


        cv2.imshow("Attendence ",frame)
        if cv2.waitKey(1) & 0xFF== ord("q"):
            break


video_capture.release()
cv2.destroyAllWindows()
f.close()