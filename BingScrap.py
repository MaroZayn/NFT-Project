#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup

twitter_username = "rockernft1"

target_url="https://www.bing.com/search?q="+twitter_username+"&qs=HS&sk=HS3&sc=10-0&cvid=DF487E35E8A64AD9B1A579B843491E40&FORM=QBLH&sp=4&lq=0"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

resp=requests.get(target_url,headers=headers)
soup = BeautifulSoup(resp.text, 'html.parser')

completeData = soup.find_all("li",{"class":"b_algo"})

response =completeData[0].find("div",{"class":"b_vlist2col"}).text.strip()

spl_word ="Abonnés"
result = response.split(spl_word)[1].replace(":", " ").strip()
print(result)


# In[ ]:




