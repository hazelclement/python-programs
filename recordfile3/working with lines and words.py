def separator():
    file=open("text.txt")
    for i in range(5):
      file_data=file.readline()
      for word in file_data:
          if word==" ":
              print("#",end="")
          else:
              print(word,end="")

separator()