'''create a textfile text and do the following:
count no of characters words and lines
display only digits in it
make a copy into copy.txt. all words beginning with t omitted.'''

def file():
 c = 0
 c1 = 1
 c2 = 1
 file = open("text.txt")
 file_data = file.read()
 word = file_data.split()
 for i in file_data:
     c+=1
     if i==" ":
         c1+=1
     elif i =="/n":
         c2+=1
     elif i in "1234567890":
         print(i,end="")

 print()
 print("the no of characters is:",c)
 print("the no of words is:",c1)
 print("the no of lines is",c2)

 file_data2=file.readlines()
 for i in file_data2:
     print(i,sep=",")
file()