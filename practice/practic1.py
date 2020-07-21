with open('mynote.txt','r') as f1:
    f1.seek(0,2)
    print(f1.tell())
    curpos=f1.tell()
    f1.seek(curpos-3)
    print(f1.read(1))