'''
label은 "글자"나 "이미지"를 보여주는 것으로 실제로 동작을 실행하는 것은 아니다.

#---------------------------------------
# 1. label에 텍스트 나타내기
#---------------------------------------

import tkinter

window=tkinter.Tk()
window.title('test')
window.geometry('640x480')

label1=tkinter.Label(window, text='안녕하세요')
label1.pack()

window.mainloop()



#---------------------------------------
# 2. label에 이미지 나타내기
# 1) photo=tkinter.PhotoImage(file='이미지명')로 이미지 불러오고
# 2) Label(root, image=photo) 지정함
#---------------------------------------
import tkinter

window=tkinter.Tk()
window.title('test')
window.geometry('640x480')

photo=tkinter.PhotoImage(file='./img01.png')
label=tkinter.Label(window, image=photo)
label.pack()

window.mainloop()

# ---------------------------------------------------
# 3. [실습1]버튼을 만들어 label1의 메시지 내용 바꾸기 (config())
# ---------------------------------------------------

import tkinter

window=tkinter.Tk()
window.title('test')
window.geometry('640x480')

def change():
    label.config(text='클릭했습니다.')
    pass
label = tkinter.Label(window, text='안녕하세요')
label.pack()

btn1=tkinter.Button(window, text='클릭', command=change)
btn1.pack()

window.mainloop()
'''

# ---------------------------------------------------
# 4. [실습2]버튼을 만들어 label의 메시지와 이미지를 한번에 바꾸기
# * 주의: 함수 안에 변수는 전역변수를 사용함(global 변수)
# ---------------------------------------------------
import tkinter
window=tkinter.Tk()
window.title('test')
window.geometry('640x480')

def change():
    label1.config(text='또 만나요')
    global photo2
    photo2=tkinter.PhotoImage(file='./img02.png')
    label2.config(image=photo2)

label1=tkinter.Label(window, text='안녕하세요')
label1.pack()

photo=tkinter.PhotoImage(file='./img01.png')
label2=tkinter.Label(window, image=photo)
label2.pack()

btn1=tkinter.Button(window, text='클릭', command=change)
btn1.pack()

window.mainloop()

