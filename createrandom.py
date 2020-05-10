#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


bond=pd.read_csv("jb.csv",index_col="Film")
bond.sort_index(inplace=True)

bond.head()


# In[3]:


bond


# In[4]:


bond.sample()


# In[5]:


bond.sample(n=5)


# In[ ]:




