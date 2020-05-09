#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


bond=pd.read_csv("jb.csv",index_col="Film")

bond.sort_index(inplace=True)

bond.head()


# In[12]:


bond.ix["Skyfall"]


# In[5]:


bond.ix["Skyfall","Year"]="2014"


# In[11]:


bond.ix["Skyfall",["Year","Bond actor"]]=[2460,"Pravesh"]


# In[ ]:




