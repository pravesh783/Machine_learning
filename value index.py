#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


tes=pd.read_csv("first.csv")
tes


# In[9]:


tes=pd.read_csv("first.csv",index_col="Value",squeeze=True)
tes.head()


# In[12]:


pd.value_counts(tes.values.flatten())


# In[ ]:




