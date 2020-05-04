#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


rev=pd.read_csv("pokemon.csv")
rev.head()


# In[4]:


s=pd.Series([1,2,3])

s.sum()


# In[5]:


rev.sum()


# In[6]:


rev.sum(axis=0)
rev.sum(axis="index")


# In[8]:


rev.sum(axis=1)


# In[11]:


tes=pd.read_csv("first.csv")
tes


# In[12]:


tes.head(8)


# In[14]:


tes.Units.head()


# In[15]:


tes.Units.head()
type(tes.Units)


# In[ ]:




