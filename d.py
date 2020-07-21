def readfile():
    f = open("recordfile3/reports.txt")
    f1 = open("copy.txt","w")
    for line in f:
        f1.write(line)
    f.close()
    f1.close()
readfile()