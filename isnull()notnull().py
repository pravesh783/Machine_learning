#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("first.csv")
df.head()


# In[6]:


tes=pd.read_csv("pokemon.csv")
tes.head()


# In[8]:


mask=tes["Type 2"]== "NaN"
tes[mask]


# In[9]:


tes["Type 2"]== "NaN"


# In[10]:


mask=tes["Type 2"].isnull()
tes[mask]


# In[11]:


tes["Type 2"].notnull()


# In[12]:


cod=tes["Type 2"].notnull()
tes[cod]


# In[ ]:




