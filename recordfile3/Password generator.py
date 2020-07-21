import os
def password_generator():
    count=0
    user_id=input("Enter UserId:")
    passwd_file=open("../graphical pass point/security.txt", "r+")
    is_present = False
    run=True
    running=True
    while running:
     for line in passwd_file.readlines():
        if line.strip() == user_id:
            is_present = True
     if is_present:
        print("The User Name already exists.")
        user_id = input("Enter UserId:")

     else:
        running=False

        passwd_file.seek(0,os.SEEK_END)
        passwd_file.write(user_id)


    while run:
     password=input("Enter password:")
     if len(password)<8:
        print("Password must be of more than 8 characters")
     elif password.isalpha():
        print("Error! Must contain digit")
     if password.count("%")==0 and password.count("@")==0 and password.count("$")==0 :
        print("Error! Must contain special characters")
     else:
        run=False
        word=" ,"+password+"\n"
        passwd_file.write(word)
password_generator()