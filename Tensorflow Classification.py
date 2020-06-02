#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


diabetes=pd.read_csv('diabetes.csv')
diabetes.head(30)


# In[5]:


diabetes.columns


# In[6]:


cols_to_norm=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction']


# In[7]:


diabetes[cols_to_norm]=diabetes[cols_to_norm].apply(lambda x:(x-x.min())/(x.max()-x.min()))


# In[8]:


diabetes.head()


# In[11]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


# In[12]:


diabetes.columns


# In[61]:


num_preg = tf.feature_column.numeric_column('Number_pregnent')
num_glu = tf.feature_column.numeric_column('Number_Glucose')
num_bp = tf.feature_column.numeric_column('Number_BP')
num_st = tf.feature_column.numeric_column('Number_sk')
num_insulin = tf.feature_column.numeric_column('Number_insulin')
num_BMI = tf.feature_column.numeric_column('Number_BMI')
num_dpf = tf.feature_column.numeric_column('Number_DPF')
num_age = tf.feature_column.numeric_column('Number_age')


# In[62]:


import matplotlib.pyplot as plt


# In[63]:


diabetes['Age'].hist(bins=20)


# In[64]:


age_bucket = tf.feature_column.bucketized_column(num_age,boundaries=[20,30,40,50,60,70,80])


# In[65]:


feat_cols = [num_preg,num_glu,num_bp,num_st,num_insulin,num_BMI,num_dpf,age_bucket]


# In[66]:


#train test split


# In[67]:


x_data = diabetes.drop('Outcome',axis=1)
x_data.head()


# In[68]:


labels  = diabetes['Outcome']
labels.head()


# In[69]:


from sklearn.model_selection import train_test_split


# In[70]:


x_train,x_test,y_train,y_test = train_test_split(x_data,labels,test_size=0.3,random_state=101)


# In[71]:


x_train


# In[72]:


x_test


# In[73]:


input_func = tf.estimator.inputs.pandas_input_fn(x=x_train,y=y_train,batch_size=10,num_epochs=1000,shuffle = True)


# In[74]:


model = tf.estimator.LinearClassifier(feature_columns=feat_cols,n_classes=2)


# In[ ]:





# In[ ]:




