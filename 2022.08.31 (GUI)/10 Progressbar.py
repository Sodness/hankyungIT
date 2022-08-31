'''
# --------------------------------------------------
#  Progressbar
#  현재 진행 상황을 표시하는 프로그래스 바를 생성할 수 있습니다.
# --------------------------------------------------
- import tkinter.ttk as ttk
- progressbar=ttk.Progressbar(root, maximum=100, mode='indeterminate')
    - progressbar는 tkinter,ttk에 있음
    - maximum=100 : 100%까지 진행한다는 것
    - mode='indeterminate': 종료가 결정되지 않아 진행바가 왔다갔다 함.
    - mode='determinate' : 종료값을 maxium으로 한정함 (기본값임)
    - (추가) length=150 : progressbar의 길이 지정
- progressbar 메서드
    - progressbar.start(10) : 10초마다 진행, 이것을 넣어줘야 작동이 됨
    - progressbar.stop(): progressbar 작동 중단
    - progressbar.set(값) : progressbar의 값을 설정
    - progressbar.update(): progressbar 업데이트


# ---------------------------------
# 1. progressbar
# ---------------------------------

import tkinter.ttk as ttk
from tkinter import *
root=Tk()
root.title('test')
root.geometry('640x480')

# Progressbar 생성
pbar=ttk.Progressbar(root, maximum=100, mode='indeterminate') # 종료가 결정되어있지 않아 왔다갔다 함
pbar.start(10) #10초마다 진행, pbar.start(10)를 해야 진행됨
pbar.pack()
root.mainloop()


# ------------------------------------------------------------------------
#  2. progressbar를 작동시키고, mode='determinate', 중지버튼을 눌러 중지시킴
# ------------------------------------------------------------------------
import tkinter.ttk as ttk
from tkinter import *

root=Tk()
root.title('test')
root.geometry('640x480')

def btncmd():
    pbar.stop() # pbar 중지

# progressbar 생성
pbar=ttk.Progressbar(root, maximum=100, mode='determinate', length=150)
pbar.start(10)
pbar.pack()

# 중지버튼 생성
btn=Button(root, text='중지', command=btncmd)
btn.pack()

root.mainloop()
'''
# --------------------------------------------------------------------------------------------
#  3. 1) '시작'버튼을 눌러 progressbar를 작동시키고,
#     2) 진행상황이 보여지고
#     3) 진행이 완료되면 멈추고
#     4) 진행된 값을 화면 보여줌
# p_var=DoubleVar() # progressbar에 값을 지정할 변수 생성
# pbar=ttk.Progressbar(root, maximum=100,length=150, variable=p_var) # variable=p_var 지정함
# -----------------------------------------------------------------------------------------------

import tkinter.ttk as ttk
from tkinter import *
import time

root=Tk()
root.title('test')
root.geometry('640x480')

def btncmd():
    for i in range(1,101):
        time.sleep(0.01) # 너무 빨리 진행되어 0.01초 대기
        p_var.set(i)
        print(p_var.get())  # p_var 값 확인
        pbar.update() # 중간 진행과정이 보이지 않으므로, for문을 돌때마다 GUI를 업데이트 함


# Progressbar 생성: Progressba 객체 값을 셋팅할 변수 필요
p_var=DoubleVar()
pbar=ttk.Progressbar(root,maximum=100, length=150, variable=p_var)
pbar.pack()

#'시작'버튼 생성
btn=Button(root, text='시작', command=btncmd)
btn.pack()

root.mainloop()
'''
import time
import tkinter.ttk as ttk
from tkinter import *

root=Tk()
root.title('test')
root.geometry('640x480')

p_var=DoubleVar()
progressbar=ttk.Progressbar(root, maximum=100,length=150, variable=p_var)
progressbar.pack()

def btncmd():
    for i in range(1,101):
        time.sleep(0.01) # 0.01초 대기
        p_var.set(i) #progressbar의 값을 set함
        progressbar.update() #ui 업데이트
        print(p_var.get())
btn=Button(root, text='시작', command=btncmd)
btn.pack()
root.mainloop()
'''