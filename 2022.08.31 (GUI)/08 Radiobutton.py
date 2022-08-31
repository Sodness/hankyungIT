'''
# -----------------------------------------------------------------------
# Radiobutton : 여러 옵션 중에 하나만 선택
# -----------------------------------------------------------------------
- 변수 지정 : 선택한 옵션을 저장할 변수 꼭 필요함
    - 변수=IntVar() #int형으로 값을 저장함, 선택한 옵션을 값(index)를 저장함
    - 변수=StringVar() #문자형으로 값을 저장함, 선택한 옵션을 값(문자,string)을 저장함. 저장할 변수 꼭 필요함

- btn_burger1=Radiobutton(root, text='햄버거', value=1, variable=변수)
    - value=1 : value 속성이 반드시 있어야함. 선택했을 때 입력되는 값임
    - variable=변수 : 라디오 단추가 선택되었을 때 값을 담을 변수 필요함

[라디오 단추 메서드]
btn_burger1.select() : 기본값 선택

# ------------------------------------------
# 1. Radiobutton 생성
# ------------------------------------------

from tkinter import *
root=Tk()
root.title('test')
root.geometry('640x480')

#레이블 생성
lbl=Label(root, text='메뉴를 선택해 주세요')
lbl.pack()

def btncmd():
    pass

#라디오단추 생성
menu_var=IntVar()
opt1=Radiobutton(root, text='햄버거', value=1, variable=menu_var)
opt1.select() # 기본 선택 지정
opt2=Radiobutton(root, text='불고기햄버거', value=2, variable=menu_var)
opt3=Radiobutton(root, text='치킨햄버거', value=3, variable=menu_var)
opt1.pack()
opt2.pack()
opt3.pack()

# 버튼 생성
btn=Button(root, text='주문', command=btncmd)
btn.pack()

root.mainloop()



# ------------------------------------------
# 2. 라디오 버튼 선택한 값 가져오기
# ------------------------------------------
from tkinter import *
root=Tk()
root.title('test')
root.geometry('640x480')

#레이블 생성
lbl=Label(root, text='메뉴를 선택해 주세요')
lbl.pack()

def btncmd():
    print(menu_var.get())

#라디오단추 생성
menu_var=IntVar()
opt1=Radiobutton(root, text='햄버거', value=1, variable=menu_var)
opt1.select() # 기본 선택 지정
opt2=Radiobutton(root, text='불고기햄버거', value=2, variable=menu_var)
opt3=Radiobutton(root, text='치킨햄버거', value=3, variable=menu_var)
opt1.pack()
opt2.pack()
opt3.pack()

# 버튼 생성
btn=Button(root, text='주문', command=btncmd)
btn.pack()

root.mainloop()
'''
# -------------------------------------------------------------------
# 3. 2개 그룹 라디오 단추 생성하여 각각 값 가져오기
# -------------------------------------------------------------------
# - 변수 지정 : 선택한 옵션을저장할 변수 꼭 필요함
#    - 변수=IntVar() # int형으로 값을 저장함, 선택한 옵션을 값(index)를 저장함
#    - 변수=StringVar() # 문자형으로 값을 저장함, 선택한 옵션을 값(문자,string)을 저장함.
#       저장할 변수 꼭 필요함
#
# - btn_burger1=Radiobutton(root, text='햄버거', value=1, variable=변수)
#    - value=1 : value 속성이 반드시 있어야 함. 선택했을 때 입력되는 값임
#    - variable=변수 : 라디오 단추가 선택 되었을 때 값을 담을 변수 필요함
# --------------------------------------------------------------------
from tkinter import *
root=Tk()
root.title('test')
root.geometry('640x480')

#레이블 생성
lbl=Label(root, text='메뉴를 선택해 주세요')
lbl.pack()

def btncmd():
    print(menu_var.get())
    print(drink_var.get())

#라디오단추1 생성
menu_var=IntVar()
opt1=Radiobutton(root, text='햄버거', value=1, variable=menu_var)
opt1.select() # 기본 선택 지정
opt2=Radiobutton(root, text='불고기햄버거', value=2, variable=menu_var)
opt3=Radiobutton(root, text='치킨햄버거', value=3, variable=menu_var)
opt1.pack()
opt2.pack()
opt3.pack()

#레이블2생성
lbl2=Label(root, text='음료를 선택해 주세요')
lbl2.pack()
#라디오단추2 생성
drink_var=StringVar()
drink1=Radiobutton(root, text='아메리카노', value='아메리카노', variable=drink_var)
drink1.select()
drink2=Radiobutton(root, text='콜라', value='콜라', variable=drink_var)
drink1.pack()
drink2.pack()


# 버튼 생성
btn=Button(root, text='주문', command=btncmd)
btn.pack()

root.mainloop()