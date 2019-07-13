#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle 

turtle.color("green")
turtle.begin_fill()
turtle.circle(130,180)
turtle.end_fill()
turtle.hideturtle()
turtle.color("orange")
turtle.begin_fill()
turtle.circle(130,180)
turtle.end_fill()
turtle.hideturtle()


# In[ ]:


#Draw a Spirling Square with Pen color as 'Red'
import turtle as y
a=y.Turtle()
a.pencolor('red')
for i in range (100):
    a.forward(i)
    a.left(91)
y.done()


# In[ ]:


def printLarge(n):
    large = 0
    while n != 0:
        r = n % 10
        if large < r:
            large = r
        n = n // 10
    return large
printLarge(195263)


# In[ ]:


def isPalindrome(n):
    rev = 0
    buffer = n
    while n!= 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    if rev == buffer:
        return True
    else:
        return False
    return


# In[ ]:


def countPalindrome(lb,ub):
    cnt = 0
    while lb != ub:
        # Implement
        if isPalindrome(lb) == True:
            cnt = cnt + 1
        lb = lb + 1
    return cnt
countPalindrome(1,10)


# In[ ]:




