#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values


# In[2]:


#Sample Output : {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}


# In[3]:


#Method-1 by Dictionary and Loops 


# In[4]:


a = "abcdefghijklmnopqrstuvwxyz"
j=0
m_d = {a[i]: (len(a[j:i])+97) for i in range (0, len(a))}
print("The mini Dictionary of small alphabets ASCII codes are:", m_d)


# In[5]:


#Method -2 by Dictionary and ASCII function


# In[6]:


a = "abcdefghijklmnopqrstuvwxyz"
m_d = {a[i]: ord(a[i]) for i in range (0, len(a))}
print("The mini Dictionary of small alphabets ASCII codes are:", m_d)


# In[ ]:




