#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pkm=pd.read_csv("pokemon.csv")

pkm.head()


# In[5]:


pkm=pd.read_csv("pokemon.csv").dropna(how="all")

pkm["Attack"]=pkm["Attack"].fillna(0)

pkm.head()


# In[6]:


pkm=pd.read_csv("pokemon.csv").dropna(how="all")

pkm["Attack"]=pkm["Attack"].fillna(0).astype(int)

pkm.head()


# In[7]:


pkm["Attack"].rank()


# In[9]:


pkm["Attack"].rank(ascending=False).astype(int)


# In[10]:


pkm["Attackrank"]=pkm["Attack"].rank(ascending=False).astype(int)

pkm.head()


# In[14]:


pkm["Attackrank"]=pkm["Attack"].rank(ascending=False).astype(int)

pkm.sort_values(by="Attack",ascending=False)


# In[ ]:




