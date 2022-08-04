#!/usr/bin/env python
# coding: utf-8

# In[7]:


# 내가 한거

def get_df_by_naverAPI(search, category='blog', start=1):
    '''
    category = 'blog, news, book, movie, cafearticle, kin, shop...'
    1 <= start <= 1000
    default display = 100
    ''' 
    import os
    import sys
    import urllib.request
    import json
    import pandas as pd
    
    client_id = "54q2aSQIN4MCZ8baU_aw"
    client_secret = "qU3u6LNbIm"

    encText = urllib.parse.quote(search)
    url = "https://openapi.naver.com/v1/search/"+category+"?query=" + encText +"&display=100&start="+str(start)

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        json_obj = json.loads(response_body)
        df = pd.DataFrame(json_obj['items'])
    else:
        print("Error Code:" + rescode)
        
    return df


# In[8]:


# df = get_df_by_naverAPI('스타벅스')
# display(df)


# In[20]:


# 선생님이 한거

import os
import sys
import urllib.request
import json
import pandas as pd

def connect(search, category='blog'):
    client_id = "54q2aSQIN4MCZ8baU_aw"
    client_secret = "qU3u6LNbIm"

    encText = urllib.parse.quote(search)
    url = "https://openapi.naver.com/v1/search/"+category+"?query=" + encText +"&display=100&start=1"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode!=200):
        print("Error Code:" + rescode)
        return

    response_body = response.read()
    response = json.loads(response_body)
    return response

# response = connect('파이썬', 'blog')

def naver_api(search, category='blog'):
    '''
    naver_api(search, category='blog')
    api='blog'(default) 'news | cafearticle | kin | book | encyc | movie'
    'news(뉴스) | cafearticle(카페글) | kin(지식인) | book(책검색) | encyc(백과사전) | movie(영화검색)'
    '''

    response = connect(search, category)
    df = pd.DataFrame(response['items'])
    return df

def total_count(search, category='blog'):
    response = connect(search, category)
    return response['total']

if __name__ == '__main__':
    # df = naver_api('파이썬', 'kin')
    # display(df)
    t = total_count('파이썬', 'cafearticle')
    print(t)


# In[ ]:




