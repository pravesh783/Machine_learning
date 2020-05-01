#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

figl=plt.figure()

axl=figl.add_subplot(1,1,1)

def animate(p):
    plot_data=open('test.txt','r').read()
    line_data=plot_data.split('\n')
    x1=[]
    y1=[]
    
    for line in line_data:
        
        if len(line)>1:
            x,y=line.split(',')
            x1.append(x)
            y1.append(y)
            
            
        axl.clear()
        axl.plot(x1,y1)
anime_data=animation.FuncAnimation(figl,animate,interval=500)
plt.show()


# In[7]:


import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

figl=plt.figure()

axl=figl.add_subplot(1,1,1)

def animate(p):
    plot_data=open('test.txt','r').read()
    line_data=plot_data.split('\n')
    x1=[]
    y1=[]
    
    for line in line_data:
        
        if len(line)>1:
            x,y=line.split(',')
            x1.append(x)
            y1.append(y)
            
            
        axl.clear()
        axl.plot(x1,y1)
anime_data=animation.FuncAnimation(figl,animate,interval=500)
plt.show()


# In[ ]:




