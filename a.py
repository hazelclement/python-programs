def readfile():
    file=open("recordfile3/reports.txt")
    for i in range(3):
      file_line=file.readline()
      print(file_line)
readfile()