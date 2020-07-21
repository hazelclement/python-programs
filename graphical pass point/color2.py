import tkinter
from tkinter import *
import time
import colorgame2

root = tkinter.Tk()

label=tkinter.Label(root, text='''

WELCOME TO GRAPHICAL PASSWORD CREATOR.




''',bg="pink")

label.grid(column=0, row=0)
label.after(4000, label.destroy)

root.update()
time.sleep(4)


login.grid(column=20, row=0)
generate=tkinter.Label(root, text="Generate/Login")
generate.grid(row=20,column=0)
e3 = tkinter.Entry(root)
e3.grid(row=20, column=20)
value=e3.get()
print(value)
login.after(4000, login.destroy)
generate.after(4000, login.destroy)

fields = 'Generate/Login', 'Select image ', 'Username'

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text))

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tkinter.Frame(root)
        lab = tkinter.Label(row, width=15, text=field, anchor='w')
        ent = tkinter.Entry(row)
        row.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        lab.pack(side=tkinter.LEFT)
        ent.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.X)
        entries.append((field, ent))
    return entries

if __name__ == '__main__':
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = tkinter.Button(root, text='Show',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tkinter.LEFT, padx=5, pady=5)
    b2 = tkinter.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tkinter.LEFT, padx=5, pady=5)
    root.mainloop()

s=e3.get()
value=tkinter.Label(root,text=s)
root.update()
time.sleep(4)
e3.destroy()

w=tkinter.Label(root,text=''' 

           
          To select an image::             
          1.Burj khalifa.jpg            
          2.Chocolate lava cake.jpg           
          3.Eiffel tower.jpg         
          4.Hogwarts.jpg         
          5.Lemonade.jpg           
          6.Lighthouse.jpg            
          7.Mt fuji.jpg           
          8.Pizza.jpg           
          9.Taj Mahal.jpg          
         10.Elephants.jpg       
         
         

''',anchor=N)
w.grid(column=10, row=0)
image= tkinter.Label(root, text="Select image",bg="sky blue")
image.grid(row=25,column=0)

e4 = tkinter.Entry(root)

e4.grid(row=25, column=20)

root.update()

time.sleep(4)
e4.destroy()
root.update()

root.title("Python Tkinter Text Box")



root.mainloop()

