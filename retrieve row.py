#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


bond=pd.read_csv("jb.csv",index_col="Film")

bond.head()


# In[4]:


bond.sort_index(inplace=True)
bond.head()


# In[5]:


bond.loc["Goldfinger"]


# In[7]:


bond.loc["GoldenEye"]


# In[8]:


bond.loc["Casino Royale"]


# In[9]:


bond.loc["Diamonds are forever":"Moonraker"]


# In[ ]:




