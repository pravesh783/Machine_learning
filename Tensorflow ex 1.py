#!/usr/bin/env python
# coding: utf-8

# In[12]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


# In[13]:


tf.__version__


# In[14]:


hello = tf.constant("Hello")
hello


# In[15]:


hello


# In[16]:


world = tf.constant("World")


# In[6]:


type(hello)


# In[17]:


print(hello)


# In[18]:


with tf.compat.v1.Session() as sess:
    result = sess.run(hello+world)


# In[19]:


print(result)


# In[20]:


var1=tf.constant(10)
var2=tf.constant(30)


# In[21]:


var1+var2


# In[23]:


with tf.Session() as sess:
    result=sess.run(var1+var2)


# In[24]:


print(result)


# In[25]:


const = tf.constant(10)


# In[26]:


mat1=tf.fill((5,5),10)


# In[27]:


zeros = tf.zeros((5,5))


# In[28]:


ones=tf.ones((5,5))


# In[29]:


randn=tf.random_normal((4,4),mean=0,stddev=1.0)


# In[30]:


randu = tf.random_uniform((4,4),minval=0,maxval=1)


# In[31]:


myops=[const,mat1,zeros,ones,randn,randu]


# In[32]:


sess=tf.InteractiveSession()


# In[35]:


for op in myops:
    print(sess.run(op))
    print("\n")


# In[36]:


for op in myops:
    print(op.eval())
    print("\n")


# In[38]:


a = tf.constant([[1,2],[3,4]])


# In[39]:


a.get_shape()


# In[40]:


b=tf.constant([[10],[100]])


# In[41]:


b.get_shape()


# In[42]:


result = tf.matmul(a,b)


# In[43]:


sess.run(result)


# In[ ]:




