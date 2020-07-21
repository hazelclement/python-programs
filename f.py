def readfile():
    f = open("recordfile3/reports.txt")
    f1 = open("cons.txt","w+")
    for line in f:
        for char in line:
            print(char,end="")
            if char not in "aeiou1234567890":
              f1.write(char)

    for k in f1:
        print(k,end="")
    f.close()
    f1.close()
readfile()