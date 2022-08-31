'''
### 퀴즈 : tkinter를 이용한 메모장 프로그램을 만드시오.

#### [GUI 조건]
1. title: 제목 없음 -Widows 메모장
2. 메뉴: 파일, 편집, 서식, 보기, 도움말
3. 실제 메뉴 구성 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
    - 3-1. 열기: mynote.txt 파일을 열어서 보여주기
    - 3-2. 저장: mynote.txt 파일을 현재 내용 저장하기
    - 3-3. 끝내기: 프로그램 종료
4. 프로그램 시작 시 본문은 비어 있는 상태
5. 하단 status 바는 필요없음
6. 프로그램 크기, 위치는 자유로베 하되 크기 조정 가능해야 함
7. 본문 우측에 상하 스크롤바 넣기


# -----------------------------------------------
# 1. 메뉴만 구성해 보고, 본문 구성
# -----------------------------------------------
from tkinter import *
root=Tk()
root.title('제목 없음 -Widows 메모장')
root.geometry('640x480')

def open_file(): #열기 메뉴 함수
    pass

def save_file(): #저장 메뉴 함수
    pass

# 1. 파일 메뉴 구성(열기, 저장, 구분선, 끝내기)
menu=Menu()
menu_file=Menu(menu,tearoff=0)
menu_file.add_command(label='열기',command=open_file)
menu_file.add_command(label='저장',command=save_file)
menu_file.add_separator()
menu_file.add_command(label='끝내기', command=root.quit)
menu.add_cascade(label='파일', menu=menu_file)

# 2. 편집, 서식, 보기, 도움말는 빈 메뉴로 구성
menu_edit=Menu(menu, tearoff=0)
menu.add_cascade(label='편집', menu=menu_edit)

menu_temp=Menu(menu,tearoff=0)
menu.add_cascade(label='서식', menu=menu_temp)

menu_view=Menu(menu,tearoff=0)
menu.add_cascade(label='보기',menu=menu_view)

menu_help=Menu(menu, tearoff=0)
menu.add_cascade(label='도움말', menu=menu_help)

# -------------------------------------------------
# 3. 본문 구성
#   스크롤바와 text박스로 구성함
# -------------------------------------------------

# 스크롤바
scrollbar=Scrollbar(root)
scrollbar.pack(side='right', fill='y')

# 텍스트 박스
txt=Text(root, yscrollcommand=scrollbar.set) #스크롤바 매핑: yscrollcommand=scrollbar.set
txt.pack(fill='both',expand=True)

scrollbar.config(command=txt.yview) #텍스트바스 매핑: command=txt.yview
root.config(menu=menu)
root.mainloop()

'''
# -----------------------------------------------
# 2. 파일 열기, 저장 함수 완성함
# mynote.txt파일을 열기 (단, 파일이 존재하면
# mynote.txt로 저장함
# -----------------------------------------------
import os
from tkinter import *
root=Tk()
root.title('제목 없음 -Widows 메모장')
root.geometry('640x480')

file_name='mynote.txt'
def open_file(): #열기 메뉴 함수
    if os.path.isfile(file_name): #파일이 존재하면 파일을 읽는다
        with open(file_name,'r', encoding='utf8') as file:
            txt.delete('1.0', END) #텍스트 모두 삭제
            txt.insert(END,file.read())


def save_file(): #저장 메뉴 함수
    with open(file_name,'w', encoding='utf8') as file:
        file.write(txt.get('1.0',END))

# 1. 파일 메뉴 구성(열기, 저장, 구분선, 끝내기)
menu=Menu()
menu_file=Menu(menu,tearoff=0)
menu_file.add_command(label='열기',command=open_file)
menu_file.add_command(label='저장',command=save_file)
menu_file.add_separator()
menu_file.add_command(label='끝내기', command=root.quit)
menu.add_cascade(label='파일', menu=menu_file)

# 2. 편집, 서식, 보기, 도움말는 빈 메뉴로 구성
menu_edit=Menu(menu, tearoff=0)
menu.add_cascade(label='편집', menu=menu_edit)

menu_temp=Menu(menu,tearoff=0)
menu.add_cascade(label='서식', menu=menu_temp)

menu_view=Menu(menu,tearoff=0)
menu.add_cascade(label='보기',menu=menu_view)

menu_help=Menu(menu, tearoff=0)
menu.add_cascade(label='도움말', menu=menu_help)

# -------------------------------------------------
# 3. 본문 구성
#   스크롤바와 text박스로 구성함
# -------------------------------------------------

# 스크롤바
scrollbar=Scrollbar(root)
scrollbar.pack(side='right', fill='y')

# 텍스트 박스
txt=Text(root, yscrollcommand=scrollbar.set) #스크롤바 매핑: yscrollcommand=scrollbar.set
txt.pack(fill='both',expand=True)

scrollbar.config(command=txt.yview) #텍스트바스 매핑: command=txt.yview
root.config(menu=menu)
root.mainloop()

