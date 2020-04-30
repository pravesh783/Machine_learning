#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


activities=['eat','sleep','work','play']

slices=[3,7,8,6]
color=['r','g','m','b']

plt.pie(slices,labels=activities,colors=color)

plt.legend()
plt.show()


# In[14]:


activities=['eat','sleep','work','play']

slices=[3,7,8,6]
color=['r','g','m','b']

plt.pie(slices,labels=activities,colors=color,startangle=90,shadow=True,explode=(0.2,0,0,0),autopct='x1.2f%%')

plt.legend()
plt.show()


# In[ ]:




