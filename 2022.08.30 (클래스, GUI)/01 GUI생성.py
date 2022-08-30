# -----------------------------------------------------------
# Tkinter GUI
# https://076923.github.io/posts/Python-tkinter-1/
# -----------------------------------------------------------

import tkinter

window=tkinter.Tk()

window.title('test')
window.geometry('640x640')
window.resizable(True,False)

label=tkinter.Label(window,text='안녕하세요')
label.pack()

window.mainloop()