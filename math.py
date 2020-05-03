#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


google=pd.read_csv("first.csv",squeeze=True)
google


# In[3]:


google.head()


# In[5]:


google.count


# In[6]:


len(google)


# In[8]:


google.sum()


# In[9]:


google.mean()


# In[10]:


tes=pd.read_csv("test.csv")
tes


# In[11]:


tes.mean()


# In[ ]:




