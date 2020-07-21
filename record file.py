'''Write a program to print every number between 2 and n, divisible by m.Accept
m and n from the user.'''
m=int(input("input divisor:"))
n=int(input("input range:"))

for i in range(2,n):
    if i % m == 0:
        print(i,sep=",",end="")
    else:
        pass