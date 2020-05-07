#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("pokemon.csv")
df.head()


# In[4]:


df.sort_values("Name",inplace=True)
df


# In[6]:


df["Name"].duplicated()


# In[8]:


df["Speed"].duplicated(keep=False)


# In[9]:


df[df["Speed"].duplicated(keep=False)]


# In[11]:


mask=~df[df["Speed"].duplicated(keep=False)]
df[mask]


# In[ ]:




