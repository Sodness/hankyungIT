# a=3
# b=4
# c=a+b
# print(c)

#-----------------------------------
# import tkinter

# windows = tkinter.Tk()
# windows.title('지금은 연습중')
# windows.geometry('640x480')
# windows.resizable(False, True)
# windows.mainloop()

#-----------------------------------
# import tkinter
#
# windows = tkinter.Tk()
# windows.title('test')
# windows.geometry('640x480')
#
# lbl = tkinter.Label(windows, text='안녕하세요')
# lbl.pack()
#
# windows.mainloop()

#-----------------------------------
# import tkinter
#
# windows = tkinter.Tk()
# windows.title('test')
# windows.geometry('640x480')
#
# photo = tkinter.PhotoImage(file='./img01.png')
# lbl = tkinter.Label(windows, image=photo)
# lbl.pack()
#
# windows.mainloop()

#-----------------------------------
# import tkinter
#
# windows = tkinter.Tk()
# windows.title('test')
# windows.geometry('640x480')
#
# def change():
#     lbl.config(text='클릭했습니다.')
#
# lbl = tkinter.Label(windows, text='안녕하세요.')
# lbl.pack()
# btn = tkinter.Button(windows, text='클릭', command=change)
# btn.pack()
#
# windows.mainloop()

#-----------------------------------
# import tkinter
#
# window = tkinter.Tk()
# window.title('test')
# window.geometry('640x480')
#
# def change():
#     lbl1.config(text='또 만나요.')
#     global photo2
#     photo2 = tkinter.PhotoImage(file='./img02.png')
#     lbl2.config(image=photo2)
#
# def change1():
#     lbl1.config(text='또 만나요.')
#     lbl2.img = tkinter.PhotoImage(file='./img02.png')
#     lbl2.config(image=lbl2.img)
#
# lbl1 = tkinter.Label(window, text='안녕하세요.')
# lbl1.pack()
# photo = tkinter.PhotoImage(file='./img01.png')
# # photo2 = tkinter.PhotoImage(file='./img02.png')
# lbl2 = tkinter.Label(window, image=photo)
# lbl2.pack()
# btn = tkinter.Button(window, text='클릭', command=change)
# btn.pack()
#
# window.mainloop()

#-----------------------------------
# import tkinter
#
# window = tkinter.Tk()
# window.title('test')
# window.geometry('640x480')
#
# btn1 = tkinter.Button(window, text='버튼1', padx=10, pady=5).pack()
# btn2 = tkinter.Button(window, text='버튼2', padx=5, pady=10).pack()
# btn3 = tkinter.Button(window, text='버튼3', padx=10, pady=5, width=10, height=5).pack()
# btn4 = tkinter.Button(window, text='버튼4', width=4, height=5, bg='red', fg='yellow').pack()
#
# window.mainloop()

#-----------------------------------
# import tkinter
#
# window = tkinter.Tk()
# window.title('test')
# window.geometry('640x480')
#
# photo = tkinter.PhotoImage(file='./img01.png')
# btn = tkinter.Button(window, image=photo).pack()
#
# window.mainloop()

#-----------------------------------
# import tkinter
#
# window = tkinter.Tk()
# window.title('test')
# window.geometry('640x480')
#
# def countUp():
#     global cnt
#     cnt = lb['text']
#     cnt = int(cnt)
#     cnt = cnt + 1
#     lb.config(text=str(cnt))
#
# lb = tkinter.Label(window, text='0')
# # print(lb['text'])
# lb.pack()
# btn = tkinter.Button(window, text='증가', width=10, command=countUp)
# btn.pack()
#
# window.mainloop()

#-----------------------------------
# import tkinter as tk
#
# window = tk.Tk()
# window.title('test')
# window.geometry('640x480')
# cnt = 0
#
# def cntUp():
#     global cnt
#     cnt = cnt + 1
#     # lb.config(text=f'버튼 클릭 횟수: {cnt}') # 이것도 됨
#     lb['text'] = f'버튼 클릭 횟수: {cnt}'
#
# def reset():
#     global cnt
#     cnt = 0
#     lb.config(text='리셋되어짐: 0')
#
# lb = tk.Label(window, text='아직 출력되지 않았음')
# lb.pack()
# btn1 = tk.Button(window, text='증가', command=cntUp)
# btn1.pack()
# btn2 = tk.Button(window, text='리셋', command=reset)
# btn2.pack()
#
# window.mainloop()

#-----------------------------------
# import tkinter as tk
#
# class App:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.title('test')
#         self.window.geometry('640x480')
#
#         self.run()
#
#         self.window.mainloop()
#
#     def printStr(self):
#         print(self.btn['text'])
#
#     def run(self):
#         self.lb = tk.Label(self.window, text='레이블 예제')
#         self.lb.pack()
#         self.btn = tk.Button(self.window, text='레이블값 읽기', command=self.printStr)
#         self.btn.pack()
#
# if __name__ == '__main__':
#     App()

#-----------------------------------
# import tkinter as tk
#
# def btncmd():
#     # print(text.get('1.0', 'end')) # 이것도 됨
#     print(text.get('1.0', tk.END))
#     print(e.get())
#
#
# window = tk.Tk()
# window.title('test')
# window.geometry('640x480')
#
# text = tk.Text(window, width=30, height=5)
# text.pack()
# text.insert('current', '글자를 입력하세요.\n')
# text.insert('current', '안녕하세요 홍길동입니다.')
#
# e = tk.Entry(window, width=30)
# e.pack()
# e.insert(0, '글자를 한 줄만 입력하세요.')
#
# btn = tk.Button(window, text='클릭', command=btncmd)
# btn.pack()
#
# window.mainloop()

#-----------------------------------
# import tkinter as tk
# import time
#
# window = tk.Tk()
# window.title('test')
# window.geometry('640x480')
#
# listbox = tk.Listbox(window, selectmode='extended', height=0)
# listbox.pack()
# listbox.insert(0, '항목1')
# listbox.insert(1, '항목2')
# listbox.insert(tk.END, '항목3')
# listbox.insert(tk.END, '항목4')
# listbox.insert(tk.END, '항목5')
#
# time.sleep(3)
# listbox.delete(0,2)
#
# window.mainloop()

#-----------------------------------
# import tkinter as tk
#
# def btncmd():
#     print('총 항목 갯수:', listbox.size())
#     print('첫 번째 항목 명칭:', listbox.get(0))
#     print('1~3번까지 항목 가져오기:', listbox.get(0, 2))
#     print('모든 항목이름은:', listbox.get(0, tk.END))
#     print('사용자가 선택한 항목 index:', listbox.curselection())
#     print('사용자가 선택한 항목:', [listbox.get(i) for i in listbox.curselection()])
#
# window = tk.Tk()
# window.title('test')
# window.geometry('640x480')
#
# listbox = tk.Listbox(window, selectmode='extended', height=0)
# listbox.pack()
# listbox.insert(0, '항목1')
# listbox.insert(1, '항목2')
# listbox.insert(tk.END, '항목3')
# listbox.insert(tk.END, '항목4')
# listbox.insert(tk.END, '항목5')
#
# btn = tk.Button(window, text='클릭', command=btncmd)
# btn.pack()
#
# window.mainloop()

#-----------------------------------
import tkinter as tk

class App:
    def __init__(self):
        self.items = ['국어', '영어', '수학', '과학']
        self.root = tk.Tk()
        self.root.title('test')
        self.root.geometry('640x480')

        self.listbox = tk.Listbox(self.root, selectmode='extended', height=0)
        for idx, item in enumerate(self.items):
            self.listbox.insert(idx, item)
        self.listbox.pack()

        self.btn = tk.Button(self.root, text='삭제', command=self.btncmd)
        self.btn.pack()

        self.root.mainloop()

    def btncmd(self):
        selected = self.listbox.curselection()
        cnt = 0
        for i in selected:
            self.listbox.delete(i-cnt)
            self.listbox.update()
            cnt = cnt + 1

if __name__=='__main__':
    App()
#-----------------------------------


#-----------------------------------


#-----------------------------------








