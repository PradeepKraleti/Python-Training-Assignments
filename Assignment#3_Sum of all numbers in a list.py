#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a python function to sum all numbers in a list


# In[2]:


#Sample list: (8,2,3,0,7)
#Output: 20


# In[13]:


Number_List = [8,2,3,0,7]
def sum(Number_List):
    a=0
    itr=0
    for i in Number_List:
        a += i
        itr+=1
        print("The sum of number list in iteration:",[itr],a)
    return(a)
print("Sum of all numbers in the given list", sum(Number_List)) 


# In[ ]:




