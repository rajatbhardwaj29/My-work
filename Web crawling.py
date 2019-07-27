#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4


# In[2]:


import numpy as np


# In[3]:


import pandas as pd


# In[4]:


import urllib.request as url


# In[5]:


path = "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2019;trophy=12;type=season"
http_response = url.urlopen(path)
webpage = bs4.BeautifulSoup(http_response,'lxml')


# In[23]:


table=webpage.find('table')

head = table.findAll('th')


# In[28]:


t_head=[]
for i in head:
     t_head.append(i.text)
print(t_head)


# In[29]:



columns=t_head[-7:]
data=table.findAll('td')
data1=[]
for i in data:
     data1.append(i.text)
print(data1)


arr=np.array(data1)
print(arr)
array_data=arr.reshape(48,7)
print(array_data)
data_set=pd.DataFrame(array_data,columns=t_head)
print(data_set)
print(data_set)





