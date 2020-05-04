#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.read_csv("pokemon.csv")


# In[3]:


pkm=pd.read_csv("pokemon.csv")

pkm.head()


# In[4]:


pkm.tail()


# In[5]:


pkm.index


# In[6]:


pkm.shape


# In[7]:


pkm.info


# In[8]:


pkm.get_dtype_counts()


# In[9]:


pkm.dtypes.value_counts()


# In[ ]:




