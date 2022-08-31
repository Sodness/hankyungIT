'''
# --------------------------------------------------------------------
# Combobox() : 텍스트와 허용된 값의 드롭다운 목록을 표시하는 콤보 박스
# --------------------------------------------------------------------
- import tkinter.ttk as ttk
    - 콤보박스는 별도의 모듈을 import해야 함

- combox=ttk.Combobox(root, height=5, values=변수, state='readonly')
    - 콤보박스는 tkinter.ttk에 있음 (import tkinter.ttk as ttk)
    - height=5 : 최초 목록이 5개만 보여짐
    - values=변수 : 콤보 박스의 내용을 지정함
        * ex) 변수 =[str(i) + '일' for i in range(1,32)]
    - 목록 이외의 값은 입력 못하게 하려면 state='readonly' 속성을 지정함
- 콤보박스 메서드
    - combox.set('카드 결제일') : 콤보박스 최초 목록 제목 설정 및 기본값 지정할 수 있음
    - readonly_combobox.current(0): 기본값 설정

- 콤보박스 값 가져오기(get())
- 목록 이외의 값은 입력 못하게 하는 콤보박스 만들기(state='readonly')

# --------------------------------------------
# 1. 콤보 박스 생성
# --------------------------------------------
import tkinter.ttk as ttk
from tkinter import *

root=Tk()
root.title('test')
root.geometry('640x480')

# 콤보박스 생성
vlues=[str(i)+'월' for i in range(1,13)] #1월~12월까지 지정
combox=ttk.Combobox(root, height=5, values=vlues)
combox.set('월 선택') # 콤보박스 기본값 설정
combox.pack()

root.mainloop()
'''

# --------------------------------------------
# 2. 콤보 박스 생성하고 값 가져오기
# --------------------------------------------

import tkinter.ttk as ttk
from tkinter import *

root=Tk()
root.title('test')
root.geometry('640x480')

def btncmd():
    print(combox.get())
    print(combox2.get())

# 콤보박스 생성
vlues=[str(i)+'월' for i in range(1,13)] #1월~12월까지 지정
combox=ttk.Combobox(root, height=5, values=vlues)
combox.set('월 선택') # 콤보박스 기본값 설정
combox.pack()

# 콤보박스2 생성
vlue_days=[str(i)+'일' for i in range(1,32)] #1일~31일까지 지정
combox2=ttk.Combobox(root, height=10, values=vlue_days, state='readonly')
combox2.set('1일') #기본값 설정
combox2.pack()

#버튼 생성
btn=Button(root, text='선택', command=btncmd)
btn.pack()

root.mainloop()