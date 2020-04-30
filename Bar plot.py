#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


x=[1,2,3,4,5,6]
y=[10,34,56,78,12,30]

tick_label=['one','two','three','four','five','six']

plt.bar(x,y,tick_label=tick_label,width=0.9)
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.title("Bar graph")

plt.show()


# In[5]:


x=[1,2,3,4,5,6]
y=[10,34,56,78,12,30]

tick_label=['one','two','three','four','five','six']

plt.bar(x,y,tick_label=tick_label,width=0.9,color=['green','blue','red','yellow'])
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.title("Bar graph")

plt.show()


# In[ ]:




