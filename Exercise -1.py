#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[3]:


import numpy as np


# #### Create an array of 10 zeros 

# In[4]:


arr=np.zeros(10)
arr


# #### Create an array of 10 ones

# In[5]:


arr=np.ones(10)
arr


# #### Create an array of 10 fives

# In[6]:


arr = [5] * 10
print(arr)


# #### Create an array of the integers from 10 to 50

# In[7]:


a=np.arange(10,51,1)
a


# #### Create an array of all the even integers from 10 to 50

# In[8]:


a=np.arange(10,51,2)
a


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[9]:


a=np.arange(9).reshape(3,3)
a


# #### Create a 3x3 identity matrix

# In[10]:


a=np.eye(3)
a


# #### Use NumPy to generate a random number between 0 and 1

# In[11]:


np.random.rand()


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[12]:


a=np.random.rand()
a


# #### Create the following matrix:

# In[13]:


a=np.arange(0.01,1.01,0.01)
a


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[19]:


array = np.linspace(0, 1, 20)
print(array)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[58]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[41]:


np.array([[12, 13, 14, 15],
         [17, 18, 19, 20],
        [22, 23, 24, 25]])


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[29]:


print(20)


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[51]:


# x=np.array([2,7,12])
# x=x.reshape(3,1,1)
# x
np.array([[2],
         [7],
        [12]])


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[33]:


np.arange(21, 26)


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[32]:


np.arange(16, 26).reshape(2, 5)


# ### Now do the following

# #### Get the sum of all the values in mat

# In[59]:


sum = np.sum(mat)

print(sum)


# #### Get the standard deviation of the values in mat

# In[60]:


np.std(mat)


# #### Get the sum of all the columns in mat

# In[61]:


column = np.sum(mat, axis=0)
print(column)


# 
