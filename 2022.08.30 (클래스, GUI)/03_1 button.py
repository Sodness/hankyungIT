'''
-----------------------------
# 1. 기본 버튼 만들기
-----------------------------
import tkinter

window=tkinter.Tk()
window.title('test')

btn1=tkinter.Button(window,text='버튼1')
btn1.pack()

btn2=tkinter.Button(window,text='버튼2')
btn2.pack()

btn3=tkinter.Button(window,text='버튼2')
btn3.pack()

window.mainloop()

-------------------------------------------------------
# 2. 버튼 속성 (안쪽 여백, 버튼 크기, 글자색, 배경색 지정 등)
#    버튼 아쪽 좌우, 상하여백(padx,pady)
#    버튼 고정크기 지정(width, height)
#    버튼 배경색(bg), 글자색(fg) 지정
-------------------------------------------------------
import tkinter

window=tkinter.Tk()
window.title('test')

btn1=tkinter.Button(window,text='버튼1')
btn1.pack()

btn2=tkinter.Button(window,padx=10, pady=5, text='버튼2') # padx, pady
btn2.pack()

btn3=tkinter.Button(window, width=10,  height=5, text='버튼3')
btn3.pack()

btn4=tkinter.Button(window, fg='red', bg='yellow',text='버튼4')
btn4.pack()
window.mainloop()


#-------------------------------------------------
# 3.버튼에 이미지 채우기
#  1) photo=tkinter.PhotoImage(file='이미지명')로 이미지 불러오고
#  2) Button(root, image=photo) 지정함
#-------------------------------------------------

import tkinter
window=tkinter.Tk()
window.title('test')

photo=tkinter.PhotoImage(file='./img01.png')
btn=tkinter.Button(window, image=photo)
btn.pack()

window.mainloop()

#-------------------------------------------------
# 4. 버튼을 눌렀을 때 동작하기:이벤트 (command)
#-------------------------------------------------
import tkinter

window=tkinter.Tk()
window.title('test')

def btncmd():
    print('버튼을 클릭했습니다.')

btn=tkinter.Button(window, text='동작', command=btncmd)
btn.pack()

window.mainloop()
'''
