def readfile():
    f = open("recordfile3/reports.txt")
    f1 = open("digits.txt","w")
    for line in f:
        for char in line:
            print(char)
            if char in "1234567890":
              f1.write(char)
            print(f1)
    f.close()
    f1.close()
readfile()