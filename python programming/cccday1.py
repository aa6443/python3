#typecasting 
#print(4+2)
# print('4'+'2')
# print(int('4')+int('2'))
# print(float(5))
# print(int(5.767))
# print(str(10)+str(20))
# print(complex(7))
# print(bool(8))

#interview tips
# print(bool(-100))
# print(bool("SRM"))
# print(bool(''))
# print(bool(" "))
# print(bool(' '))
# print(bool({}))
# print(bool([]))
# print(bool(None))

#multiple assignment 
# x=y=z=100
# print(x,y,z)

# x,y=10,20
# print(x,y)

#print("x value="+x+)


#multiple statements in single line we use ;
# x=10;y=20;print(x+y)

#reading input 
# x=input("enter x:")
# y=input("enter y:")
# print(int(x)+int(y))

# #or
# x=int(input("enter x:"))
# y=int(input("enter y:"))
# print(int(x+y))

# #readiing multi input
# x,y=map(int,input("enter x,y:").split())
# print(x+y)
# print(x*y)

# mystr="it is python"
# print(mystr.split())
# print(mystr.split('p'))

# for i in range(1,3):
#     print("z")
#     continue
#     print("python")

# for i in range(1,3):
#     for j in range(1,4):
#         print("inner loop")
        
#     print("outer loop")
#     break

# print("program end ")

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("1",end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

n=int(input())
for i in range(1,n):
    for j in range(1,i):
        print("1")