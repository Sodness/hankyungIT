'''
### Menu
- root에 메뉴 객체 만들고  -> root에 등록하기 (root.config(menu=menu))
- 만든 메뉴에 각각의 메뉴 탭을 만듬 -> 메뉴에 적용(menu.add_cascade(label='메뉴탭이름', menu=메뉴명)
    - 메뉴 객체에 메뉴 탭을 만들고 menu_file=Menu(menu,tearoff=0)
    - 메뉴탭에 각각 명령 추가하고(add_command(label='메뉴이름', command=실행함수)
    - 메뉴에 구분선 넣기(separator())
    - 메뉴 비활성로 만들기(state='disable') 옵션 설정
    - 메뉴에 EXIT를 만들고 프로그램 종료함 (command=root.destroy)



# -----------------------------------------------------------
# 1. '파일'메뉴 만들기
# -----------------------------------------------------------
from tkinter import *

root=Tk()
root.title('test')
root.geometry('640x480')

def new_project():
    print('새 프로젝트 명령을 선택했습니다.')
#메뉴 객체 만들고 root에 등록함
menu=Menu(root) #메뉴 객체 만들고
root.config(menu=menu) # root에 메뉴를 등록시킴(root.config(menu=menu)

# -----------------------------------------------------------
# ['파일'메뉴 만들기]
#  - 'menu_file'객체 만들고
#  - menu 명령메뉴 및 구분선 추가하고
#  -'File' 탭이름으로, menu객체에 붙임
#     - menu.add_cascade(label='File', menu=menu_file)
# -----------------------------------------------------------
menu_file=Menu(menu)
menu_file.add_command(label='새 프로젝트...', command=new_project)
menu_file.add_command(label='새로 만들기')
menu_file.add_separator()
menu_file.add_command(label='다시실행', state='disabled')
menu_file.add_separator()
menu_file.add_command(label='종료', command=root.destroy) #root.destroy()Tkinter 창을 닫는 클래스 메소드
menu.add_cascade(label='파일', menu=menu_file) ## 만든 메뉴를 메인 메뉴에 붙임
root.mainloop()

'''

# -----------------------------------------------------------
# 2. 빈 메뉴, 라디오 단추 메뉴, 체크 박스 메뉴 만들기
# -----------------------------------------------------------
from tkinter import *

root=Tk()
root.title('test')
root.geometry('640x480')

def new_project():
    print('새 프로젝트 명령을 선택했습니다.')
#메뉴 객체 만들고 root에 등록함
menu=Menu(root) #메뉴 객체 만들고
root.config(menu=menu) # root에 메뉴를 등록시킴(root.config(menu=menu)

# --------------------메뉴 1 -------------------------
menu_file=Menu(menu,tearoff=0)
menu_file.add_command(label='새 프로젝트...', command=new_project)
menu_file.add_command(label='새로 만들기')
menu_file.add_separator()
menu_file.add_command(label='다시실행', state='disabled')
menu_file.add_separator()
menu_file.add_command(label='종료', command=root.destroy) #root.destroy()Tkinter 창을 닫는 클래스 메소드
menu.add_cascade(label='파일', menu=menu_file) ## 만든 메뉴를 메인 메뉴에 붙임


# --------------------메뉴 2 -------------------------
# 빈 메뉴 만들기
menu.add_cascade(label='편집')

#----------------메뉴3----------------
# 라디오 단추 메뉴 만들기
menu_language=Menu(menu, tearoff=0)
menu_language.add_radiobutton(label='파이썬')
menu_language.add_radiobutton(label='자바')
menu_language.add_radiobutton(label='C++')
menu.add_cascade(label='langueage',menu=menu_language)

#----------------메뉴4----------------
# 체크박스 메뉴 만들기
menu_view=Menu(menu, tearoff=0)
menu_view.add_checkbutton(label='탭 고정')
menu_view.add_checkbutton(label='탭 표시')
menu.add_cascade(label='보기',menu=menu_view)

root.mainloop()
'''
#----------------메뉴3----------------
# 라디오 단추 메뉴 만들기
menu_lang=Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label='Python')
menu_lang.add_radiobutton(label='Java')
menu_lang.add_radiobutton(label='C++')
menu.add_cascade(label='Language', menu=menu_lang)

#----------------메뉴4----------------
# 체크박스 메뉴 만들기
menu_view=Menu(menu, tearoff=0)
menu_view.add_checkbutton(label='Show Minimap')
menu.add_cascade(label='View', menu=menu_view)

root.config(menu=menu) # menu를 root창에 지정한다
root.mainloop()
'''