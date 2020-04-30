#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[3]:


ages=[2,56,75,34,89,67,12,90,22,67,88,99,32,11,12,78,54,34,66,99,76,54,32,12,34,56,78,90,9,76]

range=(0,100)

bins=10

plt.hist(ages,bins,range,color='pink',histtype='bar',rwidth=0.7)

plt.xlabel("ages")
plt.ylabel("bins")
plt.title("Histogram Bar")
plt.show()


# In[5]:


ages=[2,56,75,34,89,67,12,90,22,67,88,99,32,11,12,78,55,77,88,99,11,22,33,44,65,79,54,34,66,99,76,54,32,12,34,56,78,90,9,76]

range=(0,100)

bins=10

plt.hist(ages,bins,range,color='green',histtype='bar',rwidth=0.7)

plt.xlabel("ages")
plt.ylabel("bins")
plt.title("Histogram Bar")
plt.show()


# In[ ]:




