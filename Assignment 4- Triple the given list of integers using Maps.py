#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program to triple all numbers of a given list of integers. Use Python map.

# sample list: [1, 2, 3, 4, 5, 6, 7]

# Triple of list numbers:

# [3, 6, 9, 12, 15, 18, 21]


# In[2]:


#Method 1 using Maps and Lambda


# In[3]:


n=[1,2,3,4,5,6,7]
print("Triple of List of numbers:",list(map((lambda var:var*3),n)))


# In[4]:


#Method 2 using Maps and Function


# In[5]:


n=[1,2,3,4,5,6,7]
def Triple(n):
    n*=3
    return(n)
print("Triple of List of numbers:", list(map(Triple, n)))


# In[6]:


#Method 3 using for loop


# In[7]:


n=[1,2,3,4,5,6,7]
n3=[]
for i in n:
    n3.append(Triple(i))
print("Triple of List of numbers:",n3)


# In[ ]:




