#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


bond=pd.read_csv("jb.csv",index_col="Film")
bond.sort_index(inplace=True)

bond.head()


# In[3]:


bond.rename(columns={"Year":"Total Dispatched","Actual box office":"Villians Dispatched"},inplace=True)
bond.head()


# In[5]:


bond.rename(index={"Dr.NO":"A View to a Kill"},inplace=True)
bond


# In[6]:


bond.ix["Moonraker"]


# In[7]:


bond.coloumns=["Total Dispatched","Years lapse","Bond actor","Bond actor","patched","Total Dispatched"]
bond.head()


# In[ ]:




