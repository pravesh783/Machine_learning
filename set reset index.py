#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("pokemon.csv")
df.head()


# In[3]:


tes=pd.read_csv("jb.csv")
tes


# In[5]:


tes.head()


# In[6]:


tes.set_index("Film")


# In[7]:


tes.head()


# In[8]:


tes.reset_index()


# In[9]:


tes.reset_index(drop=True)


# In[11]:


tes.set_index("Year").head()


# In[13]:


tes.reset_index().head()


# In[14]:


tes.set_index("Year",inplace=True)
tes.head()


# In[ ]:




