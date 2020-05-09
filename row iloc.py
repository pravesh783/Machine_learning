#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


bond=pd.read_csv("jb.csv")

bond.head()


# In[4]:


bond.loc[15]


# In[5]:


bond.iloc[[15,20]]


# In[6]:


bond.iloc[:4]


# In[7]:


bond.iloc[4:8]


# In[ ]:




