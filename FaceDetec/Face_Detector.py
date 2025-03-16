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
if trained_face_data.empty():
    print("Error: No cascade foudn")
    exit()
webcam = cv2.VideoCapture(0) #or video if you put "video.something"
if not webcam.isOpened():
    print("Error: could not be opened")
    exit()
print("Webcam is active. Press 'q' to quit.")
while True: 
    successful_frame_read, frame = webcam.read() #return true or false, and then the actual image
    if not successful_frame_read:
        print("Error: Failed to read the frame")
        break
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for (x,y, w,h ) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow('Awesome Face Detector Photo', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        print("Quitting...")
        break

webcam.release()
cv2.destroyAllWindows()
print("Code Completed")