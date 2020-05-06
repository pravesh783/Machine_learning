#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df=pd.read_csv("pokemon.csv")
df.head()
df.tail()


# In[6]:


mask1=df["Type 2"]=="Poisan"
mask2=df["Type 2"]=="Dark"
mask3=df["Type 2"]=="Water"
df[mask1 | mask2 | mask3].head(8)


# In[8]:


mask=df["Type 2"].isin(["Dark","Water","Poisan"])
df[mask]


# In[ ]:




