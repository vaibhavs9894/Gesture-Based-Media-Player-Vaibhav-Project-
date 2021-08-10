import cv2 

import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
from controls import *

coordinates = {
  
}


# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  activate_right_software()
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)
    h,w,_ =  image.shape
    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * w)
        y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * h)
        
        
        #--------------------------------Conditions_For_


        if x > 0 and x < w//2 and y > 0 and y < 100:
          print("volume down")
          volume_down()
        if x > w//2 and x < w and y > 0 and y < 100:
          print("volume up")
          volume_up()
        onethird = w//3
        if x > 0 and x < onethird and y > 100 and y < 200:
          print("backwards")
          backward()
        twothird= (w*2)//3    
        if x > onethird and x < twothird  and y > 100 and y < 200:
            print("play or Pause")
            play_or_pause()
        if x > twothird and x < w  and y > 100 and y < 200:
            print("forward")
            forward()

  
  
    green = (255,255,0)
    red = (255,255,255)
    thickness = 2
    cv2.line(image,(0,100),(w,100),green,thickness)
    cv2.line(image,(0,200),(w,200),green,thickness)
    cv2.line(image,(w//2,0),(w//2,100),green,thickness)
    cv2.line(image,(w//3,100),(w//3,200),green,thickness)
    cv2.line(image,(w//3*2,100),(w//3*2,200),green,thickness)

    cv2.putText(image,"Vol -",(10,80),cv2.FONT_HERSHEY_PLAIN,1,red)
    cv2.putText(image,"Vol +",(w//2+10,80),cv2.FONT_HERSHEY_PLAIN,1,red)
    cv2.putText(image,"<<",(10,200-20),cv2.FONT_HERSHEY_PLAIN,1,red)
    cv2.putText(image,"Play/Pause",(w//3+50,180),cv2.FONT_HERSHEY_PLAIN,1,red)
    cv2.putText(image,">>",(w-80,180),cv2.FONT_HERSHEY_PLAIN,1,red)
    
    #  put text in other boxes yourself

    cv2.imshow('gesture window', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break


cap.release()