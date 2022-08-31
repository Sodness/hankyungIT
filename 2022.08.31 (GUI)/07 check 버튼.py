'''
### Checkbox  (Checkbutton)
- 변수=IntVar() :체크박스는 체크 여부를 확인할 변수가 꼭 필요함
- chkbox=Checkbutton(root, text='메시지', variable=변수)
    -  variable=변수 -> 체크 여부를 저장 받을 변수 필요함
- 체크박스 메서드
    - chkbox.select()  :  자동 선택처리
    - chkbox.deselect()  : 선택 해제
- 체크박스 선택여부 값 가져오기(get())
    - 체크 여부를 저장 받은 변수를 통해 값을 가져올 수 있다.
    - 변수.get() : 0->체크 해제, 1-> 체크 선택


[참고] 파이썬 tkinter 변수값 가져오기(StringVar, IntVar, DoubleVar, BooleanVar)
 tkinter에서 만일 텍스트 박스에 텍스트를 입력하고 해당 입력값을 이용하고 싶을 때
 그냥 일반 파이썬으로 하듯이 변수를 가져오면 에러가 발생합니다.
 변수 선언은 tkinter에서 제공하는 함수를 사용해서 선언해야 합니다.
    - StringVar : string 변수를 선언
    - IntVar : Integer (정수) 변수를 선언
    - DoubleVar : float (실수) 변수를 선언
    - BooleanVar : True Flase 변수를 선언

# ------------------------------------------------
# 1. 체크박스 생성
# -------------------------------------------------
from tkinter import *
root=Tk()
root.title('test')
root.geometry('640x480')

#체크박스 생성
chkvar=IntVar() #체크여부 확인할 변수, 0-> 선택 x, 1-> 선택 0
chkbox=Checkbutton(root, text='오늘 하루동안 보지 않기', variable=chkvar)
chkbox.pack()
root.mainloop()


# ------------------------------------------------
# 2. 버튼을 눌러 체크 박스 선택여부 값 가져오기
#  - 체크박스 선택 여부 값 가져오기(get())
#     - 체크 여부를 저장 받은 변수를 통해 값을 가져올 수 있다.
#     - 변수.get() : 0->체크 해제, 1-> 체크 선택
# -------------------------------------------------

from tkinter import *

root=Tk()
root.title('test')
root.geometry('640x480')

def btncmd():
    print(chkvar.get())

#체크박스 생성
chkvar=IntVar()
chkbox=Checkbutton(root, text='오늘 하루동안 보지 않기', variable=chkvar)
chkbox.pack()

#버튼 생성
btn=Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()
'''

# ------------------------------------------------
# 3. 2개의 체크 박스에서  선택 여부 값 가져오기
# ------------------------------------------------
from tkinter import *
root=Tk()
root.title('test')
root.geometry('640x480')

def btncmd():
    print(chkvar1.get())
    print(chkvar2.get())

# 체크박스1 생성
chkvar1=IntVar()
chkbox1=Checkbutton(root, text='오늘 하루 그만 보기', variable=chkvar1)
chkbox1.pack()

# 체크박스2 생성
chkvar2= IntVar()
chkbox2=Checkbutton(root, text='일주일동안 그만 보기', variable=chkvar2)
chkbox2.pack()

# 버튼 생성
btn=Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()
