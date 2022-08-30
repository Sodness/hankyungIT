'''
# --------------------------------------------------------
# Listbox
# 목록을 불러와 추가, 제거 또는 선택하기 위한 리스트박스를 생성
# -----------------------------------------------------------
[listbox]: 여러줄에 걸쳐 목록을 관리하는 위젯

    Listbox(root, selectmode='extended', height=0)

    - selectmode='extended' / 'single'
        - extended: 여러 개 선택 가능,
        -single : 1개만 선택 가능
    - height= 0
        - height= 0 :리스트 갯수만큼 모두 보여주고 listbox크기가 늘어남
        - height=3: 3개 리스트만 보여줌. 스크롤바는 다음 시간에

[Listbox 관련 메서드]
    - 리스트 박스에 선택된 항목 삭제하기 (delete)
    - 리스트 박스 항목 갯수 구하기(size)
    - 리스트 항목을 확인하고 프린터하고(get(시작index, 끝index))
    - 선택한 리스트 항목 확인_위치로 반환(culselection())
'''

import tkinter

window=tkinter.Tk()
window.title('test')
window.geometry('640x480')

listbox=tkinter.Listbox(window,selectmode='extended', height=0)
listbox.insert(0,'1번')
listbox.insert(1,'2번')
listbox.insert(2,'3번')
listbox.insert(tkinter.END,'4번')
listbox.insert(tkinter.END,'5번')

listbox.delete(1,2)
listbox.pack()
window.mainloop()
