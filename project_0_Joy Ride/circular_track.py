
# coding: utf-8

# In[12]:


get_ipython().run_cell_magic('HTML', '', '<button id="launcher">Launch Car Simulator</button>\n<script src="setupLauncher.js"></script>')


# In[13]:


from Car import Car
import time

def circle(car):
    car.steer(5)
    car.gas(0.8)
    
car = Car()

circle(car)

