#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np 


# In[4]:


x=np.arange(0,2*np.pi,0.01)

y1=np.sin(x)
y2=np.cos(x)

plt.plot(x,y1,label='sin')
plt.plot(x,y2,label='cos')

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.title("sin & cosine")
plt.legend()
plt.show()


# In[6]:


x=np.arange(0,2*np.pi,1)

y1=np.sin(x)
y2=np.cos(x)

plt.plot(x,y1,label='sin')
plt.plot(x,y2,label='cos')

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.title("sin & cosine")

plt.show()


# In[ ]:




