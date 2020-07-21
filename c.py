def readfile():
    file=open("recordfile3/reports.txt")
    count = 0
    c =0
    c1=0

    for i in range(4):
     file_data=file.readline()
     words=file_data.split()
     for word in words:
      print(word)
      count+=1
     if words[0][0] in"aeiou":
          c+=1
     for word1 in words:
         if word=="to":
             c1+=1

    print("vowels:",c)
    print("words:",count)
    print("no. of to:",c1)

readfile()