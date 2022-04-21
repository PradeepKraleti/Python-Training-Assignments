#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a python program to reverse a String
#Sample String:"1234abcd"
#Expected Output: "dcba4321"


# In[2]:


#Method 1


# In[3]:


str="1234abcd"
def reverse(str):
    Reversed_str =""
    for i in str:
        Reversed_str = i + Reversed_str
    print("The reversed string:", Reversed_str)
reverse(str)


# In[4]:


str = input("Enter the Sample String:")
Output = reverse(str)


# In[5]:


str = input("Enter the Sample String:")
Output = reverse(str)


# In[6]:


#Method 2


# In[7]:


str ="1234abcd"
def Rev(str):
    for i in range(len(str)-1,-1,-1):
        print(str[i], end='')
Rev(str)


# In[8]:


str = input("Enter the Sample String:")
Output = Rev(str)


# In[ ]:




