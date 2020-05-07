#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("pokemon.csv")

df.head()


# In[3]:


df["Speed"].between(60,75)


# In[4]:


df[df["Speed"].between(60,75)]


# In[ ]:




