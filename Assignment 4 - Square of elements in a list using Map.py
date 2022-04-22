#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]


# In[2]:


#Method 1 using maps and lambda


# In[3]:


n= [4,5,2,9]
print("Square of the elements of the list:",list(map((lambda var:var**2),n)))


# In[4]:


#Method 2 using maps and function


# In[5]:


n= [4,5,2,9]
def Square(n):return(n**2)
print("Square of the elements of the list:",list(map(Square,n)))


# In[ ]:




