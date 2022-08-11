#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 모듈화
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import requests
import time
import os
import urllib.request
from datetime import datetime

def google_img(search, scroll_cnt=1):
    url = 'https://www.google.co.kr/imghp?hl=ko&ogbl'

    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get(url)
    time.sleep(2)

    # 검색
    elem = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    elem.click()
    elem.send_keys(search)
    elem.send_keys(Keys.ENTER)
    time.sleep(2)

    # 스크롤
    for i in range(scroll_cnt):
        if i == 5:
            driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)
        else:   
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)

    html = driver.page_source
    time.sleep(2)

    driver.close()
    driver.quit()
    
    # BeautifulSoup 전환 후 img 추출
    soup = bs(html, 'html.parser')
    img_tags = soup.select('div#islrg div.islrc div img')
    
    today = datetime.today()
    date = str(today.year) + str(today.month) + str(today.day) + str(today.hour) + str(today.minute)
    
    os.makedirs(f'./{search}{date}/', exist_ok=True)
    
    for idx,img_tag in enumerate(img_tags,1):
        try:
            # print(img_tag['src'])
            urllib.request.urlretrieve(img_tag['src'], f'./{search}{date}/{search}{str(idx)}_google_{date}.jpg')
        except:
            pass


# In[ ]:




