import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Cascade is the algorithm, classifer classifies the face

# img = cv2.imread('Friends.JPG')


#grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converts to gray scale to read

#face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#print(face_coordinates)
#for (x, y, w, h) in face_coordinates: 
    #cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0) ,2)

#cv2.imshow('Awesome Face Detector Photo', img)
#cv2.waitKey() #It will pause until a key is pressed.

webcam = cv2.VIdeoCapture(0) #or video if you put "video.something"
key = cv2.waitKey(1)
while True: 
    successful_frame_read, frame = webcam.read() #return true or false, and then the actual image
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Awesome Face Detector Photo', grayscaled_img)
    cv2.waitKey(1)

print("Code Completed")