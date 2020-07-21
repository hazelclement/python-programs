
def series(x,y):
    a=(x+y)//4
    l =

    for i in range(3):
        x=x+a
        l+=[x]
    return l
x=int(input(":"))
y=int(input(":"))
print(series(x,y))