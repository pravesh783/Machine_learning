#!/usr/bin/env python
# coding: utf-8

# In[7]:


name=input("please enter your name")
age=int(input("What is your age,{0}".format(name)))


if age <=18:
    print("you are not eligible for voting")
else:
    print("you are eligible for voting {0}".format(18-age))


# In[ ]:


print("please enter a no between 1 to 10")
guess=int(input())
if guess <5:
    print("Please guess higher")
    
    guess=int(input())
    if guess==5:
        print("Weldone")
    else:
        print("Sorry,you have not guess correct")
elif guess>5:
    print("Please guess lower no")
    guess=int(input())
    if guess==5:
        print("Weldone")
    else:
        print("Sorry,you have not guess correct")
else:
    print("you got it first time")
        


# In[ ]:


#BREAK and CONTINUE in PYTHON
name="Pravesh"
while True:
    print("plese enter your name")
    name1=input()
    if name is name1:
        break
print("Thank you",name)


# In[ ]:


while True:
    print("who are you")
    name=input()
    
    if name is 'Pravesh':
        continue
    print("hello Pravesh what is your password")
    password=input()
    if password=='time':
        break
print("congrats,Access granted")


# In[ ]:




