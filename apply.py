#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


bond=pd.read_csv("jb.csv",index_col="Film")

bond.sort_index(inplace=True)

bond.head()


# In[7]:


def add_millions(number):
    return str(number)+ " MILLIONS"

bond["Adjusted box office"]=bond["Adjusted box office"].apply(add_millions)


bond["Adjusted budget"]=bond["Adjusted budget"].apply(add_millions)
bond


# In[ ]:





# In[8]:


def add_millions(number):
    return str(number)+ " MILLIONS"

bond["Adjusted box office"]=bond["Adjusted box office"].apply(add_millions)


bond["Adjusted budget"]=bond["Adjusted budget"].apply(add_millions)
bond


# In[12]:


columns=["Others' Dispatched","Total Dispatched","Adjusted box office","Actual box office","Adjusted budget"]
for col in columns:
    bond[col]=bond[col].apply(add_millions)


# In[13]:


bond.head()


# In[ ]:




