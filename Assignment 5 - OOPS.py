#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Create You own built-in class method
#Write a Python class to implement pow(x, n)

#Use should be able to find the nth power of the x.(i.e x*x*x*x...n times)

# You must implement it using Class
# Sample Input:
# x: 10
# n: 2
# Sample Output:
# 100


# In[2]:


class Power:
    
    def __init__(self,x,n):
        self.x = x
        self.n = n
        self._power = None
      
    def set_power(self,x,n):
        self._power = x**n
    def get_power(self):
        return self._power
x = int(input("Enter the number:"))
n = int(input("Enter the exponent:"))
Result = Power(x,n)
Result.set_power(x,n)
print("The Result of given number to given power:",Result.get_power())

