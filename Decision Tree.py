#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor


# In[8]:


data=pd.read_csv('ps.csv')
data.head()


# In[15]:


real_x= data.iloc[:,1:2].values

real_y=data.iloc[:,2].values


# In[16]:


reg = DecisionTreeRegressor(random_state=0)
reg.fit(real_x,real_y)


# In[22]:


x_grid = np.arange(min(real_x),max(real_x),0.01)
x_grid = x_grid.reshape((len(x_grid),1))
                        


# In[23]:


plt.scatter(real_x,real_y,color='green')
plt.plot(x_grid,reg.predict(x_grid),color='blue')
plt.title('Decision Tree')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()


# In[ ]:




