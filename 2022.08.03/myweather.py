#!/usr/bin/env python
# coding: utf-8

# In[18]:


# json으로 기상청 api 자료 받기
import requests
import json
import pandas as pd
import time

def connect(s_date, e_date, code):
    key = '3stAbv9xb2DXsahAa8m%2BKk3IbrtFKuJERl1J94cP13IWHoRG4OiNDa2nBScTx0PicBTTDFVBTgfjv0hWpV6cBg%3D%3D'
    startDt = s_date
    endDt = e_date
    stnIds = code

    url1 = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey='+key
    url2 = '&pageNo=1&numOfRows=999&dataType=JSON&dataCd=ASOS&dateCd=DAY&startDt='+str(startDt)
    url3 = '&endDt='+str(endDt)
    url4 = '&stnIds='+str(stnIds)
    url = url1 + url2 + url3 + url4

    response = requests.get(url)
    
    if(response.status_code != 200):
        print('연결 오류')
        return
    else:
        return response


def find_code(name):
    try:
        df_code = pd.read_csv('./기상청_지역코드.csv', encoding='euc-kr')
        code = int(df_code[df_code['지점명'] == name]['지점'])
    except FileNotFoundError:
        print('파일이 없습니다.')
        return
    except Exception as e:
        print('오류 발생:', e)
        return
    finally:
        return code


def get_weather(s_date, e_date, t_code):
    code = find_code(t_code)
    if code ==None:
        return
    
    response = connect(s_date, e_date, code)
    
    json_obj = json.loads(response.text)
    items = json_obj['response']['body']['items']['item']
    df = pd.DataFrame(items)
    df_res = df[['stnId', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn', 'maxWs', 'avgWs']]
    return df_res

if __name__ == '__main__':
    df = get_weather(20220101, 20220106, '서울')
    display(df)


# In[14]:




