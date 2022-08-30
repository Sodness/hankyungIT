import tkinter

window=tkinter.Tk()
window.title('test')
window.geometry('640x640')

label=tkinter.Label(window,text='파이썬',width=10, height=5, fg='red',relief='solid')
label.pack()

window.mainloop()