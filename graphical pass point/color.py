import tkinter
from tkinter import *
import time

window = tkinter.Tk()

label=tkinter.Label(window, text='''

WELCOME TO GRAPHICAL PASSWORD CREATOR.




''',bg="pink")

label.grid(column=0, row=0)
label.after(4000, label.destroy)

window.update()
time.sleep(4)

login=tkinter.Label(window,text='''Would you like to generate a password or login to the game?

         For generating, press 1

         For login, press 2  ''')
login.grid(column=20, row=0)
generate=tkinter.Label(window, text="Generate/Login")
generate.grid(row=20,column=0)
e3 = tkinter.Entry(window)
e3.grid(row=20, column=20)
login.after(4000, login.destroy)
generate.after(4000, login.destroy)


window.update()
time.sleep(4)
e3.destroy()

w=tkinter.Label(window,text=''' 

           
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
image= tkinter.Label(window, text="Select image",bg="sky blue")
image.grid(row=25,column=0)

e4 = tkinter.Entry(window)

e4.grid(row=25, column=20)

window.update()

time.sleep(4)
e4.destroy()

window.title("Python Tkinter Text Box")
window.update()



window.mainloop()

