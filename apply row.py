#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


bond=pd.read_csv("jb.csv",index_col="Film")
bond.sort_index(inplace=True)
bond.head(3)


# In[11]:


def good_movie(row):
    Year=row[1]
    
    
    if Year=="2006":
        return "Thhe best"
    elif Year=="1985":
        return " Enjoy"
    else:
        return "Okk"
    
    
bond.apply(good_movie,axis=1)


# In[ ]:




