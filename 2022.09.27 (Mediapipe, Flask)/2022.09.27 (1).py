'''
mediapipe 얼굴인식
고양이 코, 고양이 귀 (함수 사용)
https://google.github.io/mediapipe/solutions/face_detection.html
'''

'''
mediapipe 기본 import 및 객체생성
face detection에 opencv 객체를 사용하므로
mediapipe 사용
face detection용 객체 생성
detect된 keypoints를 이미지에 표시해 주는 객체
'''
import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# 필요한 패키지 추가 import
import numpy as np

'''
<Input>
img1: 원본 이미지
img2: 합치려는 png 이미지
c: RGB 채널
x: 합치려는 원본 이미지 x좌표 (받을 때 0~1로 정규화된 상태)
y: 합치려는 원본 이미지 y좌표 (받을 때 0~1로 정규화된 상태)
xm: 합친 후 img2를 x축으로 움직일 픽셀단위
ym: 합친 후 img2를 y축으로 움직일 픽셀단위

<Output>
리턴값 없이 알아서 합쳐진 원본 이미지
'''
def imgSumByXY(img1, img2, c, x, y, xm, ym):
    img_w = int(img2.shape[1]/2)
    img_h = int(img2.shape[0]/2)
    img_x = int(x*img1.shape[1])
    img_y = int(y*img1.shape[0])
    mask = img2[:,:,3]/255

    img_sum1 = img2[:,:,c]*mask
    img_sum2 = img1[img_y-img_h+ym:img_y+img_h+ym, img_x-img_w+xm:img_x+img_w+xm, c]*(1-mask)
    img1[img_y-img_h+ym:img_y+img_h+ym, img_x-img_w+xm:img_x+img_w+xm, c]=(img_sum1+img_sum2).astype(np.uint8)

# 합칠 png 이미지 로드
nose_img = cv2.imread('./img/nose150.png',cv2.IMREAD_UNCHANGED)
LEar_img = cv2.imread('./img/left_ear80.png',cv2.IMREAD_UNCHANGED)
REar_img = cv2.imread('./img/right_ear80.png',cv2.IMREAD_UNCHANGED)
# 웹캠 로드
cap = cv2.VideoCapture(0)

'''
model_selection = 0 (0 or 1)
0: 2m 이내에 있는 얼굴을 인식할 때
1: 5m 이내에 있는 얼굴을 인식할 때

min_detection_confidence = 0.5 (0.0 ~ 1.0) (최소 감지 신뢰값)
얼굴 이라고 인식할 최솟값

Output (results.detections)
얼굴 인식 box, 오른쪽 눈, 왼쪽 눈, 코, 입, 오른쪽 귀, 왼쪽 귀
box는 LeftTop(xmin, ymin), width, height 반환 (0~1로 정규화되서 반환됨. 픽셀값 변환 필요)
key points 6개는 x, y 좌표를 반환 (0~1로 정규화되서 반환됨. 픽셀값 변환 필요)
'''
with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        # success: 웹캠이 성공적으로 로드 됐는지
        # image: cv2.waitKey(5) 5ms 마다 읽어오는 frame
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            break
        
        # 성능 향상을 위해 이미지를 읽기 전용으로
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Processes an RGB image and returns a list of the detected face location data.
        results = face_detection.process(image)

        # 이미지를 쓰기 가능으로
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        '''
        results.변수 = count, detections, index (dir로 확인)
        results.cout: <method 'count' of 'tuple' objects> 뭔지 모르겠고
        results.detections:
        [label_id: 0
        score: 0.8642400503158569           # 얼굴로 인식되는 신뢰도
        location_data {
            format: RELATIVE_BOUNDING_BOX
            relative_bounding_box {         # face_box
                xmin: 0.4175698459148407
                ymin: 0.3413591980934143
                width: 0.24680224061012268
                height: 0.3289602994918823
            }
            relative_keypoints {            # 오른쪽 눈
                x: 0.4911727011203766
                y: 0.4464417099952698
            }
            relative_keypoints {            # 왼쪽 눈
                x: 0.5891190767288208
                y: 0.4470962882041931
            }
            relative_keypoints {            # 코
                x: 0.5408813953399658
                y: 0.5222705006599426
            }
            relative_keypoints {            # 입
                x: 0.5415130853652954
                y: 0.5867577195167542
            }
            relative_keypoints {            # 오른쪽 귀
                x: 0.43904829025268555
                y: 0.47977226972579956
            }
            relative_keypoints {            # 왼쪽 귀
                x: 0.6453734636306763
                y: 0.48184114694595337
            }
        }
        ]
        results.index: <method 'index' of 'tuple' objects> 뭔지 모르겠고 
        '''
        if results.detections:
            nose_x = results.detections[0].location_data.relative_keypoints[2].x
            nose_y = results.detections[0].location_data.relative_keypoints[2].y
            LEar_x = results.detections[0].location_data.relative_keypoints[-1].x
            LEar_y = results.detections[0].location_data.relative_keypoints[-1].y
            REar_x = results.detections[0].location_data.relative_keypoints[-2].x
            REar_y = results.detections[0].location_data.relative_keypoints[-2].y

            for c in range(3):
                imgSumByXY(image, nose_img, c, nose_x, nose_y, 0, -10)
                imgSumByXY(image, LEar_img, c, LEar_x, LEar_y, 0 , -150)
                imgSumByXY(image, REar_img, c, REar_x, REar_y, 0, -150)

        cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
        # 이것도 됨 if cv2.waitKey(5) == 27:
        # 이거 and가 아니라 비트연산 & 이거임
        if cv2.waitKey(5) & 0xFF == 27:
            print(cv2.waitKey(5))
            break
cap.release()
cv2.destroyAllWindows()