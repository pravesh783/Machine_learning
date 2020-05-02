#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


rate=[3.99,4.54,3.67,8.9,6.8]

r=pd.Series(rate)

r


# In[4]:


r.sum()


# In[6]:


r.product()


# In[7]:


r.mean()


# In[8]:


fruts=['apple','watermelon','pineapple','grape','mango']

weak=["sunday ","monday","wdnesday","friday","thursfday"]

pd.Series(fruts,weak)


# In[9]:


fruts=['apple','watermelon','pineapple','grape','mango']

weak=["sunday ","monday","wdnesday","friday","thursfday"]

pd.Series(fruts,weak)
pd.Series(data=fruts,index=weak)


# In[ ]:




