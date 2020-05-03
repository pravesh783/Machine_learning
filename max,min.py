#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


google=pd.read_csv("first.csv",squeeze=True)
google


# In[5]:


google.head()


# In[6]:


google.max()


# In[7]:


google.min()

