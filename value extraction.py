#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


tes=pd.read_csv("first.csv")
tes


# In[6]:


tes=pd.read_csv("first.csv",index_col="Units",squeeze=True)
tes


# In[7]:


tes.head()


# In[12]:


tes.tail()


# In[ ]:





# In[ ]:




