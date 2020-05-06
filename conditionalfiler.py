#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df=pd.read_csv("pokemon.csv")
df.head()


# In[5]:


df.info()


# In[6]:


df["Legendary"]=="False"


# In[8]:


df[df["Legendary"] == "True"]


# In[ ]:




