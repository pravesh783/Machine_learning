#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pkm=pd.read_csv("pokemon.csv")
pkm.head()


# In[3]:


pkm.fillna(0)


# In[4]:


pkm["Type 2"].fillna(0)


# In[6]:


pkm["Type 2"].fillna(0,inplace=True)
pkm.head()


# In[ ]:




