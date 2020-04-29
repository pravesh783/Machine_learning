#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

my_list=[1,2,3,4]

type(np.array(my_list))


# In[3]:


import numpy as np

my_list=[1,2,3,4]

type(np.array(my_list))
arr=np.array(my_list)
arr


# In[5]:


np.arange(0,10)


# In[6]:


np.zeros(5)


# In[7]:


np.zeros((3,5))


# In[8]:


np.ones((3,5))


# In[9]:


np.random.randint(0,9)


# In[12]:


np.random.randint(0,9)

np.random.randint(0,1000,(4,4))


# In[13]:


np.random.seed(101)

np.random.randint(0,100,10)


# In[16]:


np.random.seed(101)

np.random.randint(0,100,10)
arr
arr.max()
arr.mean()

arr.argmax()


# In[17]:


arr.argmin()


# In[21]:


np.random.seed(101)

np.random.randint(0,100,10)
arr
arr.reshape(2,2)


# In[22]:


mat=np.arange(0,100).reshape(10,10)
mat


# In[23]:


mat[4][5]


# In[24]:


mat[:,1]


# In[ ]:




