import cv2
import os
import dlib

cap = cv2.VideoCapture(0)
count = 0
nameD = str(input("Name: ")).lower()
path = "./images/"+ nameD

detector = dlib.get_frontal_face_detector()

isExist = os.path.exists(path)

if isExist:
    print("Klasor zaten var")
else:
    os.makedirs(path)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).astype('uint8')
    faces = detector(rgbFrame)
    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        count += 1
        name = path + '/ ' + str(count)+'.jpg'
        if 0<= y < rgbFrame.shape[0] and 0 <= y+h < rgbFrame.shape[0] and 0 <= x < rgbFrame.shape[1] and 0 <= x+w < rgbFrame.shape[1]:
            print(f"Olusturuldu: {count}.jpg")
            cv2.imwrite(name, frame[y:y+h, x:x+w])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 248), 2)
    cv2.imshow("Dataset", frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or count > 10:
        break
cap.release()
cv2.destroyAllWindows()