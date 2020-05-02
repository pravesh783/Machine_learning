#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


test=pd.read_csv("test.csv",usecols=["1"],squeeze=True)

test.head(4)


# In[4]:


test.sort_values(ascending=False,inplace=True)
test.head(4)


# In[5]:


test.sort_index()


# In[7]:


test.sort_index(ascending=False,inplace=True)
test.head()


# In[ ]:




