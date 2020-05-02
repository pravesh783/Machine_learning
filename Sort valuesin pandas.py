#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


test=pd.read_csv("test.csv",usecols=["1"],squeeze=True)


# In[5]:


test


# In[9]:


test.sort_values().head(8)


# In[11]:


test.sort_values().head(8)

test.sort_values(ascending=False).tail()


# In[13]:


google=pd.read_csv("test.csv",squeeze=True)
google.head()

