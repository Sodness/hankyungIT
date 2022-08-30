'''
# -------------------------------------------------------------------
##  Text, Entry 위젯
- Text : 여러줄 입력받을 수 있음
    - test.insert(END,'기본텍스트 입력')
- Entry : 한 줄 입력받을 수 있음, 로그인이나, 닉네임 입력받고자할때
# -------------------------------------------------------------------
'''

# ------------------------------------------------------
# 1. text 위젯 만들고 기본값 넣기
# insert메서드를 통해 text위젯의 초기 글자(기본값)를 나타나게 할 수 있다.
# --------------------------------------------------------
import tkinter

window=tkinter.Tk()
window.title('test')
window.geometry('640x480')

text=tkinter.Text(window, width=30, height=5)
text.pack()
text.insert('current', '글자를 입력하세요1\n')
text.insert('current','글자를 입력하세요2')

# ------------------------------------------------------
# 2.Entry 위젯 생성 -한줄 입력가능
# ------------------------------------------------------
e=tkinter.Entry(window,width=30)
e.insert(0,'한 줄만 입력하세요')
e.pack()


# ------------------------------------------------------
# 3.버튼을 누르면 Text나 Entry에 있는 값을 가져오거나(get) 지워보기
# 1) text와 entry의 텍스트 가져오기(get)
# 2) text와 entry값 삭제(delete)
# ------------------------------------------------------
def btncmd():
    print(text.get('1.0', tkinter.END))
    print(e.get())

    text.delete('1.0',tkinter.END)
    e.delete(0,tkinter.END)

btn=tkinter.Button(window,text='클릭', command=btncmd)
btn.pack()
window.mainloop()