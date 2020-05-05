#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pkm=pd.read_csv("pokemon.csv")

pkm.head()


# In[3]:


pkm.tail()


# In[4]:


pkm.dropna()


# In[5]:


pkm.dropna(how="any")
pkm.dropna(how="all")


# In[6]:


pkm.dropna(how="any")
pkm.dropna(how="all",inplace=True)
pkm


# In[7]:


pkm.tail()


# In[8]:


pkm.dropna(axis=1)


# In[9]:


pkm.dropna(subset=["Type 2"])


# In[ ]:




