#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


bond=pd.read_csv("jb.csv",index_col="Film")
bond.sort_index(inplace=True)

bond.head()


# In[3]:


bond.drop("Die Another Day")


# In[4]:


bond.drop("Casino Royale")


# In[5]:


bond.drop(["You Only Live Twice","The World is Not Enough","Thunderball"])


# In[6]:


bond.drop("Actual box office",axis=1)


# In[11]:


bond.drop(["Villians Dispatched"],axis=1,inplace=True)
bond.head()


# In[12]:


bond


# In[13]:


actor=bond.pop("Bond actor")
bond.head()


# In[ ]:




