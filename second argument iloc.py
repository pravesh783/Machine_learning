#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


bond=pd.read_csv("jb.csv",index_col="Film")

bond.sort_index(inplace=True)
bond.head()


# In[4]:


bond.loc["Moonraker","Year"]


# In[6]:


bond.iloc[14,2]


# In[7]:


bond.iloc[15,2:7]


# In[8]:


bond.ix[20]


# In[9]:


bond.ix[20,"Year"]


# In[ ]:




