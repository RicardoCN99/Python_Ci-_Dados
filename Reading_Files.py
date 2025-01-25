with open("file","r") as file1:  
    file_stuff=file1.readline(4) # lê primeiros 4 caracteres
    print(file_stuff)
    file_stuff=file1.readline() #lê primeira linha
    print(file_stuff)

    file_stuff=file1.readlines()
    print(file_stuff)
    file1.seek(0)
    print(file1.read())
    print(file1.name) #apresenta nome do ficheiro

print(file1.closed)
print(file_stuff)
print("Primeira linha:",file_stuff[0])

with open("file","r") as f1:
    for line in f1:
        print(line)

# with-- fecha leitura do ficheiro automaticamente

#("file","r") 1º nome do ficheiro, 2º modo (r-leitura,w-escrita,a-acrescenta ao que já existe no ficheiro)

