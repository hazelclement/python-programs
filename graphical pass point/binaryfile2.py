import pickle
def read():
    file = open("employee.txt", "rb")
    s = []
    try:
        while True:
            s = pickle.load(file)
            print(s)
    except EOFError:
        file.close()

read()