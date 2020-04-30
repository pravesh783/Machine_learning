#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[4]:


x=[1,2,3,4,5,6,7,8,9,10]
y=[8,4,5,7,2,9,12,45,26,45]

plt.scatter(x,y,label="stars",color="green",marker="*",s=30)

plt.xlabel("X-axis")
plt.ylabel("Y-Axis")
plt.title("Scatter bar")
plt.legend()
plt.show()


# In[5]:


x=[1,2,3,4,5,6,7,8,9,10]
y=[8,4,5,7,2,9,12,45,26,45]

plt.scatter(x,y,label="circle",color="red",marker="*",s=70)

plt.xlabel("X-axis")
plt.ylabel("Y-Axis")
plt.title("Scatter bar")
plt.legend()
plt.show()


# In[ ]:




