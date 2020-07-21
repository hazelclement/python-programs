def create():
    data=input("Enter data: ")
    f1=open("lower.txt","w")
    f2=open("upper.txt","w")
    f3=open("others.txt","w")
    for char in data:
        if char.islower():
            f1.write(char)
        if char.isupper():
            f2.write(char)
        if char.isupper()==False and char.islower()==False:
            f3.write(char)
    f1.close()
    f2.close()
    f3.close()

def read():
    f1=open("lower.txt","r")
    f2=open("upper.txt","r")
    f3=open("others.txt","r")
    lower=f1.read()
    upper=f2.read()
    others=f3.read()
    print("LOWER CASE :",lower)
    print("UPPER CASE: ",upper)
    print("SPECIAL CHARACTERS: ",others)
create()
read()