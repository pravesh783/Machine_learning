#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


# In[5]:


sess=tf.InteractiveSession()


# In[6]:


my_tensor = tf.random_uniform((5,5),0,2)


# In[7]:


my_tensor


# In[8]:


var1=tf.Variable(initial_value=my_tensor)


# In[9]:


print(var1)


# In[10]:


init = tf.global_variables_initializer()


# In[11]:


sess.run(init)


# In[12]:


sess.run(var1)


# In[14]:


pH1=tf.placeholder(tf.float32,shape=(None,4))


# In[15]:


pH2=tf.placeholder(tf.float32)


# In[ ]:




