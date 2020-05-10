#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


bond=pd.read_csv("jb.csv",index_col="Film")

bond.sort_index(inplace=True)

bond.head()


# In[3]:


bond


# In[4]:


bond["Bond actor"]=="Sean Connery"


# In[5]:


mask=bond["Bond actor"]=="Sean Connery"
bond[mask]


# In[7]:


bond[mask]["Bond actor"]


# In[8]:


bond[mask]["Bond actor"]="Sir Sean Connery"


# In[10]:


bond.head()


# In[12]:


df=bond[mask]
df["Bond actor"]="Sir Sean Conery"
df


# In[13]:


bond.ix[mask]


# In[14]:


bond.ix[mask,"Bond actor"]


# In[16]:


bond.ix[mask,"Bond actor"]="Sir Sean Connery"
bond


# In[17]:


bond[bond["Bond actor"]=="Pierce Brosnan"]


# In[20]:


bond.ix[bond["Bond actor"]==" Pierce Brosnan"]


# In[ ]:




