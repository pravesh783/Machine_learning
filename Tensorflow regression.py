#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[25]:


x_data=np.linspace(0.0,10,1000000)


# In[26]:


noise=np.random.randn(len(x_data))
x_data


# In[27]:


noise


# In[7]:


#y=mx+b,b=5
y_true = (0.5*x_data)+5+noise


# In[28]:


x_df = pd.DataFrame(data=x_data,columns=['Data'])


# In[29]:


y_df=pd.DataFrame(data=y_true,columns=['Y'])


# In[30]:


x_df.head()


# In[31]:


y_df.head()


# In[32]:


my_data=pd.concat([x_df,y_df],axis=1)


# In[33]:


my_data.head()


# In[34]:


my_data.sample(n=250).plot(kind='scatter',x='Data',y='Y')


# In[38]:


batch_size=8


# In[39]:


m=tf.Variable(0.5)
b=tf.Variable(1.0)


# In[40]:


xph=tf.placeholder(tf.float32,[batch_size])
yph=tf.placeholder(tf.float32,[batch_size])


# In[41]:


y_model = m*xph+b


# In[42]:


error=tf.reduce_sum(tf.square(yph-y_model))


# In[44]:


optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.001)
train=optimizer.minimize(error)


# In[45]:


init=tf.global_variables_initializer()


# In[46]:


with tf.Session() as sess:
    sess.run(init)
    
    
    batches=1000
    for i in range(batches):
        rand_ind=np.random.randint(len(x_data),size=batch_size)
        feed={xph:x_data[rand_ind],yph:y_true[rand_ind]}
        sess.run(train,feed_dict=feed)
    model_m,model_b=sess.run([m,b])


# In[49]:


model_m


# In[50]:


model_b


# In[51]:


y_hat=x_data*model_m+model_b


# In[52]:


my_data.sample(n=250).plot(kind='scatter',x='Data',y='Y')
plt.plot(x_data,y_hat,'g')


# In[ ]:




