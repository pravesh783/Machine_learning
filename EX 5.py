#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np


# In[7]:


n_f=10
n_d_n = 3


# In[8]:


x=tf.placeholder(tf.float32,(None,n_f))


# In[10]:


b=tf.Variable(tf.zeros([n_d_n]))

w=tf.Variable(tf.random_normal([n_f,n_d_n]))


# In[11]:


#y=mx+c
xw=tf.matmul(x,w)


# In[12]:


z=tf.add(xw,b)


# In[13]:


#activation function

a=tf.sigmoid(z)


# In[14]:


init=tf.global_variables_initializer()


# In[15]:


with tf.Session() as sess:
    sess.run(init)
    
    layer_out=sess.run(a,feed_dict={x:np.random.random([1,n_f])})


# In[16]:


print(layer_out)


# In[ ]:




