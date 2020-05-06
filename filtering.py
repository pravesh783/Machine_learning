#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df=pd.read_csv("first.csv")


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df["Industry_code_NZSIOC"].head()


# In[16]:


df["Industry_code_NZSIOC"].astype("bool")

df["Industry_code_NZSIOC"]=df["Industry_code_NZSIOC"].astype("bool")


# In[17]:


df.info()


# In[ ]:




