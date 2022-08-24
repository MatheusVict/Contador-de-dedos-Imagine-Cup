import cv2
import mediapipe as np

webcam = cv2.VideoCapture(0)
cont = 0
hand = np.solutions.hands

Hand = hand.Hands(max_num_hands=2)
npDraw = np.solutions.drawing_utils

while True:
    check, img = webcam.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = Hand.process(imgRGB)
    handsPoints = result.multi_hand_landmarks
    h,w,_ = img.shape
    pointsControl = []

    if handsPoints:
        for points in handsPoints:
            # print(points)
            npDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
            for id, corde in enumerate(points.landmark):
                cx, cy = int(corde.x * w), int(corde.y * h)
                # cv2.putText(img, str(id), (cx, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                pointsControl.append((cx, cy))
                # print(pointsControl)

        fingers = [8, 12, 16, 20]
        contador = 0
        if points:
            if pointsControl[4][0] < pointsControl[2][0]: #Logica do deão
                contador += 1
            for x in fingers:
                if pointsControl[x][1] < pointsControl[x - 2][1]: # Logica dos outros dedos
                    contador += 1
        # print(contador)
        cv2.rectangle(img, (80, 10), (200, 100), (255, 0, 0), -1)
        cv2.putText(img, str(contador), (100, 100), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 4, (255, 255, 255), 5)


    cv2.imshow("img", img)
    cv2.waitKey(1) 