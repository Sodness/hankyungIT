## 고양이 코, 고양이 귀 (함수 없이)
# import cv2
# import mediapipe as mp
# import numpy as np
# mp_face_detection = mp.solutions.face_detection
# mp_drawing = mp.solutions.drawing_utils

# nose_img = cv2.imread('./img/nose150.png',cv2.IMREAD_UNCHANGED)
# nose_w = int(nose_img.shape[1]/2)
# nose_h = int(nose_img.shape[0]/2)
# LEar_img = cv2.imread('./img/left_ear80.png',cv2.IMREAD_UNCHANGED)
# LEar_w = int(LEar_img.shape[1]/2)
# LEar_h = int(LEar_img.shape[0]/2)
# REar_img = cv2.imread('./img/right_ear80.png',cv2.IMREAD_UNCHANGED)
# REar_w = int(REar_img.shape[1]/2)
# REar_h = int(REar_img.shape[0]/2)

# cap = cv2.VideoCapture(0)

# with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
#     while cap.isOpened():
#         success, image = cap.read()
#         if not success:
#             print("Ignoring empty camera frame.")
#             break

#         image.flags.writeable = False
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         results = face_detection.process(image)

#         image.flags.writeable = True
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#         if results.detections:
#             nose_x = results.detections[0].location_data.relative_keypoints[2].x
#             nose_x = int(nose_x*image.shape[1])
#             nose_y = results.detections[0].location_data.relative_keypoints[2].y
#             nose_y = int(nose_y*image.shape[0])

#             LEar_x = results.detections[0].location_data.relative_keypoints[-1].x
#             LEar_x = int(LEar_x*image.shape[1])
#             LEar_y = results.detections[0].location_data.relative_keypoints[-1].y
#             LEar_y = int(LEar_y*image.shape[0])

#             REar_x = results.detections[0].location_data.relative_keypoints[-2].x
#             REar_x = int(REar_x*image.shape[1])
#             REar_y = results.detections[0].location_data.relative_keypoints[-2].y
#             REar_y = int(REar_y*image.shape[0])

#             nose_mask = nose_img[:,:,3]/255
#             LEar_mask = LEar_img[:,:,3]/255
#             REar_mask = REar_img[:,:,3]/255

#             for c in range(3):
#                 img_sum1 = nose_img[:,:,c]*nose_mask
#                 img_sum2 = image[nose_y-nose_h-10:nose_y+nose_h-10, nose_x-nose_w:nose_x+nose_w, c]*(1-nose_mask)
#                 image[nose_y-nose_h-10:nose_y+nose_h-10, nose_x-nose_w:nose_x+nose_w, c]=(img_sum1+img_sum2).astype(np.uint8)
#                 imgSumByXY(image, nose_img, nose_x, nose_y, 0, -10)

#                 img_sum1 = LEar_img[:,:,c]*LEar_mask
#                 img_sum2 = image[LEar_y-LEar_h-150:LEar_y+LEar_h-150, LEar_x-LEar_w:LEar_x+LEar_w, c]*(1-LEar_mask)
#                 image[LEar_y-LEar_h-150:LEar_y+LEar_h-150, LEar_x-LEar_w:LEar_x+LEar_w, c]=(img_sum1+img_sum2).astype(np.uint8)
#                 imgSumByXY(image, LEar_img, LEar_x, LEar_y, 0 , -150)

#                 img_sum1 = REar_img[:,:,c]*REar_mask
#                 img_sum2 = image[REar_y-REar_h-150:REar_y+REar_h-150, REar_x-REar_w:REar_x+REar_w, c]*(1-REar_mask)
#                 image[REar_y-REar_h-150:REar_y+REar_h-150, REar_x-REar_w:REar_x+REar_w, c]=(img_sum1+img_sum2).astype(np.uint8)
#                 imgSumByXY(image, REar_img, REar_x, REar_y, 0, -150)

#             # print(x,y)
#             # print(image.shape)
#             # print(tuple(x, y))
#             # image = cv2.circle(image, (x,y), 3, (0,0,255), -1)
#             # for detection in results.detections:
#             #     mp_drawing.draw_detection(image, detection)
#         cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
#         if cv2.waitKey(5) & 0xFF == 27:
#             break
# cap.release()
# cv2.destroyAllWindows()

#----------------------------------------------------------------------------------------
## 고양이 코, 고양이 귀 (함수 사용)
# import cv2
# import mediapipe as mp
# import numpy as np
# mp_face_detection = mp.solutions.face_detection
# mp_drawing = mp.solutions.drawing_utils


# def imgSumByXY(img1, img2, x, y, xm, ym):
#     img_w = int(img2.shape[1]/2)
#     img_h = int(img2.shape[0]/2)
#     img_x = int(x*img1.shape[1])
#     img_y = int(y*img1.shape[0])
#     mask = img2[:,:,3]/255

#     img_sum1 = img2[:,:,c]*mask
#     img_sum2 = img1[img_y-img_h+ym:img_y+img_h+ym, img_x-img_w+xm:img_x+img_w+xm, c]*(1-mask)
#     img1[img_y-img_h+ym:img_y+img_h+ym, img_x-img_w+xm:img_x+img_w+xm, c]=(img_sum1+img_sum2).astype(np.uint8)


# nose_img = cv2.imread('./img/nose150.png',cv2.IMREAD_UNCHANGED)
# LEar_img = cv2.imread('./img/left_ear80.png',cv2.IMREAD_UNCHANGED)
# REar_img = cv2.imread('./img/right_ear80.png',cv2.IMREAD_UNCHANGED)

# cap = cv2.VideoCapture(0)

# with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
#     while cap.isOpened():
#         success, image = cap.read()
#         if not success:
#             print("Ignoring empty camera frame.")
#             break

#         image.flags.writeable = False
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         results = face_detection.process(image)

#         image.flags.writeable = True
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#         if results.detections:
#             nose_x = results.detections[0].location_data.relative_keypoints[2].x
#             nose_y = results.detections[0].location_data.relative_keypoints[2].y
#             LEar_x = results.detections[0].location_data.relative_keypoints[-1].x
#             LEar_y = results.detections[0].location_data.relative_keypoints[-1].y
#             REar_x = results.detections[0].location_data.relative_keypoints[-2].x
#             REar_y = results.detections[0].location_data.relative_keypoints[-2].y

#             for c in range(3):
#                 imgSumByXY(image, nose_img, nose_x, nose_y, 0, -10)
#                 imgSumByXY(image, LEar_img, LEar_x, LEar_y, 0 , -150)
#                 imgSumByXY(image, REar_img, REar_x, REar_y, 0, -150)

#         cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
#         if cv2.waitKey(5) & 0xFF == 27:
#             break
# cap.release()
# cv2.destroyAllWindows()

#----------------------------------------------------------------------------------------
## 고양이 코, 고양이 귀 (함수 사용, 비율 조절)
import cv2
import mediapipe as mp
import numpy as np
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


def imgSumByXY(img1, img2, c, x, y, xm, ym, fw, fh):
    # img_w = int(img2.shape[1]/2)
    # img_h = int(img2.shape[0]/2)
    rw_h = int(fw/4/2)
    rh_h = int(fh/4/2)
    img_x = int(x*img1.shape[1])
    img_y = int(y*img1.shape[0])

    img_rs=cv2.resize(img2,(int(fw/4),int(fh/4)))
    mask=img_rs[:,:,3]/255
    mask_w = mask.shape[1]
    mask_h = mask.shape[0]
    # mask = img2[:,:,3]/255
    # print(mask.shape)
    # print(mask_w, mask_h)
    # print(rh_h, mask_h-rh_h)
    # print(rw_h, mask_w-rw_h)
    # print(img_y-rh_h+ym, img_y+(mask_h-rh_h)+ym)
    # print(img_x-rw_h+xm, img_x+(mask_w-rw_h)+xm)
    # print(img1[img_y-rh_h+ym:img_y+(mask_h-rh_h)+ym, img_x-rw_h+xm:img_x+(mask_w-rw_h)+xm, c].shape, (1-mask).shape)
    # print(img1.shape)
    # print(img2.shape, img_rs.shape)
    print('img_rs: ', img_rs.shape)

    img_sum1 = img_rs[:,:,c]*mask
    img_sum2 = img1[img_y-rh_h+ym:img_y+(mask_h-rh_h)+ym, img_x-rw_h+xm:img_x+(mask_w-rw_h)+xm, c]*(1-mask)
    img1[img_y-rh_h+ym:img_y+(mask_h-rh_h)+ym, img_x-rw_h+xm:img_x+(mask_w-rw_h)+xm, c]=(img_sum1+img_sum2).astype(np.uint8)


nose_img = cv2.imread('./img/nose150.png',cv2.IMREAD_UNCHANGED)
LEar_img = cv2.imread('./img/left_ear80.png',cv2.IMREAD_UNCHANGED)
REar_img = cv2.imread('./img/right_ear80.png',cv2.IMREAD_UNCHANGED)

cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            break

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.detections:
            face_box = results.detections[0].location_data.relative_bounding_box
            face_box = (int(face_box.xmin*image.shape[1]), 
                        int(face_box.ymin*image.shape[0]), 
                        int((face_box.xmin+face_box.width)*image.shape[1]), 
                        int((face_box.ymin+face_box.height)*image.shape[0]))
            image = cv2.rectangle(image, (face_box[0],face_box[1]), (face_box[2],face_box[3]), (0,0,255), 3)

            nose_x = results.detections[0].location_data.relative_keypoints[2].x
            nose_y = results.detections[0].location_data.relative_keypoints[2].y
            LEar_x = results.detections[0].location_data.relative_keypoints[-1].x
            LEar_y = results.detections[0].location_data.relative_keypoints[-1].y
            REar_x = results.detections[0].location_data.relative_keypoints[-2].x
            REar_y = results.detections[0].location_data.relative_keypoints[-2].y

            for c in range(3):
                print('face_box: ', face_box)
                imgSumByXY(image, nose_img, c, nose_x, nose_y, 0, 0, face_box[2], face_box[3])
                imgSumByXY(image, LEar_img, c, LEar_x, LEar_y, 0, 0, face_box[2], face_box[3])
                imgSumByXY(image, REar_img, c, REar_x, REar_y, 0, 0, face_box[2], face_box[3])

        cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()













