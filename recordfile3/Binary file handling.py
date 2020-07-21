n=int(input("Enter no of records"))
import pickle
def create():
    f1=open('binfile','wb')
    for i in range(n):
        s=[]
        sno=eval(input("Enter sno: "))
        s.append(sno)
        sname=input("Enter snmae: ")
        s.append(sname)
        marks=eval(input("Enter marks :"))
        s.append(marks)
        pickle.dump(s,f1)
    f1.close()
def add():
    s=[]
    sno=eval(input("Enter sno: "))
    s.append(sno)
    sname=input("Enter snmae: ")
    s.append(sname)
    marks=eval(input("Enter marks :"))
    s.append(marks)
    f1=open('binfile',"ab")
    pickle.dump(s,f1)
    f1.close()
    read_add()
def marks_modify():
    f1=open("binfile","rb+")
    sno=eval(input("Enter sno: "))
    marks=eval(input("Enter marks :"))
    try:
        while True:
            pos=f1.tell()
            s=pickle.load(f1)
            if s[0]==sno:
                s[2]=marks
                f1.seek(pos)
                pickle.dump(s,f1)
                print("Record updated")
                break
    except EOFError:
        print("Detail not found")
    f1.close()
    read()
def name_modify():
    s=[]
    f1=open("binfile","rb+")
    sno=eval(input("Enter sno: "))
    sname=input("Enter sname :")
    try:
        while True:
            pos=f1.tell()
            s=pickle.load(f1)
            if s[0]==sno:
                s[1]=sname
                f1.seek(pos)
                pickle.dump(s,f1)
                print("Record updated")
                break
    except EOFError:
        print("Detail not found")
    f1.close()
    read()
def menu():
    print("a.Add a record")
    print("b.Display all records")
    print("c.Accept Sno and modify the marks of that student ")
    print("d.Accept Sno and modify the name of that student.")
    ch=input("Make your choice")
    if ch=="a":
        add()
    if ch=="b":
        read()
    if ch=="c":
        marks_modify()
    if ch=="d":
        name_modify()
def read_add():
    f1=open("binfile","rb")
    for i in range(n+1):
        s=[]
        s=pickle.load(f1)
        print(s)
    f1.close()
create()
menu()
def read():
    f1=open("binfile","rb")
    for i in range(n):
        s1=[]
        s1=pickle.load(f1)
        print(s1)
    f1.close()