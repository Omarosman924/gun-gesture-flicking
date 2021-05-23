import cv2
import mediapipe as mp
import time
import numpy as np
import random
#import pygame
cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,640)
#pygame.mixer.init()
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands =2,min_tracking_confidence = .99)
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0
stat = ''
randomx = 236
randomy = 333
count = 0

while True:
    black = np.zeros((480,640,3))
    import random
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    cv2.circle(img, (randomx, randomy), 20, (0, 0, 255), cv2.FILLED)
    cv2.circle(img, (randomx, randomy), 15, (0, 255, 255), cv2.FILLED)
    cv2.circle(img, (randomx, randomy), 10, (0, 0, 255), cv2.FILLED)
    cv2.circle(img, (randomx, randomy), 5, (123, 125, 255), cv2.FILLED)
    cv2.circle(img, (randomx, randomy), 2, (0, 0, 0), cv2.FILLED)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            #mpDraw.draw_landmarks(black,handLms,mpHands.HAND_CONNECTIONS)
            landmarks = []
            for id, lm in enumerate(handLms.landmark):
                mpDraw.draw_landmarks(img,handLms, mpHands.HAND_CONNECTIONS)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #cv2.putText(img, str(id), (cx, cy), cv2.FONT_HERSHEY_PLAIN, .5,0)
                landmarks.append([cx,cy])
        landmarks = np.array(landmarks)
        if landmarks[4][1]< landmarks[8][1] and landmarks[4][1]< landmarks[6][1] :
            if landmarks[4][1] < landmarks[6][1]:
                stat = 'aim'
                #cv2.circle(black, (landmarks[4][0], landmarks[4][1]), 5, (255, 0, 0), cv2.FILLED)
        elif landmarks[8][1]<landmarks[4][1] and landmarks[8][1]<landmarks[6][1] :
            if landmarks[8][1] < landmarks[9][1]:
                stat = 'aim'
                #cv2.circle(black, (landmarks[8][0], landmarks[8][1]), 5, (255, 0, 0), cv2.FILLED)
        else:
            if stat == 'aim':
                if landmarks[8][1]< landmarks[4][1]:
                    
                    #cv2.circle(img, (landmarks[8][0], landmarks[8][1]), 5, (255, 0, 0), cv2.FILLED)
                    
                    if landmarks[8][0] in range(randomx-40,randomx+40) and landmarks[8][1] in range(randomy-40 ,randomy+40):
                        
                        #pygame.mixer.music.load('Pew sound effect.mp3')
                        #pygame.mixer.music.play(0)
                        randomx = random.randint(100, 400)
                        randomy = random.randint(100, 400)
                        count +=1
                else:
                    
                    #cv2.circle(img, (landmarks[4][0], landmarks[4][1]), 5, (255, 0, 0), cv2.FILLED)
                    
                    if landmarks[4][0] in range(randomx-40,randomx+40) and landmarks[4][1] in range(randomy-40,randomy+40):
                        #pygame.mixer.music.load('Pew sound effect.mp3')
                        #pygame.mixer.music.play(0)
                        randomx = random.randint(100, 300)
                        randomy = random.randint(100, 500)
                        
                        count +=1
            #print(randomx,randomy)        
            stat = 'fire'
                
    
    

    #cTime = time.time()
    #fps = 1 / (cTime - pTime)
    #pTime = cTime

    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
     #          (255, 0, 255), 3)
    cv2.putText(img, 'pew = '+str(count), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1,
               (0, 0, 255), 2)

    cv2.imshow("pew", img)
    cv2.waitKey(1)
