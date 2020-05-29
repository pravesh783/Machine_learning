#!/usr/bin/env python
# coding: utf-8

# In[11]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np


# In[14]:


np.random.seed(101)
tf.set_random_seed(101)


# In[15]:


rand_a = np.random.uniform(0,100,(5,5))
rand_a


# In[16]:


rand_b=np.random.uniform(0,100,(5,1))
rand_b


# In[17]:


a=tf.placeholder(tf.float32)
b=tf.placeholder(tf.float32)


# In[18]:


add=a+b


# In[19]:


mul=a*b


# In[24]:


with tf.Session() as sess:
    add_result=sess.run(add,feed_dict={a:rand_a,b:rand_b})
    print(add_result)
    print("\n")
    mult=sess.run(mul,feed_dict={a:rand_a,b:rand_b})
    print(mult)
    
   


# In[ ]:




