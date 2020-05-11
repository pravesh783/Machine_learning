#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


bond=pd.read_csv("jb.csv",index_col="Film")
bond.sort_index(inplace=True)

bond.head()


# In[5]:


bond.columns


# In[6]:


bond.columns=[column_name.replace(" ","_")for column_name in  bond.columns]
bond.head(3)


# In[12]:


bond.query('Bond_actor == "Sean Connery"')


# In[ ]:





# In[13]:


bond.query('Bond_actor != "Sean Connery"')


# In[ ]:


bond

