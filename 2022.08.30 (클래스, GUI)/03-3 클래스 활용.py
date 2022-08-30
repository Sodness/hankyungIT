import tkinter

class App():
    def __init__(self):
        self.window=tkinter.Tk()
        self.window.title('test')
        self.window.geometry('200x80')

        self.lbl=tkinter.Label(self.window,text='레이블 예제')
        self.lbl.pack()

        self.btn=tkinter.Button(self.window, text='레이블값 읽기',
                                command=self.readLabelText)
        self.btn.pack()
        self.window.mainloop()

    def readLabelText(self):
        print(self.lbl['text'])



if __name__=='__main__':
    App()