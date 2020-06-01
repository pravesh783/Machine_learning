#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


x_data=np.linspace(0.0,10,1000000)


# In[4]:


noise=np.random.randn(len(x_data))
x_data


# In[5]:


noise


# In[6]:


#y=mx+b,b=5
y_true = (0.5*x_data)+5+noise


# In[7]:


x_df = pd.DataFrame(data=x_data,columns=['Data'])


# In[8]:


y_df=pd.DataFrame(data=y_true,columns=['Y'])


# In[9]:


x_df.head()


# In[10]:


y_df.head()


# In[11]:


my_data=pd.concat([x_df,y_df],axis=1)


# In[12]:


my_data.head()


# In[13]:


my_data.sample(n=250).plot(kind='scatter',x='Data',y='Y')


# In[14]:


batch_size=8


# In[15]:


m=tf.Variable(0.5)
b=tf.Variable(1.0)


# In[16]:


xph=tf.placeholder(tf.float32,[batch_size])
yph=tf.placeholder(tf.float32,[batch_size])


# In[17]:


y_model = m*xph+b


# In[18]:


error=tf.reduce_sum(tf.square(yph-y_model))


# In[19]:


optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.001)
train=optimizer.minimize(error)


# In[20]:


init=tf.global_variables_initializer()


# In[21]:


with tf.Session() as sess:
    sess.run(init)
    
    
    batches=1000
    for i in range(batches):
        rand_ind=np.random.randint(len(x_data),size=batch_size)
        feed={xph:x_data[rand_ind],yph:y_true[rand_ind]}
        sess.run(train,feed_dict=feed)
    model_m,model_b=sess.run([m,b])


# In[22]:


model_m


# In[23]:


model_b


# In[24]:


y_hat=x_data*model_m+model_b


# In[25]:


my_data.sample(n=250).plot(kind='scatter',x='Data',y='Y')
plt.plot(x_data,y_hat,'g')


# In[26]:


#estimater API
feat_cols=[tf.feature_column.numeric_column('x',shape=[1])]


# In[27]:


estimator=tf.estimator.LinearRegressor(feature_columns=feat_cols)


# In[28]:


#train test split
from sklearn.model_selection import train_test_split


# In[29]:


x_train,x_eval,y_train,y_eval = train_test_split(x_data,y_true,test_size=0.3,random_state=0)


# In[30]:


x_train.shape


# In[32]:


x_eval.shape


# In[34]:


input_func = tf.estimator.inputs.numpy_input_fn({'x':x_train},y_train,batch_size=4,num_epochs=None,shuffle=True)


# In[35]:


train_input_func = tf.estimator.inputs.numpy_input_fn({'x':x_train},y_train,batch_size=4,num_epochs=1000,shuffle=False)


# In[36]:


eval_input_func = tf.estimator.inputs.numpy_input_fn({'x':x_train},y_train,batch_size=4,num_epochs=1000,shuffle=False)


# In[37]:


estimator.train(input_fn=input_func,steps=1000)


# In[38]:


train_metrics=estimator.evaluate(input_fn=train_input_func,steps=1000)


# In[39]:


eval_metrics = estimator.evaluate(input_fn=eval_input_func,steps=1000)


# In[41]:


input_func_predict = tf.estimator.inputs.numpy_input_fn({'x':np.linspace(0,10,10)},shuffle=False)


# In[43]:


list(estimator.predict(input_fn=input_func_predict))


# In[55]:


predictions = []
for x in estimator.predict(input_fn=input_func_predict):
    
    predictions.append(x['predictions'])
    
   


# In[56]:


predictions 


# In[59]:


my_data.sample(n=250).plot(kind='scatter',x='Data',y='Y')
plt.plot(np.linspace(0,10,10),predictions,'r')


# In[58]:


plt.plot(np.linspace(0,10,10),predictions,'r')


# In[ ]:




