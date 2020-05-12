#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[14]:


data=pd.read_csv("slr.csv")
data.head(7)


# In[19]:


real_x=data.iloc[:,1].values
real_y=data.iloc[:,0].values
real_y
real_x
real_x=real_x.reshape(-1,1)
real_y=real_y.reshape(-1,1)


# In[20]:


training_x,testing_x,training_y,testing_y = train_test_split(real_x,real_y,test_size=0.3,random_state=0)


# In[21]:


lin=LinearRegression()
lin.fit(training_x,training_y)


# In[22]:


pred_y= lin.predict(testing_x)


# In[23]:


testing_y[3]


# In[24]:


pred_y[3]


# In[27]:


plt.scatter(training_x,training_y,color='green')

plt.plot(training_x,lin.predict(training_x),color='blue')

plt.title("SAT and GPA Plot")
plt.xlabel("GPA")
plt.ylabel("SAT")

plt.show()


# In[28]:


plt.scatter(testing_x,testing_y,color='green')

plt.plot(training_x,lin.predict(training_x),color='blue')

plt.title("SAT and GPA Plot")
plt.xlabel("GPA")
plt.ylabel("SAT")

plt.show()


# In[ ]:




