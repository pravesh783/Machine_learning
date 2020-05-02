#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

pd.read_csv("test.csv")


# In[3]:


import pandas as pd

pd.read_csv("test.csv",squeeze=True)


# In[8]:


import pandas as pd

pd.read_csv("test.csv",squeeze=True,usecols=["1"])

