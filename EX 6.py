#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


x_data = np.linspace(0,10,10)+np.random.uniform(-1.5,1.5,10)
x_data


# In[4]:


y_label=np.linspace(0,10,10)+np.random.uniform(-1.5,1.5,10)
y_label


# In[7]:


plt.plot(x_data,y_label,'*')


# In[9]:


np.random.rand(2)


# In[10]:


m=tf.Variable(0.98)
b=tf.Variable(0.85)


# In[11]:


#cost function

error=0
for x,y in zip(x_data,y_label):
    y_hat=m*x+b
    error+=(y-y_hat)**2


# In[14]:


optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train=optimizer.minimize(error)


# In[15]:


init=tf.global_variables_initializer()


# In[21]:


with tf .Session() as sess:
    sess.run(init)
    
    epochs=100
    for i in range(epochs):
        sess.run(train)
        
    
    final_slope,final_intersect=sess.run([m,b])


# In[22]:


final_slope


# In[23]:


final_intersect


# In[24]:


x_test=np.linspace(-1,11,10)
y_pred_plot = final_slope*x_test+final_intersect
plt.plot(x_test,y_pred_plot,'g')
plt.plot(x_data,y_label,'*')


# In[ ]:




