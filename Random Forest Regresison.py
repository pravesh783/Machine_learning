#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


# In[5]:


data=pd.read_csv('ps.csv')
data.head(10)


# In[21]:


real_x=data.iloc[:,1:2].values
real_y=data.iloc[:,2].values


# In[22]:


reg=RandomForestRegressor(n_estimators=100,random_state=0)
reg.fit(real_x,real_y)


# In[23]:


x_grid = np.arange(min(real_x),max(real_x),0.01)
x_grid = x_grid.reshape((len(x_grid),1))
plt.scatter(real_x,real_y,color='green')
plt.plot(x_grid,reg.predict(x_grid),color='blue')

plt.title("RFR")
plt.xlabel("Position")
plt.ylabel("Salary")
plt.show()


# In[ ]:





# In[ ]:




