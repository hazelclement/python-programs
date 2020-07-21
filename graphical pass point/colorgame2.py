import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class Password(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='''

WELCOME TO GRAPHICAL PASSWORD CREATOR.




        
        
        ''', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text='''Login''',
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Generate",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageOne(tk.Frame):
    passwd = tk.StringVar()
    passwd_var.set("")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,textvariable=passwd_var, text='''
        
Enter Username  
1.Create a password of at least 8 characters.
        
2.Include both uppercase and lowercase letters.
        
3.Include numbers and special characters[ @ , ? , ! , _ ]
        
NOTE: Do not use blankspace in the password. 
         
         
         
         ''', justify=tk.LEFT ,font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        E1 = tk.Entry(self,bd=5)
        E1.pack()
        result=E1.get()
        button2 = tk.Button(self, text="Select Image",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        print(result)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='''

           
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
         
         

''',justify=tk.LEFT, font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        E2 = tk.Entry(self, bd=5)
        E2.pack()
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


app = Password()
app.mainloop()