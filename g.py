def readfile():
    file=open("recordfile3/reports.txt")
    lines=file.readlines()
    c=0
    c1=0
    for line in lines:
        c1+=1
        if line[-2]=="y" :
            c+=1

    print("no of lines that end with y:",c)
    print("total no of lines:",c1)
readfile()