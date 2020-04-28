#!/usr/bin/env python
# coding: utf-8

# In[8]:


#FOR LOOP
for i in range(20,1,-2):
    print("i is now {}".format(i) )


# In[9]:


number="9,223,036,854,775,807"
for i in range(0,len(number)):
    print(number[i])


# In[17]:


number="9,223,036,854,775,807"
for i in range(0,len(number)):
    if number[i] in '0123456789':
        print(number[i ],end="")
print(type(number))
    


# In[16]:


number="9,223,036,854,775,807"
cleanednumber=''
for i in range(0,len(number)):
    if number[i] in '0123456789':
        cleanednumber=cleanednumber+number[i]
        
newnumber=int(cleanednumber)
print(type(newnumber))
print("the no is {}".format(newnumber))


# In[18]:


# while loop


# In[19]:


var1=0

while var1<10:
    print("value of  var1 is",var1)
    var1+=1


# In[23]:


avaiable_exist={"east","west","north","south"}

choisen_exit=""

while choisen_exit not in  avaiable_exist:
    choisen_exit=input("please enter the direction :")
    
print("are you not glad that you are  out of this loop ")


# In[27]:


avaiable_exist={"east","west","north","south"}

choisen_exit=""

while choisen_exit not in  avaiable_exist:
    choisen_exit=input("please enter the direction :")
    if choisen_exit=="quit":
        print("your GAME OVER")
        break
    else:
    
         print("are you not glad that you are  out of this loop ")


# In[ ]:




