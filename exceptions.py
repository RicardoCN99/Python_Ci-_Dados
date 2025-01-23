try:
    getfile=open("file","r") #Se ocorrer erro, passa para except e procura erro e print associado
    getfile.write("Exceptions handling")
except IOError:
    print("Unable to open or read the data")    
   