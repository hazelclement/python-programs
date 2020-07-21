def modify():
    file=open("original.txt")
    file_data=file.readlines()
    files=open("copy.txt","a+")
    for line in file_data:
        if "a" in line:
            pass
        else:
            files.write(line)
modify()