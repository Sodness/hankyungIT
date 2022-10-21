import os
import shutil

def folderCreate(folder, field):
    # 폴더 이름에 들어가면 안되는 것들
    stopFolderName = '\ / : * ? " < > |'

    for x in stopFolderName.split(' '):
        field = field.str.replace(x, '_')
    
    if folder in os.listdir('./'):
        print('기존폴더를 삭제합니다.')
        shutil.rmtree(folder)
    
    os.mkdir(folder)

    for x in field.unique():
        os.mkdir(folder + '/' + x)

# folderCreate('테스트', df['분류명'])