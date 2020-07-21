def readfile():
    file=open("recordfile3/reports.txt")
    last=file.readlines()
    print(last[-1])
readfile()