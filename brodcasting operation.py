#!/usr/bin/env python
# coding: utf-8

# In[1]:


import  pandas as pd


# In[2]:


pkm=pd.read_csv("pokemon.csv")

pkm.head()


# In[3]:


pkm["Attack"].add(100)


# In[4]:


pkm["Defense"].add(8)


# In[5]:


pkm["Defense"]+8


# In[6]:


pkm["Attack"].mul(3)


# In[ ]:




