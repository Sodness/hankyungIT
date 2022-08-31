from tkinter import *
# color
IVORY='#FFE4C0'
PINK='#FFBBBB'
BLUE='#BFFFF0'
GREEN='#BFFFF0'

#숫자 버튼 눌렀을 때 명령
def clicked(digit):
    # ←버튼 누를 때 끝에서 삭제
    if digit=='←':
        input_entry.delete(len(input_entry.get())-1)
    else:
        input_entry.insert(END,digit)
# C를 눌렀을 때 Entry 모두 삭제
def del_digit():
    input_entry.delete(0,END)
    result_label.config(text='')
# '=' 눌렀을 때 계산
def calulate():
    try:
        result=eval(input_entry.get())
        result_label.config(text=result)
    except:
        result_label.config(text='계산식 오류')


root=Tk()
root.title('계산기')
root.resizable(0,0)
root.config(padx=10,pady=10, bg=IVORY)


digits=[['7','8','9','*'],
       ['4','5','6','/'],
       ['1','2','3','-'],
       ['0','.','←','+']]

# Entry
input_entry=Entry(root,width=30, font=('맑은 고딕',20, 'bold'),
                  bg=IVORY, justify=RIGHT)
input_entry.focus() #커서가 나오게 셋팅    print(input_entry.get())

input_entry.grid(column=0, row=0, columnspan=4, pady=15)

# Label
result_label=Label(root, text='',width=20, font=('맑은 고딕',30),
                   bg=IVORY)
result_label.grid(column=0, row=1, columnspan=4, pady=2)

# digits
for r in range(4):
    for c in range(4):
        digit=digits[r][c]
        button=Button(root, text=digit, width=8, font=('맑은 고딕',15),
                      bg=PINK, command=lambda x=digit: clicked(x))
        button.grid(row=r+2,column=c, pady=2)
#마지막 행(6행)
clear_button=Button(root, text='C',width=17, font=('맑은 고딕',15,'bold'),
                    bg=BLUE, command=del_digit)
clear_button.grid(column=0, row=6, columnspan=2, pady=5)

clear_button=Button(root, text='=',width=17, font=('맑은 고딕',15,'bold'),
                    bg=BLUE, command=calulate)
clear_button.grid(column=2, row=6, columnspan=2, pady=5)


root.mainloop()