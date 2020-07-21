import pickle
def create():
    file=open("employee.txt","wb+")
    no=int(input("enter number of employees:"))
    for i in range(no):
        eno=int(input("enter employee number:"))
        ename=input("enter employee name:")
        desig=input("enter designation:")
        salary=int(input("enter salary"))
        t=[eno,ename,desig,salary]
        pickle.dump(t,file)

    file.close()
create()