#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


pkm=pd.read_csv("pokemon.csv")

pkm.head()


# In[4]:


pkm.sort_values("Name")


# In[5]:


pkm.sort_values("HP")


# In[6]:


pkm.sort_values("Type 2",na_position="first")


# In[ ]:




