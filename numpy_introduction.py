
# coding: utf-8

# In[15]:

import numpy as np


# In[31]:

a = np.array([1, 2, 3, 4, 5]) #declaring an array using list anotation

a


# In[35]:

b = np.array((6, 7, 8, 9, 10)) #declaring an array using tuple anotation

b


# In[24]:

#different mathematical operations can be perfomed on numpy array, which which reflect on each element of the array.

a * 3 


# In[47]:

# mathematical operations between two arrays

a + b


# In[48]:

b / a


# In[20]:

type(a)


# In[21]:

a.dtype


# In[27]:

#bytes per element

a.itemsize 


# In[30]:

#size reports total number of elements in an Array.

a.size 


# In[33]:

a.shape #it indicates that array has 5 elements along dimension zero in this case.


# In[42]:

c = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

c


# In[44]:

#number of rows and columns

c.shape 


# In[45]:

len(c)


# In[46]:

c.size


# In[49]:

# Return the number of bytes used by the data portion of the array

c.nbytes


# In[50]:

# number od dimensions

c.ndim


# In[51]:

# Array Indexing
a


# In[52]:

a[0]


# In[53]:

c


# In[54]:

c[1][2]


# In[55]:

# Re-assigning values

a[0] = 50


# In[56]:

a


# In[57]:

# set all values in an array using Fill

a.fill(0)


# In[58]:

a


# In[59]:

#this also works but can be slower

a[:] = 100


# In[60]:

a


# In[61]:

# assigning a float into an int32 array truncates the decimal part

a[0] = 5.8


# In[62]:

a


# In[63]:

# fill has the same behaviour

a.fill(4.6)


# In[64]:

a


# In[66]:

# Slicing for Arrays works like List Slicing

b


# In[67]:

b[2:4]


# In[68]:

b[-4:3]


# In[69]:

b[::2]


# In[71]:

# Creating array using arange

np.arange(30)


# In[76]:

r = np.arange(30).reshape(5,6)


# In[75]:

r 


# In[77]:

r[-1, -1] # Unlike list, multiple parameters can be passed in single bracket to locate an element in the array. 


# In[87]:

r[1, 1]


# In[88]:

r[2, 1:]


# In[89]:

r[:1 , :1]


# In[90]:

r[: , 2] = 100 #targeting a column


# In[91]:

r


# In[83]:

list_example = [[1,2,3], [4,5,6]]


# In[84]:

list_example[-1][-1] # here we have to passmeters in separate brackets


# In[92]:

r % 3 == 0 # values divisible by 3


# In[93]:

r[r % 3 == 0] # Using above mask/condition to get the values.


# In[98]:

b


# In[99]:

b.sum()


# In[100]:

b.prod()


# In[101]:

b.mean()


# In[102]:

b.max()


# In[103]:

b.min()


# In[108]:

r


# In[109]:

r[2, 4]  = -10


# In[110]:

r


# In[111]:

np.unravel_index(r.argmin(), r.shape) #to find the index of min/smallest element in the array


# In[113]:

# different options to create arrays
# reshape function can be used with these options to give array a desired shape

np.arange(5)


# In[114]:

np.zeros(5)


# In[115]:

np.ones(6)


# In[117]:

np.linspace(0, 2, 10) #similar to arange


# In[ ]:



