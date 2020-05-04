#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


google=pd.read_csv("first.csv")
google


# In[3]:


google=pd.read_csv("first.csv",squeeze=True)

google.head()


# In[5]:


def classify_perforance(number):
    if number<300:
        return "ok"
    elif number<300 and number < 650 :
        return "satisfactory"
    else :
        return "inreadable"


# In[6]:


google.apply(classify_perforance)


# In[7]:


first=pd.read_csv("test.csv",squeeze=True)
first


# In[9]:


def classify_perforance(number):
    if number<8:
        return "ok"
    elif number >= 8 and number < 10 :
        return "satisfactory"
    else :
        return "inreadable"


# In[10]:


first.apply(classify_perforance)


# In[11]:


google=pd.read_csv("pokemon.csv")
google


# In[13]:


google=pd.read_csv("pokemon.csv",squeeze=True)
google


# In[14]:


def classify_perforance(number):
    if number<300:
        return "ok"
    elif number<300 and number < 650 :
        return "satisfactory"
    else :
        return"incedble"
    


# In[ ]:




