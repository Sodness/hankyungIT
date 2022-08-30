import tkinter

window=tkinter.Tk()
window.title('test')
window.geometry('640x640')

count=0
def countUP():
    global count
    count += 1
    label.config(text=str(count))

label=tkinter.Label(window,text='0')
label.pack()



button=tkinter.Button(window, text='버튼', command=countUP,
                      overrelief='sunken', width=15,
                      repeatdelay=1000,
                      repeatinterval=100)

button.pack()

window.mainloop()