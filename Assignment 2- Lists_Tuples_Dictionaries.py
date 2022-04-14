#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples


# In[2]:


#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


# In[3]:


#Method 1: By function


# In[4]:


sl = [(2,5),(1,2),(4,4),(2,3),(2,1)]


# In[5]:


def last(sl):
    return sl[-1]
def sort(sl):
    return sorted (sl, key = last)
print ("The sorted list in increasing order by the tuples in last element:", sort(sl))


# In[6]:


#Method 2: by Loops


# In[7]:


L = [(2,5),(1,2),(4,4),(2,3),(2,1)]


# In[8]:


for i in range (len(L)-1):
    for j in range (len(L)-1):
        a,b=L[j]
        c,d=L[j+1]
        if b>d:
            temp = L[j]
            L[j] = L[j+1]
            L[j+1] = temp
        else:
            pass
print ("The sorted list in increasing order by the tuples in last element:", (L))


# In[9]:


#Different List for testing the Loop python program


# In[10]:


L = [(3,5),(1,7),(4,1),(2,9),(2,4)]


# In[11]:


for i in range (len(L)-1):
    for j in range (len(L)-1):
        a,b=L[j]
        c,d=L[j+1]
        if b>d:
            temp = L[j]
            L[j] = L[j+1]
            L[j+1] = temp
        else:
            pass
print ("The sorted list in increasing order by the tuples in last element:", (L))


# In[ ]:




