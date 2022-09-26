import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
# 웹캠 사용
cap = cv2.VideoCapture(0)
# 0.5 이상이면 손으로 인식
with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        # 캠에서 읽어옴
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            break

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        # BGR -> RGB로 컨버트 후 손인식
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        # 다시 RGB -> BGR로 컨버트
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # 엄지[4], 검지[8] 찾아서 동그라미 표시
        if results.multi_hand_landmarks:
            # print(results.multi_hand_landmarks)
            x = int(image.shape[1] * results.multi_hand_landmarks[0].landmark[8].x)
            y = int(image.shape[0] * results.multi_hand_landmarks[0].landmark[8].y)
            image = cv2.circle(image, (x,y), 20, (0,0,255), 2)

            x = int(image.shape[1] * results.multi_hand_landmarks[0].landmark[4].x)
            y = int(image.shape[0] * results.multi_hand_landmarks[0].landmark[4].y)
            image = cv2.circle(image, (x,y), 20, (0,0,255), 2)

            # for hand_landmarks in results.multi_hand_landmarks:
            #     mp_drawing.draw_landmarks(
            #         image,
            #         hand_landmarks,
            #         mp_hands.HAND_CONNECTIONS,
            #         mp_drawing_styles.get_default_hand_landmarks_style(),
            #         mp_drawing_styles.get_default_hand_connections_style())
        # Flip the image horizontally for a selfie-view display.
        # 좌우 반전
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        # 'q'키 입력시 종료
        if cv2.waitKey(5) & 0xFF == 27:
            break
# 자원 반납
cap.release()
cv2.destroyAllWindows()
