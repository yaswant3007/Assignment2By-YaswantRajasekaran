#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
1. Write a Python function to multiply all the numbers in a list.
"""
def mulallnum(a_lst):
    o=""
    j=1
    for k in a_lst:
        if k!="[" and k!="]":
            o+=k
    p=o.split(",")
    po=[]
    for t in p:
        tp=float(t)
        po.append(tp)
    for i in po:
        j=j*i
    return j
l=input()
print(mulallnum(l))


# In[2]:


"""
2. Write a Python function to reverse a string
i) use for loop
"""

def revstr(a_str):
    c=""
    for  i in range(len(s)-1,-1,-1):
        c+=a_str[i].lower()
    return c    

s=input()
print(revstr(s))


# In[3]:


"""
2. Write a Python function to reverse a string
ii) use while loop
"""
def revstr(a_str):
    c=""
    i=len(a_str)-1
    while i>=0:
        c+=a_str[i].lower()
        i=i-1
    return c


s=input()
print(revstr(s))


# In[4]:


"""
3. Write a function to add and subtract two variables
"""

def aands(a,b):
    add=a+b
    sub1=a-b
    sub2=b-a
    print("Result of Addition of Two Variables =",add)
    if sub1<0:
        print("Result of Subtraction of Two Variables (when the smaller value is subtracted by the greater value) =",sub1)
    if sub2<0:
        print("Result of Subtraction of Two Variables (when the smaller value is subtracted by the greater value) =",sub2)
    if sub1>0:
        print("Result of Subtraction of Two Variables (when the greater value is subtracted by the smaller value) =",sub1)
    if sub2>0:
        print("Result of Subtraction of Two Variables (when the greater value is subtracted by the smaller value) =",sub2)
    if sub1==0 and sub2==0:
        print("Result of Subtraction of Two Variables (when both the variables have equal value) =",sub1)
o=float(input("Enter the first number : "))
p=float(input("Enter the second number : "))
aands(o,p)


# In[5]:


"""
4.Write a function to check the number is divisible by 12
"""

def chknumdivby12(a_cn):
    if a_cn%12==0:
        return True
    else:
        return False

c=float(input())
print(chknumdivby12(c))


# In[7]:


"""
5.Write a function to calculate the number of days and weeks.
"""

def daysandweeks_inamonth(c):
    c=c.split(" ")
    days =0
    lp=""
    oneyearindays=0
    for i in c:
        if c.index(i)==0:
            month=i.lower()
        if c.index(i)==1:
            year=int(i)
    
    if year%4==0 and year%100!=0:
        lp="Leap_Year"
    elif year%100==0 and year%400==0:
        lp="Leap_Year"
    else:
        lp="Not_a_Leap_Year"
    if lp=="Leap_Year":
        oneyearindays=366
    if lp=="Not_a_Leap_Year":
        oneyearindays=365.25
    if month=="jan"or month=="january":
        days=31
    if month=="february" or month=="feb":
        if lp=="Not_a_Leap_Year":
            days=28
        if lp=="Leap_Year":
            days=29
    if month=="mar"or month=="march":
        days=31
    if month=="apr"or month=="april" :
        days=30
    if month=="may":
        days=31
    if month=="june":
        days=30
    if month=="july":
        days=31
    if month=="aug" or month=="august":
        days=31
    if month=="sept"or month=="september" :
        days=30
    if month=="oct"or month=="october" :
        days=31
    if month=="nov"or month=="november" :
        days=30
    if month=="dec"or month=="december" :
        days=31
    weeks=days/7
    print("Number of days in the month of",month,"is",days,"and the number of weeks in the month of",month,"is",weeks)

d=input("Please enter the Month and Year (Enter as shown: January 2023):")
daysandweeks_inamonth(d)


# In[8]:


"""
6.Write a Python function to Find the 5!?
"""
def fac(a_fac):
    j=1
    a_fac.split("!")
    f=int(a_fac[0])
    while f>0:
            j=j*f
            f-=1
    return j

facto=input("Enter a number to find its factorial (Enter as shown: 6!): ")
print(fac(facto))


# In[9]:


"""
7.Write a Python function to find the unique elements of the list =
[1,2,3,3,3,3,4,5,4,2,4,2,4,4,2,4,5,4,34,654,5,7,6,5,4,3]

"""
def unq(a_u):
    o=""
    for i in a_u:
        if i!="[" and i!="]":
            o+=i
    b=o.split(",")
    u=list(set(b))
    return u

ui=str(input("Enter a list : "))
print(unq(ui))


# In[10]:


"""
Types of arguments
1. Required arguments
2. Keyword arguments
3. Default arguments
1. Required arguments:
Write a program to calculate Simple Interest which accepts three arguments and
returns the simple interest accordingly
"""
def si(p,r,t):
    SimpleInt=(p*r*t)/100
    return SimpleInt

ps=float(input("Enter the principal amount: "))
rs=float(input("Enter the rate of interest in percentage: "))
ts=float(input("Enter the time in years: "))
print("Simple Interest = ₹.",si(ps,rs,ts),sep="")


# In[12]:


"""
2.Keyword arguments:
Write a function which will be called with the name and message as the keyword
arguments. Output will be "printing the message with 'name' and 'message'"
"""
def nm(name,message):
    print("printing message with",name,"and",message)

n=input("Enter the name of the person:")
m=input("Enter the message you want to print:")
nm(n,m)


# In[13]:


"""
3.Default Arguments:
Write a function which will be called with the name as keyword argument and age
as the default arguments. Output will be "My name is 'name' and 'age is 27'"
"""
def na(name, age=22):
    print(f"My name is '{name}' and age is '{age}'")

n=input("Enter your name: ")
a=input("Enter your age: ")
if a=="":
    na(n)
else:
    na(n,a)


# In[14]:


"""
lambda function
1. Get a number from user, find if it is even or odd number?
"""
g=lambda n: "Even" if n%2==0 else "Odd"
c=int(input("Enter a number:"))
print(g(c))


# In[15]:


"""
2. Take a input from user and square it
"""
i = lambda s: s**2
ui=int(input("Enter a number to find its square: "))
print(i(ui)) 


# In[16]:


"""
3. Write a lambda function using logical operators?
Hint:
Check x < 10
Output: False / True
"""
h = lambda x: True if x<10 else False
ui = int(input("Enter a number : "))
print(h(ui))


# In[17]:


"""
4. Take an integer input from the user, add 5 to the number and print it back?
"""

a = lambda x : x+5
k = int(input("Enter a number:"))
print(a(k))


# In[18]:


"""
Map:
1. Add two lists using map ()
lis1 = [12, 24, 36]
lis2 = [41, 54, 69]
Output:
[53, 78, 105]
"""

list1=[12,24,36]
list2=[41,54,69]
a=list(map(lambda x,y: x+y,list1,list2))
print(a)


# In[19]:


"""
2. Use Lambda and map functions on a List, to square each element in the list =
[1, 2, 3, 4, 5, 6, 7]
"""
list1=[1, 2, 3, 4, 5, 6, 7]
s=list(map(lambda x: x**2,list1))
print(s)


# In[20]:


"""
3.In the given list [1, 2, 3, 4, 5, 6, 7], find the even and odd elements in the
list, use the map()function
"""
list1 = [1, 2, 3, 4, 5, 6, 7]
ed=list(map(lambda n: "Even" if n%2==0 else "Odd",list1))
print(ed)


# In[21]:


"""
4. In the given list [11, 12, 13, 14, 435, 6, 27], perform the Floor division
using 7 on each elements on the list
"""
list1 = [11, 12, 13, 14, 435, 6, 27]
f=list(map(lambda x: x//7,list1))
print(f)


# In[22]:


"""
Filter
1.Using the given list lis1 = [3,12, 24, 36,43,654,65432,2,654,455,43,543]
filter the numbers in list which are not divisible by 2
"""
lis1 = [3,12, 24, 36,43,654,65432,2,654,455,43,543]
k = list(filter(lambda x: x%2!=0,lis1))
print(k)


# In[23]:


"""
2.For a given list1 = [1, 2, 3, 4, 5, 6] filter only the even numbers (Use
filter).
"""
list1 = [1, 2, 3, 4, 5, 6]
ed = list(filter(lambda x: x%2==0,list1))
print(ed)


# In[24]:


"""
3. For a given list = [2,3,5,3,6,3,7,4,6,7] filter only the even numbers using
user defined function.
"""
def ed(a_n):
    o=""
    l=[]
    for i in a_n:
        if i!="["and i!="]":
            o+=i
    p=o.split(",")
    print(p)
    for j in p:
        op=int(j)
        l.append(op)
    g=list(filter(lambda n : n%2==0,l))
    return g

lt=input("Enter the list to find even numbers in it: ")
print(ed(lt))


# In[25]:


"""
4. For a given list = [1, 12, 31, 4, 15, 6, 7] filter only the odd numbers using
user defined function.
"""
def ed(a_n):
    o=""
    l=[]
    for i in a_n:
        if i!="["and i!="]":
            o+=i
    p=o.split(",")
    print(p)
    for j in p:
        op=int(j)
        l.append(op)
    g=list(filter(lambda n : n%2!=0,l))
    return g

lt=input("Enter the list to find odd numbers in it: ")
print(ed(lt))


# In[26]:


"""
Reduce
1.For list = [1, 2, 3, 4] multiply all the elements (use reduce function)
"""
from functools import reduce
list1 = [1, 2, 3, 4]
mul=reduce((lambda x,y: x*y),list1 )
print(mul)


# In[27]:


"""
2. For list = [ 11 , 13, 15, 16, 2,43 ] sum all the elements (use reduce
function)
"""
import functools
list1 = [ 11 , 13, 15, 16, 2,43 ]
sum = functools.reduce((lambda x,y: x+y),list1)
print(sum)


# In[28]:


"""
3. Find the maximum value in the list = [543,7,6,4567,7,78,6,6,78,765,678] (use
reduce function)
"""
from functools import reduce
list1 = [543,7,6,4567,7,78,6,6,78,765,678]
maxval=reduce((lambda x,y : x if x>y else y), list1)
print(maxval)


# In[29]:


"""
4. Find the minimum value in the list= [543,7,6,4567,7,78,6,6,78,765,678] (use
reduce function)
"""
import functools
list1= [543,7,6,4567,7,78,6,6,78,765,678]
minval= functools.reduce((lambda x,y: x if x<y else y),list1)
print(minval)


# In[ ]:




