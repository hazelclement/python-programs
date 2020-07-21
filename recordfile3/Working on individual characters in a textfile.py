def count():
    file=open("notes.txt")
    file_data=file.read()
    count=0
    count1=0
    for word in file_data:
            print(word,end="")
            if word==",":
                count+=1
            if word==".":
                count1+=1

    print()
    print("the number of , is:",count)
    print("the number of . is:",count1)

count()