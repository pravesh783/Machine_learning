#!/usr/bin/env python
# coding: utf-8

# In[10]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


# In[11]:


var1=tf.constant(10)


# In[12]:


var2=tf.constant(20)


# In[16]:


var3=var1+var2


# In[17]:


with tf.Session() as sess:
    result=sess.run(var1+var2)


# In[18]:


print(result)


# In[20]:


print(var3)


# In[21]:


print(tf.get_default_graph())


# In[22]:


g=tf.Graph()
print(g)


# In[23]:


g_1 = tf.get_default_graph()


# In[24]:


print(g_1)


# In[25]:


g_2=tf.Graph()
print(g_2)


# In[26]:


with g_2.as_default():
    print(g_2 is tf.get_default_graph())


# In[27]:


print(g_2 is tf.get_default_graph())


# In[ ]:




