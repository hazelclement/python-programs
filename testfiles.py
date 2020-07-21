def readfile():
    file=open("text.txt")
    str=file.read()

    for char in str:
        if char=="k":
            print("a",end="")
        else:
            print(char,end="")

readfile()
