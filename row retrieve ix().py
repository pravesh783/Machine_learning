#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


bond=pd.read_csv("jb.csv",index_col="Film")

bond.head()


# In[12]:


bond.sort_index(inplace=True)
bond


# In[8]:


bond.loc["GoldenEye"]


# In[9]:


bond.ix["GoldenEye"]


# In[14]:


bond.ix["A View to a kill":"Thw World is not Enough"]


# In[16]:


bond.ix["Skyfall"]


# In[17]:


"Skyfall" in bond.index


# In[18]:


"sacred" in bond.index


# In[19]:


bond.ix[10]


# In[ ]:




