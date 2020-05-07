#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("pokemon.csv")

df.head()


# In[3]:


len(df)


# In[5]:


len(df.drop_duplicates())


# In[7]:


df.drop_duplicates(subset=["Speed"])


# In[8]:


len(df.drop_duplicates(subset=["Speed"]))


# In[9]:


df.drop_duplicates(subset=["Defense","Attack"])


# In[10]:


len(df.drop_duplicates(subset=["Defense","Attack"]))


# In[ ]:




