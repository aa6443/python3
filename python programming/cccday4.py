#        ---------->          KEYWORD ARGUMENTS        -------------------------------------------------------

# def myfun(x,y):
#     print("x=",x,"y=",y)

# myfun(10,5)
# #for specifying 
# myfun(y=10,x=5)   #this is called as keyword argument 

# def myfun(name,marks):
#     print("name=",name,"marks=",marks)

# #myfun("murthy",90)
# myfun(marks=90,name="Murthy")


# ------------------>    DEFAULT ARGUMENTS   -------------------------------------------------------

# def add(x,y=50):
#     print(x+y)

# add(10)


#------------------> VARIABLE LENGTH ARGUMENTS -----------------------------------------------------

# def add(*p):
#     total=0
#     for i in p:
#         print(i,end=" ")
#         total=total+i
#     print("Total=",total)
#     print()

# add(10,20)
# add(10,20,30)

# add(10,20,30,40)

#--------------------> LAMBDA FUNCTIONS  ---------------------------------------------------------
#            x=lambda n:n*10
#            x=lambda n:(exp)

# def myfun(n):
#     return(n*10)
# print(myfun(4))

# myfun1=lambda n:n*10
# print(myfun1(5))

# res=lambda x,y,z:x+y+z
# print(res(1,2,3))
# print(res(10,20,30))

#------------------> SCOPE OF VARIABLE  ----------------------------------------------------------
# x=100
# def f1():
#     x=10
#     print("x in f1=",x)
# def f2():
#     print("x in f2=",x)

# print("x in main=",x)
# f1()
# f2()

#------------------> RECURSION    -----------------------------------------------------------------
# def f1():
#     print("f1 start")
#     f2()
#     print("f1 end")
# def f2():
#     print("f2 start")
#     print("f2 end")

# print("main start")
# f1()
# print("main end")

# def f1(n):
#     i=1
#     if(n<=10):
#         print(n)
#     f1(n+1)

# print("main start")
# f1(10)

# def f1(n):
#     if n>0 :
#         f1(n-1)                              
#         print(n,end=' ')
# n=10
# f1(n)

#---------------------------->  #recursive function reduces number of lines of code -------------------------

# def f1(n):
#     if(n==0 or n==1):
#         return(1)
#     else:
#         return(n*f1(n-1))
    
# n=3
# f1(n)
#-------------------------->  MODULES ------------------------------------------------------------
#from mymodule import myfun
# from math  import pow,factorial
# print(pow(2,4))
# print(factorial(5))


# import random

# for i in range(10):
#     print(random.randrange(1,10))

#--------------------------> EXCEPTION HANDLING ---------------------------------------------------
# try:
#     print(4/0)
# except:
#     print("division by 0 not possible ")
# print("main end")

# finally:
# print("always executes")
