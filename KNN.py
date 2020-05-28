#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix


# In[2]:


data=pd.read_csv('ads.csv')
data.head(10)


# In[4]:


real_x=data.iloc[:,[2,3]].values
real_x


# In[5]:


real_y=data.iloc[:,4].values
real_y


# In[10]:


training_x,test_x,training_y,test_y = train_test_split(real_x,real_y,test_size=0.25,random_state=0)


# In[11]:


training_x


# In[12]:


test_x


# In[14]:


s_c = StandardScaler()
training_x=s_c.fit_transform(training_x)
training_x


# In[15]:


test_x=s_c.fit_transform(test_x)
test_x


# In[18]:


cls = KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
cls.fit(training_x,training_y)


# In[20]:


y_pred = cls.predict(test_x)
y_pred


# In[21]:


test_y


# In[24]:


c_m = confusion_matrix(test_y,y_pred)
c_m


# In[30]:


from matplotlib.colors import ListedColormap
x_set,y_set = training_x,training_y
x1,x2=np.meshgrid(np.arange(start = x_set[:,0].min()-1,stop=x_set[:,0].max()+1,step=0.01)
                  np.arange(start = x_set[:,1].min()-1,stop=x_set[:,1].max()+1,step=0.01)
plt.contourf(x1,x2,cls.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),
            alpha = 0.75,cmap=ListedColormap(('red','green')))
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],
                 c=ListedColormap(('red','green'))(i),label=j)
    
    
plt.title("KNN")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()
               


# In[31]:


x_set,y_set = test_x,test_y
x1,x2=np.meshgrid(np.arange(start = x_set[:,0].min() -1,stop=x_set[:,0].max() +1,step=0.01)
                  np.arange(start = x_set[:,1].min() -1,stop=x_set[:,1].max() +1,step=0.01)
plt.contourf(x1,x2,cls.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),
            alpha = 0.75,cmap=ListedColormap(('red','green')))
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],
                 c=ListedColormap(('red','green'))(i),label=j)
    
    
plt.title("KNN testing")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()
               

