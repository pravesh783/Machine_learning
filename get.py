#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 


# In[5]:


tes=pd.read_csv("first.csv",index_col="Year",squeeze=True)

tes.sort_index(inplace=True)

tes.head()


# In[7]:


tes.get("2013")
tes


# In[ ]:




