#-----------------------------------
# from tkinter import *
#
# def btncmd():
#     print(chkvar.get())
#     print(chkvar2.get())
#
# root = Tk()
# root.title('test')
# root.geometry('640x480')
#
# chkvar = IntVar()
# chkbox = Checkbutton(root, text='오늘 하루동안 그만보기', variable=chkvar)
# chkbox.pack()
# chkvar2 = IntVar()
# chkbox2 = Checkbutton(root, text='일주일 동안 그만보기', variable=chkvar2)
# chkbox2.pack()
# btn = Button(root, text='클릭', command=btncmd)
# btn.pack()
#
# root.mainloop()

#-----------------------------------
# from tkinter import *
#
# def btncmd():
#     # global n
#     n = menu_var.get()
#     print('선택한 메뉴는:', n, '메뉴명:', main_menu_list[n], '가격:', main_menu_price[n])
#     print('선택한 음료는:', drink.get())
#
# root = Tk()
# root.title('test')
# root.geometry('640x480')
#
# main_menu_list = ['햄버거', '불고기버거', '치킨버거']
# main_menu_price = [4500, 5500, 6000]
# drink_ls = ['아메리카노', '콜라']
# drink_price_ls = [2000, 1500]
# # print(str(main_menu_price))
# menu_str = ' '.join(main_menu_list) + '\n' + ' '.join(str(main_menu_price)) + '\n' + ' '.join(drink_ls) + '\n' + ' '.join(str(drink_price_ls)) + '\n'
# menu_lb = Label(root, text=menu_str).pack()
#
# Label(root, text='메뉴를 선택해주세요.').pack()
# menu_var = IntVar()
# opt1 = Radiobutton(root, text='햄버거', value=0, variable=menu_var)
# opt1.select()
# opt1.pack()
# opt2 = Radiobutton(root, text='불고기버거', value=1, variable=menu_var)
# opt2.pack()
# opt3 = Radiobutton(root, text='치킨버거', value=2, variable=menu_var)
# opt3.pack()
#
# Label(root, text='음료를 선택해 주세요.').pack()
# drink = StringVar()
# d_opt1 = Radiobutton(root, text='아메리카노', value='아메리카노', variable=drink)
# d_opt1.select()
# d_opt1.pack()
# d_opt2 = Radiobutton(root, text='콜라', value='콜라', variable=drink)
# d_opt2.pack()
#
# btn = Button(root, text='주문', command=btncmd)
# btn.pack()
#
# root.mainloop()

#-----------------------------------
# import tkinter.ttk as ttk
# from tkinter import *
# import calendar
# from datetime import datetime
#
# def btncmd():
#     print(cmb1.get(), cmb2.get())
#
# def cmb1Cmd(e):
#     global cmb2
#     date = datetime(year=datetime.today().year, month=int(cmb1.get()[:1]), day=1).date()
#     last_day = calendar.monthrange(date.year, date.month)[1]
#     cmb2_value = [str(i) + '일' for i in range(1, last_day + 1)]
#     cmb2['values'] = cmb2_value
#     cmb2.update()
#
# root = Tk()
# root.title('test')
# root.geometry('640x480')
#
# cmb1_value = [str(i)+'월' for i in range(1,13)]
# cmb1 = ttk.Combobox(root, height=5, values=cmb1_value)
# cmb1.bind("<<ComboboxSelected>>", cmb1Cmd)
# cmb1.set('월 선택')
# cmb1.pack()
#
# date = datetime(year=datetime.today().year, month=datetime.today().month, day=1).date()
# last_day = calendar.monthrange(date.year, date.month)[1]
# cmb2_value = [str(i)+'일' for i in range(1,last_day+1)]
# cmb2 = ttk.Combobox(root, height=10, values=cmb2_value, state='readonly')
# cmb2.set('일 선택')
# cmb2.pack()
#
# btn = Button(root, text='선택', command=btncmd)
# btn.pack()
#
# root.mainloop()

#-----------------------------------
# import tkinter.ttk as ttk
# from tkinter import *
#
# def btncmd():
#     pbar.stop()
#
# root = Tk()
# root.title('test')
# root.geometry('640x480')
#
# pbar =ttk.Progressbar(root, maximum=100, mode='determinate')
# pbar.start(10)
# pbar.pack()
#
# btn = Button(root, text='중지', command=btncmd)
# btn.pack()
#
# root.mainloop()

#-----------------------------------
# import tkinter.ttk as ttk
# from tkinter import *
# import time
#
# def btncmd():
#     for i in range(1,101):
#         time.sleep(0.01)
#         pbar_value.set(i)
#         pbar.update()
#         print(pbar_value.get())
#
# root = Tk()
# root.title('test')
# root.geometry('640x480')
#
# pbar_value = DoubleVar()
# pbar =ttk.Progressbar(root, maximum=100, mode='determinate', variable=pbar_value, length=300)
# pbar.pack()
#
# btn = Button(root, text='시작', command=btncmd)
# btn.pack()
#
# root.mainloop()

#-----------------------------------
# from tkinter import *
#
# def new_cmd():
#     print('새 프로젝트를 선택했습니다.')
#
# root = Tk()
# root.title('test')
# root.geometry('640x480')
#
# menu = Menu(root)
# menu_file = Menu(menu, tearoff=False)
# menu_file.add_command(label='새 프로젝트', command=new_cmd)
# menu_file.add_command(label='새로만들기')
# menu_file.add_separator()
# menu_file.add_command(label='다시 실행', state='disabled')
# menu_file.add_separator()
# menu_file.add_command(label='종료', command=root.quit)
# menu.add_cascade(label='파일', menu=menu_file)
# root.config(menu=menu)
#
# menu_edit = Menu(menu, tearoff=False)
# menu.add_cascade(label='편집', menu=menu_edit)
#
# menu_language = Menu(menu, tearoff=False)
# menu_language.add_radiobutton(label='파이썬')
# menu_language.add_radiobutton(label='자바')
# menu_language.add_radiobutton(label='C++')
# menu.add_cascade(label='언어', menu=menu_language)
#
# menu_view = Menu(menu, tearoff=False)
# menu_view.add_checkbutton(label='탭 고정')
# menu_view.add_checkbutton(label='탭 표시')
# menu.add_cascade(label='보기', menu=menu_view)
#
# root.mainloop()

#-----------------------------------
# import tkinter.messagebox as msgbox
# from tkinter import *
#
# def info():
#     msgbox.showinfo('알림','주문이 완료되었습니다.')
#
# def warn():
#     msgbox.showwarning('경고', '해당 메뉴가 매진되었습니다.')
#
# def err():
#     msgbox.showerror('오류', '결제 오류가 발생했습니다.')
#
# def okcancel():
#     msgbox.askokcancel('확인/취소', '대기시간이 10분 이상이다.\n기다리겠습니까?')
#
# def retrycancel():
#     msgbox.askretrycancel('재시도/취소', '일시오류입니다.\n다시 진행하시겠습니까?')
#
# def yesno():
#     response = msgbox.askyesno(title=None, message='결제 계속 진행할까요?')
#     if response == True:
#         print('감사합니다. 결제 진행합니다.')
#     else:
#         print('감사합니다. 결제 취소되었습니다. 다음에 또 오세요.')
#
# root = Tk()
# root.title('test')
# root.geometry('640x480')
#
# Button(root, text='알림', command=info).pack()
# Button(root, text='경고', command=warn).pack()
# Button(root, text='오류', command=err).pack()
# Button(root, text='확인/취소', command=okcancel).pack()
# Button(root, text='재시도/취소', command=retrycancel).pack()
# Button(root, text='예/아니오', command=yesno).pack()
#
# root.mainloop()

#-----------------------------------
# from tkinter import *
#
# root = Tk()
# root.title('test')
# root.geometry('640x480')
#
# Label(root, text='메뉴를 선택해 주세요.').pack(side='top')
# btn = Button(root, text='주문하기')
# btn.pack(side='bottom')
#
# frame1 = Frame(root, bd=1, relief='solid')
# frame1.pack(side='left', fill='both', expand=True)
# Button(frame1, text='햄버거').pack()
# Button(frame1, text='불고기버거').pack()
# Button(frame1, text='새우버거').pack()
#
# frame2 = LabelFrame(root, text='음료')
# frame2.pack(side='right', fill='both', expand=True)
# Button(frame2, text='아이스아메리카노').pack()
# Button(frame2, text='콜라').pack()
#
# root.mainloop()

#-----------------------------------
# from tkinter import *
#
# root = Tk()
# root.title('test')
# root.geometry('640x480')
#
# frame = Frame(root)
# frame.pack()
# scrollbar = Scrollbar(frame)
# scrollbar.pack(side='right', fill='y')
# listbox = Listbox(frame, selectmode='extended', yscrollcommand=scrollbar.set)
# for i in range(1,32):
#     listbox.insert(END, str(i)+'일')
# listbox.pack(side='left')
# scrollbar.config(command=listbox.yview)
#
# root.mainloop()

#-----------------------------------
# from tkinter import *
#
# root = Tk()
# root.title('test')
# root.geometry('640x480')
#
# btn_f16 = Button(root, text='F16', width=5, height=2)
# btn_f17 = Button(root, text='F17', width=5, height=2)
# btn_f18 = Button(root, text='F18', width=5, height=2)
# btn_f19 = Button(root, text='F19', width=5, height=2)
# btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
# btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
# btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
# btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)
#
# btn_7 = Button(root, text='7', width=5, height=2)
# btn_8 = Button(root, text='8', width=5, height=2)
# btn_9 = Button(root, text='9', width=5, height=2)
# btn_add = Button(root, text='+', width=5, height=2)
# btn_7.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
# btn_8.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
# btn_9.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
# btn_add.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)
#
# btn_4 = Button(root, text='4', width=5, height=2)
# btn_5 = Button(root, text='5', width=5, height=2)
# btn_6 = Button(root, text='6', width=5, height=2)
# btn_minus = Button(root, text='-', width=5, height=2)
# btn_4.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
# btn_5.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
# btn_6.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
# btn_minus.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)
#
# btn_1 = Button(root, text='1', width=5, height=2)
# btn_2 = Button(root, text='2', width=5, height=2)
# btn_3 = Button(root, text='3', width=5, height=2)
# btn_enter = Button(root, text='enter', width=5, height=2)
# btn_1.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
# btn_2.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
# btn_3.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
# btn_enter.grid(row=3, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)
#
# btn_0 = Button(root, text='0', width=5, height=2)
# btn_dot = Button(root, text='.', width=5, height=2)
# btn_0.grid(row=4, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
# btn_dot.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
#
# root.mainloop()

#-----------------------------------
# 메모장
# from tkinter import *
# from tkinter import filedialog
#
# def fOpen():
#     file = filedialog.askopenfile(parent=root, mode='r')
#     if file != None:
#         lines = file.read()
#         print(lines)
#         # 1.0은 line.column이다.
#         #line은 1부터 시작하고 column은 0부터 시작함..
#         text_area.delete('1.0', END)
#         text_area.insert('1.0', lines)
#         file.close()
#
# def fSave():
#     file = filedialog.asksaveasfile(parent=root, mode='w')
#     if file != None:
#         lines = text_area.get('1.0', END+'-1c') # 마지막에서 1 char 뺀다, \n제거!
#         print(lines)
#         file.write(lines)
#         file.close()
#
# root = Tk()
# root.title('test')
# root.geometry('640x480')
#
# menu = Menu(root)
# root.config(menu=menu)
#
# menu_file = Menu(menu, tearoff=False)
# menu_edit = Menu(menu, tearoff=False)
# menu_tjtlr = Menu(menu, tearoff=False)
# menu_view = Menu(menu, tearoff=False)
# menu_help = Menu(menu, tearoff=False)
#
# menu_file.add_command(label='열기', command=fOpen)
# menu_file.add_command(label='저장', command=fSave)
# menu_file.add_separator()
# menu_file.add_command(label='끝내기', command=root.quit)
#
# menu.add_cascade(label='파일', menu=menu_file)
# menu.add_cascade(label='편집', menu=menu_edit)
# menu.add_cascade(label='서식', menu=menu_tjtlr)
# menu.add_cascade(label='보기', menu=menu_view)
# menu.add_cascade(label='도움말', menu=menu_help)
#
# text_area = Text(root)
# scrollbar = Scrollbar(root, command=text_area.yview)
# text_area.config(yscrollcommand=scrollbar.set)
# text_area.pack(side='left', fill='both', expand=True)
# scrollbar.pack(side='right', fill='y')
#
# root.mainloop()

#-----------------------------------
# 계산기
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('계산기')
root.geometry('640x480')
btn_list=[['7','8','9','*'],
          ['4','5','6','/'],
          ['1','2','3','-'],
          ['0','.','del','+']]


text = StringVar()
text_box = ttk.Entry(root, width=12, textvariable=text)
text_box.pack()

res = Label(root, text='결과:')
res.pack()

root.mainloop()





# btn_7.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)


















