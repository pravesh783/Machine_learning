#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt


# In[21]:


data=pd.read_csv('ps.csv')
data.head(10)


# In[22]:


real_x=data.iloc[:,1:2].values
real_x


# In[23]:


real_y=data.iloc[:,2].values
real_y


# In[24]:


linear_reg=LinearRegression()
linear_reg.fit(real_x,real_y)


# In[37]:


polynomial_reg=PolynomialFeatures(degree=4)
real_x_poly = polynomial_reg.fit_transform(real_x)


# In[38]:


real_x_poly


# In[39]:


polynomial_reg.fit(real_x_poly,real_y)


# In[40]:


linear_reg2=LinearRegression()
linear_reg2.fit(real_x_poly,real_y)


# In[41]:


plt.scatter(real_x,real_y,color='red')
plt.plot(real_x,linear_reg.predict(real_x),color='blue')
plt.title('Linear Model')
plt.xlabel('Position Label')
plt.ylabel('salary')
plt.show()


# In[42]:


plt.scatter(real_x,real_y,color='red')
plt.plot(real_x,linear_reg2.predict(polynomial_reg.fit_transform(real_x)),color='blue')
plt.title('Polynomial Model')
plt.xlabel('Position Label')
plt.ylabel('salary')
plt.show()

