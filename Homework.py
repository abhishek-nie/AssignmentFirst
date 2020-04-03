#!/usr/bin/env python
# coding: utf-8

# # Task 1
# 

# In[1]:


print("1st homework")


# # Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line.
# 

# In[24]:


for i  in range(2000,3201):
    if (i%7 == 0) and (i%5 !=0):
        print(i,end=", ")
    


# # Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.

# In[60]:


firstName = input("Enter first name")
lastName = input("Enter Last name")
print(lastName[::-1] + " " + firstName[::-1])


# # Same here also

# In[23]:


firstName = input("Enter first name")
lastName = input("Enter Last name")
print(lastName + " " + firstName)


# In[34]:


import math
r= 12
print("Value of volume of sphere is  V=",(4/3)*math.pi*r*r*r)


# # Task 2

# # Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.
# 

# In[40]:


print(list(input().split(",")))


# # Write a Python program to reverse a word after accepting the input from the user

# In[41]:


userInput = input("Enter the string")
print(userInput[::-1])


# In[58]:


def printPattern(userInput):
      for i in range(0, userInput):
           for j in range(0, i + 1):
                print("* ", end="")
           print("\r")
      for i in range(userInput, -1 , -1):
          for j in range(0, i + 1):
               print("* ", end="")
          print("\r")
 
userInput = int(input("Enter the no. to print patter "))
printPattern(userInput)


# # Print in given format

# In[59]:



print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens")


# In[ ]:





# In[ ]:




