import random as r
def len_no(n):

    x = ""
    y = "1"
    for i in range(n):
        x += "9"
    v = int(x)

    for p in range(n - 1):
        y += "0"
    w = int(y)

    number=r.randrange(w,v)
    return number
n = int(input(":"))
print(len_no(n))