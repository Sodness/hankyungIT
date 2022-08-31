'''
# -----------------------------------------
# Frame
# -----------------------------------------

1. 프레임 생성
- frame_burger=Frame(root, relief='solid', bd=1)
    - 제목이 없는 프레임(Frame)
    - relief='solid' : 테두리 종류 (flat, groove, raised, ridge, solid, sunken)
    - bd=1 : 테두리 두께
- frame_drink=LabelFrame(root, text='음료')
    - 제목이 있는 프레임(LabelFrame)

2. Frame 위치 와 옵션
- frame_drink.pack(side='right', fill='both',expand=True)
   - side='right' : 위치 (top, bottom, left, right)
   - fill='both': 크기 맞춤 (none, x, y, both)
   - expand=True : 공간을 확장


# -----------------------------------------
# 1. 프레임 생성
# -----------------------------------------
from tkinter import *
root=Tk()
root.title('test')
root.geometry('640x480')

#-------------프레임 1---------------------
frame_burger=Frame(root, relief='solid', bd=1)
frame_burger.pack()

Button(frame_burger,text='햄버거').pack() #frame_burger 프레임에 버튼을 적용
Button(frame_burger,text='불고기햄버거').pack()
Button(frame_burger,text='새우햄버거').pack()

#-------------프레임 2---------------------
frame_drink=LabelFrame(root, text='음료')
Button(frame_drink,text='아이스아메리카노').pack()
Button(frame_drink,text='콜라').pack()
frame_drink.pack()
root.mainloop()
'''

# -----------------------------------------
# 2. Frame 위치 와 옵션
# frame_drink.pack(side='right', fill='both',expand=True)
# side='right' : 위치 (top, bottom, left, right)
# fill='both': 크기 맞춤 (none, x, y, both)
# expand=True : 공간을 확장
# -----------------------------------------

from tkinter import *
root=Tk()
root.title('test')
root.geometry('640x480')

# 레이블
lbl=Label(root,text='메뉴를 선택해 주세요')
lbl.pack(side='top')
# 주문하기 버튼
Button(root, text='주문하기').pack(side='bottom')
#-------------프레임 1---------------------
frame_burger=Frame(root, relief='solid', bd=1)
frame_burger.pack(side='left',fill='both', expand=True)

Button(frame_burger,text='햄버거').pack() #frame_burger 프레임에 버튼을 적용
Button(frame_burger,text='불고기햄버거').pack()
Button(frame_burger,text='새우햄버거').pack()

#-------------프레임 2---------------------
frame_drink=LabelFrame(root, text='음료')
Button(frame_drink,text='아이스아메리카노').pack()
Button(frame_drink,text='콜라').pack()
frame_drink.pack(side='right', fill='both', expand=True)

root.mainloop()