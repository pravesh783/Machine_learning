#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


# In[4]:


data=pd.read_csv('ads.csv')
data.head()


# In[7]:


real_x=data.iloc[:,[2,3]].values
real_y=data.iloc[:,4].values


# In[11]:


training_x,testing_x,training_y,testing_y = train_test_split(real_x,real_y,test_size=0.25,random_state=0)


# In[12]:


s_c = StandardScaler()
training_x=s_c.fit_transform(training_x)
testing_x=s_c.transform(testing_x)


# In[14]:


cls_svc = SVC(kernel='linear',random_state=0)
cls_svc.fit(training_x,training_y)


# In[15]:


y_pred = cls_svc.predict(testing_x)
y_pred


# In[16]:


testing_y


# In[17]:


from sklearn.metrics import confusion_matrix


# In[18]:


c_m = confusion_matrix(testing_y,y_pred)
c_m


# In[20]:


from matplotlib.colors import ListedColormap
x_set,y_set = training_x,training_y
x1,x2=np.meshgrid(np.arange(start = x_set[:,0].min()-1,stop=x_set[:,0].max()+1,step=0.01)
                  np.arange(start = x_set[:,1].min()-1,stop=x_set[:,1].max()+1,step=0.01)
plt.contourf(x1,x2,cls_svc.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),
            alpha = 0.75,cmap=ListedColormap(('red','green')))
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],
                 c=ListedColormap(('red','green'))(i),label=j)
    
    
plt.title("SVM")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()
               


# In[21]:


x_set,y_set = test_x,test_y
x1,x2=np.meshgrid(np.arange(start = x_set[:,0].min() -1,stop=x_set[:,0].max() +1,step=0.01)
                  np.arange(start = x_set[:,1].min() -1,stop=x_set[:,1].max() +1,step=0.01)
plt.contourf(x1,x2,cls_svc.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),
            alpha = 0.75,cmap=ListedColormap(('red','green')))
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],
                 c=ListedColormap(('red','green'))(i),label=j)
    
    
plt.title("SVC testing")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()
               


# In[ ]:




