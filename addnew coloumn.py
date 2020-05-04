#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pkm=pd.read_csv("pokemon.csv")

pkm.head()


# In[6]:


pkm["Pravesh"]="pokemon"


# In[7]:


pkm.head()


# In[10]:


pkm1=pd.read_csv("pokemon.csv")
pkm1.head()


# In[12]:


pkm1.insert(3,column="sport",value="cricket")
pkm1.head()


# In[ ]:




