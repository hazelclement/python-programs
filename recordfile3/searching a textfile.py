def Common_EmailId():
    file=open("email.txt")
    file_data=file.readlines()
    c=0
    c1=0
    c2=0
    c3=0
    for line in file_data:
        if "gmail.com" in line:
            c+=1
        elif "yahoo.com" in line:
            c1+=1
        elif "hotmail.com" in line:
            c2+=1
        elif "reddif.com" in line:
            c3+=1
    values={c:"gmail",c1:"yahoo",c2:"hotmail",c3:"reddif"}
    max_value=max(c,c1,c2,c3)
    print(values[max_value])
Common_EmailId()