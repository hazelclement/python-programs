def search():
    f=open("email.txt")
    s=f.readlines()
    t=0
    for i in s:
        if "gmail.com" in i:
            t+=1

    print(t)

search()