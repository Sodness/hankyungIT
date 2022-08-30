from tkinter import *

class App:
    def __init__(self):
        self.items=['국어','영어','수학','과학']
        self.root=Tk()
        self.root.title('test')
        self.root.geometry('300x200')

        #listbox 생성
        self.listbox=Listbox(self.root,selectmode='extended', height=0)
        for item in self.items:
            self.listbox.insert(END,item)
        #button 생성
        self.btn=Button(self.root, text='삭제', command=self.delete)

        self.listbox.pack()
        self.btn.pack()

        self.root.mainloop()

    def delete(self):
        self.selection =self.listbox.curselection()
        self.n=self.selection[len(self.selection)]
        for i in range(len(self.selection)):
            print('delete', self.n, ' ', self.listbox.get(self.n))
            self.listbox.delete(self.n)
            self.listbox.update() # for문 동작할때마다 GUI가 업데이트 됨


if __name__=='__main__':
    App()