'''
# --------------------------------------------------------------------
# grid을 이용하여 위젯들을 배치할 수 있습니다.
#
# [grid 옵션]
# - sticky=N+E+W+S, padx=3, pady=3 : 할당된 공간내에서 동서남북으로 모두 확장
# - padx=3, pady=3 : 좌우(padx), 상하(pady) 여백
# - [참고] 버튼 상하여백은 Button메서드에 옵선을 지정함(width=5,height=2 )
#---------------------------------------------------------------------

# -------------------------------------
# 1. pack VS grid
# -------------------------------------
from tkinter import *
root=Tk()
root.title('test')
root.geometry('640x480')
button1=Button(root, text='버튼1')
button2=Button(root, text='버튼2')

# pack 경우
# button1.pack(side='left')
# button2.pack(side='right')

#grid
button1.grid(row=0, column=0)
button2.grid(row=1, column=1)
root.mainloop()


# ------------------------------------------
# 2. 숫자 키패드 만들기 (위젯만 배치)
# ------------------------------------------
from tkinter import *
root=Tk()
root.title('test')
root.geometry('640x480')

# 1줄
btn_f16=Button(root, text='F16')
btn_f17=Button(root, text='F17')
btn_f18=Button(root, text='F18')
btn_f19=Button(root, text='F19')

btn_f16.grid(row=0, column=0)
btn_f17.grid(row=0, column=1)
btn_f18.grid(row=0, column=2)
btn_f19.grid(row=0, column=3)

# 2줄
btn_7=Button(root, text='7')
btn_8=Button(root, text='8')
btn_9=Button(root, text='9')
btn_sub=Button(root, text='-')

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_sub.grid(row=1, column=3)

# 3줄
btn_4=Button(root, text='4')
btn_5=Button(root, text='5')
btn_6=Button(root, text='6')
btn_add=Button(root, text='_')

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_add.grid(row=2, column=3)


# 4줄
btn_1=Button(root, text='1')
btn_2=Button(root, text='2')
btn_3=Button(root, text='3')
btn_enter=Button(root, text='enter')

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_enter.grid(row=3, column=3, rowspan=2) # 현재 위치에서 아래쪽으로 몇 줄을 합함

# 5줄
btn_0=Button(root, text='0')
btn_point=Button(root, text='.')


btn_0.grid(row=4, column=0, columnspan=2) #현재 위치에서 오른쪽으로 몇 칸 합함
btn_point.grid(row=4, column=2)
root.mainloop()
'''

# ------------------------------------------
# 3. 숫자 키패드 만들기2 (위젯만 배치)
# - sticky=N+E+W+S, padx=3, pady=3 : 할당된 공간내에서 동서남북으로 모두 확장
# - padx=3, pady=3 : 좌우(padx), 상하(pady) 여백
# - [참고] 버튼 상하여백은 Button메서드에 옵선을 지정함(width=5,height=2 )
# ------------------------------------------
from tkinter import *
root=Tk()
root.title('test')
root.geometry('640x480')

# 1줄
btn_f16=Button(root, text='F16', width=5,height=2)
btn_f17=Button(root, text='F17', width=5,height=2)
btn_f18=Button(root, text='F18', width=5,height=2)
btn_f19=Button(root, text='F19', width=5,height=2)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0, column=1,sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2,sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3,sticky=N+E+W+S,  padx=3, pady=3)

# 2줄
btn_7=Button(root, text='7', width=5,height=2)
btn_8=Button(root, text='8', width=5,height=2)
btn_9=Button(root, text='9', width=5,height=2)
btn_sub=Button(root, text='-', width=5,height=2)

btn_7.grid(row=1, column=0,sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=1, column=1,sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=1, column=2,sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=1, column=3,sticky=N+E+W+S, padx=3, pady=3)

# 3줄
btn_4=Button(root, text='4', width=5,height=2)
btn_5=Button(root, text='5', width=5,height=2)
btn_6=Button(root, text='6', width=5,height=2)
btn_add=Button(root, text='_', width=5,height=2)

btn_4.grid(row=2, column=0,sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=2, column=1,sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=2, column=2,sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=2, column=3,sticky=N+E+W+S, padx=3, pady=3)


# 4줄
btn_1=Button(root, text='1', width=5,height=2)
btn_2=Button(root, text='2', width=5,height=2)
btn_3=Button(root, text='3', width=5,height=2)
btn_enter=Button(root, text='enter', width=5,height=2)

btn_1.grid(row=3, column=0,sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=3, column=1,sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=3, column=2,sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=3, column=3, rowspan=2,sticky=N+E+W+S, padx=3, pady=3) # 현재 위치에서 아래쪽으로 몇 줄을 합함

# 5줄
btn_0=Button(root, text='0', width=5,height=2)
btn_point=Button(root, text='.', width=5,height=2)


btn_0.grid(row=4, column=0, columnspan=2,sticky=N+E+W+S, padx=3, pady=3) #현재 위치에서 오른쪽으로 몇 칸 합함
btn_point.grid(row=4, column=2,sticky=N+E+W+S, padx=3, pady=3)
root.mainloop()