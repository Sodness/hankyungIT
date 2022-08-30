'''
# --------------------------------------------------------
# Listbox
# 목록을 불러와 추가, 제거 또는 선택하기 위한 리스트박스를 생성
# -----------------------------------------------------------
[listbox]: 여러줄에 걸쳐 목록을 관리하는 위젯

    Listbox(root, selectmode='extended', height=0)

    - selectmode='extended' / 'single'
        - extended: 여러 개 선택 가능,
        - single : 1개만 선택 가능
    - height= 0
        - height= 0 :리스트 갯수만큼 모두 보여주고 listbox크기가 늘어남
        - height=3: 3개 리스트만 보여줌. 스크롤바는 다음 시간에

[Listbox 관련 메서드]
    - 리스트 박스에 선택된 항목 삭제하기 (delete)
    - 리스트 박스 항목 갯수 구하기(size)
    - 리스트 항목을 확인하고 프린터하고(get(시작index, 끝index))
    - 선택한 리스트 항목 확인_위치로 반환(culselection())

[리스트 박스에 선택된 항목 삭제하기 (delete)]
    - listbox.delete(index)
        * 0 : 첫 번째 index 삭제
        * tkinter.END: 마직막 index 삭제

# ------------------------------------------
# 1. listbox 생성
# ------------------------------------------
import tkinter

window=tkinter.Tk()
window.title('test')
window.geometry('640x480')

listbox=tkinter.Listbox(window, selectmode='extended', height=0)
listbox.insert(0,'사과')
listbox.insert(1,'포도')
listbox.insert(tkinter.END,'포도')
listbox.insert(tkinter.END,'수박')
listbox.insert(tkinter.END,'참외')

listbox.pack()
window.mainloop()


# ------------------------------------------
# 2. listbox에 선택된 항목 삭제하기(delete)
#   - listbox.delete(index)
#     * 0 : 첫 번째 index 삭제
#     * END: 마직막 index 삭제
# ------------------------------------------

import tkinter
window=tkinter.Tk()
window.title('test')
window.geometry('640x480')

listbox=tkinter.Listbox(window, selectmode='extended', height=0)
listbox.insert(0,'사과')
listbox.insert(1,'포도')
listbox.insert(tkinter.END,'딸기')
listbox.insert(tkinter.END,'수박')
listbox.insert(tkinter.END,'참외')
listbox.pack()
def btncmd():
    #listbox.delete(0) #첫번째항목삭제
    listbox.delete(tkinter.END)# 마지막 항목 삭제

btn=tkinter.Button(window,text='삭제', command=btncmd)
btn.pack()
window.mainloop()
'''
# ------------------------------------------
# 3. listbox에 항목 갯수 구하기(size)
#   - listbox.size() #리스트박스 모든 항목 갯수
#   - listbox.get(0,2)) # 1번부터 3번까지 항목 이름 가져오기
#   - istbox.curselection() # 선택한 항목 인덱스를 리스트로 반환함
# ------------------------------------------
import tkinter
window=tkinter.Tk()
window.title('test')
window.geometry('640x480')

listbox=tkinter.Listbox(window, selectmode='extended', height=0)
listbox.insert(0,'사과')
listbox.insert(1,'포도')
listbox.insert(tkinter.END,'딸기')
listbox.insert(tkinter.END,'수박')
listbox.insert(tkinter.END,'참외')
listbox.pack()
def btncmd():
    print('모든 항목 갯수:',listbox.size())
    print('1번부터 항목가져오기:',listbox.get(0))
    print('1번부터 3번항목까지 가져오기:',listbox.get(0,2))
    print('모든 항목 가져오기: ', listbox.get(0,tkinter.END))
    print('선택된 항목 index가져오기:', listbox.curselection())
    items=listbox.curselection()
    print('선택된 항목 이름가져오기:',[listbox.get(i) for i in items])

btn=tkinter.Button(window,text='클릭', command=btncmd)
btn.pack()
window.mainloop()
