import os
import shutil

def toCsv_by_colNames(df, itemList, path):
    ## 과제3 ##
    # itemList = ['색상앞', '업소명', '전문일반구분']
    stopWords = '\ / : * ? " < > |'
    # path = './과제3'

    for item in itemList:
        for stopWord in stopWords.split(' '):
            item = item.replace(stopWord, '_')
        if item in os.listdir(path):
            print('기존폴더 삭제')
            shutil.rmtree(path+'/'+item)
        os.mkdir(path+'/'+item)

        for x in df[item].unique():
            tmp = df[df[item]==x]

            for txt in stopWord.split(' '):
                x = x.replace(txt, '_')
            
            tmp.to_csv(path + '/' + item + '/' + x + '.csv', encoding='utf-8-sig')

# toCsv_by_colNames(['색상앞', '업소명', '전문일반구분'], './과제3')