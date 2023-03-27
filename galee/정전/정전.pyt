from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


driver = webdriver.Chrome()

driver.get('http://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/sfc/acd/iflccwUserList.jsp?menuSeq=99')
time.sleep(2)
search = driver.find_element(By.ID, 'q_startDt')
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys('20120601')
search = driver.find_element(By.ID, 'q_endDt')
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys(Keys.BACK_SPACE)
search.send_keys('20220407')
time.sleep(1)
item = driver.find_elements(By.CLASS_NAME, 'search_btn')
item[0].click()
time.sleep(2)
data =[]
# for i in range(411):
for i in range(411):
    if (i >= 300):
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')
        for j in range(10):
            if i == 410:
                if j == 7:
                    break
                tmp=[]
                tmp.append(soup.find(id=f"apiTr_{j}_loc").text)
                tmp.append(soup.find(id=f"apiTr_{j}_dt").text)
                tmp.append(soup.find(id=f"apiTr_{j}_cntDown").text)
                data.append(tmp)
            else:
                tmp=[]
                tmp.append(soup.find(id=f"apiTr_{j}_loc").text)
                tmp.append(soup.find(id=f"apiTr_{j}_dt").text)
                tmp.append(soup.find(id=f"apiTr_{j}_cntDown").text)
                data.append(tmp)
        # data.append(soup)
    item = driver.find_elements(By.CLASS_NAME, 'paging_btn')
    item[1].click()
    time.sleep(0.2)

df=pd.DataFrame.from_records(data)
df.to_csv('정전5.csv',encoding="cp949")
