#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[4]:


x1=np.linspace(0.0,5.0)
x2=np.linspace(0.0,2.0)

y1=np.cos(2*np.pi*x1)*np.exp(-x1)
y2=np.cos(2*np.pi*x2)

plt.subplot(2,1,1)
plt.plot(x1,y1,'o-')
plt.title("subplot-1")
plt.xlabel("x1")
plt.ylabel("amplitude of (y1)")
plt.show()


# In[5]:


x1=np.linspace(0.0,5.0)
x2=np.linspace(0.0,2.0)

y1=np.cos(2*np.pi*x1)*np.exp(-x1)
y2=np.cos(2*np.pi*x2)

plt.subplot(2,1,1)
plt.plot(x1,y1,'o-')
plt.title("subplot-1")
plt.xlabel("x1")
plt.ylabel("amplitude of (y1)")

plt.subplot(2,1,2)
plt.plot(x2,y2,".")
plt.title("subplot 2")

plt.xlabel("x2")
plt.ylabel("y2")
plt.show()


# In[ ]:




