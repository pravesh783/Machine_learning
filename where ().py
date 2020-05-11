#!/usr/bin/env python
# coding: utf-8

# In[1]:


import  pandas as pd


# In[3]:


bond=pd.read_csv('jb.csv',index_col="Film")
bond.sort_index(inplace=True)

bond.head()


# In[4]:


bond["Bond actor"]


# In[5]:


mask=bond["Bond actor"]=="Sean Connery"
bond[mask]


# In[6]:


bond.where(mask)


# In[8]:


bond.where(bond["Others' Dispatched"] > 20)


# In[ ]:




