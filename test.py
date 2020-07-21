a=int(input("Number1:"))
b=int(input("Number2:"))

i,j = str(a),str(b)
m,n = len(str(a)),len(str(b))
print(m,n)
c,d = i[n-1],j[m-1]
if c<d:
    print(a)
elif d>c:
    print(b)


