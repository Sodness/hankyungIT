import cv2
import numpy as np


top = (0,0)
bottom = (0,0)

def drawRectangle(action, x, y, flags, *userdata):
    # 이벤트 받고 나갈 때 top 변수가 소멸됨, bottom은 빼도 동작하는데 세트여서 그냥 넣어주고
    global top, bottom
    
    # 마우스 왼쪽 DOWN
    if action == cv2.EVENT_LBUTTONDOWN:
        top=(x,y)
    # 마우스 왼쪽 UP
    elif action == cv2.EVENT_LBUTTONUP:
        bottom=(x,y)
        cv2.rectangle(image, top, bottom, (0, 255, 0), 2, 8)
        w=abs(bottom[0]-top[0]) #사각형 가로 크기
        h=abs(bottom[1]-top[1]) #사각형 세로 크기
        # 나비 사각형 크기 맞춰서 바꾸기
        tmp=cv2.resize(image2,(w,h))
        # 마스크 0~255를 0~1로 비율 맞추기
        mask_img=tmp[:,:,3]/255

        # RGB 채널별로 나눠서 이미지 합성
        # 내 코드는 얕은복사 인줄 알고 target_area 바꾸고 image도 바뀔줄 잘못알았던 거
        for c in range(3):
            img_sum1 = tmp[:,:,c]*mask_img
            img_sum2 = image[top[1]:bottom[1],top[0]:bottom[0],c]*(1-mask_img)
            image[top[1]:bottom[1],top[0]:bottom[0],c]=(img_sum1+img_sum2).astype(np.uint8)
        cv2.imshow("Window", image)
            

# 이미지 읽기
image = cv2.imread("./lenna.jpg")
temp = image.copy()
image2 = cv2.imread('./navi.png',cv2.IMREAD_UNCHANGED)
# 이미지 확인
print(np.shape(image2))

# Window 창 생성
cv2.namedWindow("Window")
# Window 창 마우스이벤트 함수 지정 -> drawRectangle
cv2.setMouseCallback("Window", drawRectangle)

k = 0
# 'q' 입력시 종료
while k != 113:
    cv2.imshow("Window", image)
    k = cv2.waitKey(0)
    
    # 'c' 입력시 이미지 초기화
    if (k == 99):
        image = temp.copy()
        cv2.imshow("Window", image)


cv2.destroyAllWindows()