'''
# ------------------------------------------
# Scrollbar
# ------------------------------------------
- 스크롤바와 연결된 위젯은 하나의 프레임에 넣는 것이 관리가 편함
- 스크롤바와 연결된 위젯은 각각 서로를 매핑해야함
    - 리스트 박스: listbox=Listbox(frame, selectmode='extended', height=10, yscrollcommand=scrollbar.set)
        - yscrollcommand=scrollbar.set
    - 스크롤바: scrollbar.config(command=listbox.yview)

'''
from tkinter import *
root=Tk()
root.title('test')
root.geometry('640x480')
# 프레임 생성
frame=Frame(root)
frame.pack()
# scrollbar 만들기
scrollbar=Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

# listbox만들기(1일~31일까지 10줄씩 보이게 만듦)
listbox=Listbox(frame,height=10, selectmode='extended', yscrollcommand=scrollbar.set)
for i in range(1,32):
    listbox.insert(END,str(i)+'일')
listbox.pack(side='left')

scrollbar.config(command=listbox.yview) # scrollbar에 listbox를 세로(y)방향으로 붙임
root.mainloop()
