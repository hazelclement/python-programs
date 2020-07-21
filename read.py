def readfile():
    files=open("recordfile3/reports.txt")
    file=files.read()

    for i in range(0,len(file)):
        print(file[i],end="")
    print()
    print("char:",len(file))

    count=1
    count1 = 0
    count2 = 0
    c=0
    a=True
    for char in file:
        print(char,end="")
        if char.isupper():
            count1+=1
        if char.isdigit():
            count2+=1
        if char=="\n":
            count+=1





    print("u:",count1)
    print("d:",count2)
    print("line:",count)
    print("y:",c)
readfile()