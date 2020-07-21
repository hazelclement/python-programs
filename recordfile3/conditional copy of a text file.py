def sports():
    file=open("sports.txt")
    file_data=file.readlines()
    files=open("athletics.txt","a+")
    for line in file_data:
        if "athletics" in line:
            print(line,end="")
            files.write(line)
sports()