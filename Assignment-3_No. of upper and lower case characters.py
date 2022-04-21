#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


# In[2]:


Sample_String = "The quick Brow Fox"
def No_of_characters(Sample_String):
    
    u=0
    l=0
    for i in Sample_String:
        if 65<=ord(i)<=90:
            u+=1
        elif 97<=ord(i)<=122:
            l+=1
        else:
            pass
    print("No. of upper case characters:", u)
    print("No. of lower case characters:", l)
No_of_characters(Sample_String)


# In[3]:


Sample_String = input("Enter the Sentence String:")
Output = No_of_characters(Sample_String)


# In[4]:


Sample_String = input("Enter the Sentence String:")
Output = No_of_characters(Sample_String)


# In[ ]:




