#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


pkm=pd.read_csv("pokemon.csv")
pkm.head()


# In[5]:


pkm.sort_values(["Total","HP"])


# In[7]:


pkm.sort_values(["Type 2","HP"],ascending=False).head()


# In[ ]:




