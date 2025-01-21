a=0
b=20
while b<201:
    while a<=b:
        if a<b:
            with open("file1","a") as file1:
                file1.write(str(a)+",")
        else:
             with open("file1","a") as file1:
                file1.write(str(a))        
        a=a+1
    with open("file1","a") as file1:    
        file1.write("\n")    
    b=b+20