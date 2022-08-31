'''
# -----------------------------------
# Messagebox
# -----------------------------------
import tkinter.messagebox as msgbox

[msgbox 메서드]
msgbox.showinfo('창제목','메시지내용') : 정보창 나타남
msgbox.showwarning('창제목','메시지내용'): 경고창 나타남
msgbox.showerror('창제목','메시지내용'): 오류창 나타남
msgbox.askokcancel('창제목','메시지내용'): 확인/취소 버튼 나타남
msgbox.askretrycancel('창제목, '메시지내용'): 다시시도/취소 버튼 나타남
msgbox.askyesno('창제목','메시지내용'): 예/아니오 버튼 나타남
msgbox.askyesnocancel(title=None, message='메시지 내용') : 예/아니오/취소 버튼 나타남. 창 제목은 없음


# ------------------------------------------------
# 1. 알림창, 경고창, 오류창
# ------------------------------------------------

import tkinter.messagebox as msgbox
from tkinter import *

root=Tk()
root.title('test')
root.geometry('640x480')

# 주문 시스템
# 1. 버튼을 누르면 '알림,주문이 완료되었습니다.'
# 2. 버튼을 누르면 '경고, 해당 메뉴가 매진되었습니다'
# 3. 버튼을 누르면 '오류, 결재 오류가 발생했습니다.'
# 4. 버튼을 누르면 '확인/취소, 대기 시간이 10분 이상입니다. 예약하시겠습니까?'
# 5. 버튼을 누르면 '재시도/취소, 일시 오류입니다. 다시 시도하시겠습니까?'
# 6. 버튼을 누르면 '예/아니오, 결재를 진행하시겠습니까?'
def info():
    msgbox.showinfo('알림', '주문이 완료되었습니다') ##msgbox.showinfo('창제목','메시지 내용')
def warn():
    msgbox.showwarning('경고', '해당 메뉴가 매진되었습니다')
def err():
    msgbox.showerror('오류', '결재 오류가 발생했습니다')
def okcancel():
    msgbox.askokcancel('확인/취소','대기 시간이 10분이상입니다.예약하시겠습니까?')
def retrycancel():
    msgbox.askretrycancel('재시도/취소', '일시오류입니다. 다시시도하시겠습니까?')
def yesno():
    msgbox.askyesno('예/아니오','결재 진행하시겠습니까')

Button(root,text='알림', command=info).pack()
Button(root,text='경고', command=warn).pack()
Button(root,text='오류', command=err).pack()
Button(root,text='확인/취소', command=okcancel).pack()
Button(root,text='재시도/취소', command=retrycancel).pack()
Button(root,text='예/아니오', command=yesno).pack()
root.mainloop()
'''
# ------------------------------------------------------------
# 2. 메시지박스의 yes/no/cancel를 눌렀을 때 응답 메시지 출력¶
# ------------------------------------------------------------
import tkinter.messagebox as msgbox
from tkinter import *

root=Tk()
root.title('test')
root.geometry('640x480')

# 주문 시스템

def info():
    msgbox.showinfo('알림', '주문이 완료되었습니다') ##msgbox.showinfo('창제목','메시지 내용')
def warn():
    msgbox.showwarning('경고', '해당 메뉴가 매진되었습니다')
def err():
    msgbox.showerror('오류', '결재 오류가 발생했습니다')
def okcancel():
    msgbox.askokcancel('확인/취소','대기 시간이 10분이상입니다.예약하시겠습니까?')
def retrycancel():
    msgbox.askretrycancel('재시도/취소', '일시오류입니다. 다시시도하시겠습니까?')
def yesno():
    response=msgbox.askyesno('예/아니오','결재 진행하시겠습니까') # msgbox명령을 response 변수에 정의한다.
    if response==1:
        print('예')
    else:
        print('아니요')


Button(root,text='알림', command=info).pack()
Button(root,text='경고', command=warn).pack()
Button(root,text='오류', command=err).pack()
Button(root,text='확인/취소', command=okcancel).pack()
Button(root,text='재시도/취소', command=retrycancel).pack()
Button(root,text='예/아니오', command=yesno).pack()
root.mainloop()