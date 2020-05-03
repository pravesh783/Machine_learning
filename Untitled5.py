#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


test=pd.read_csv("test.csv",squeeze=True)
test


# In[5]:


test.head()


# In[8]:


test


# In[14]:


tes=pd.read_csv("first.csv")
tes


# In[22]:


tes=pd.read_csv("first.csv",usecols=["Year"],squeeze=True)
tes


# In[23]:


tes[10]


# In[24]:


tes[[100,200,300]]
tes[50:100]


# In[25]:


tes[:51]


# In[26]:


tes[-30:]


# In[28]:


tes[-30:20]


# In[ ]:




