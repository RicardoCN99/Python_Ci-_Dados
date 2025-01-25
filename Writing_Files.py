with open("file1","w") as f1: # "w" cria ou apaga ficheiro,"a" acrescenta linhas ao ficheiro
    f1.write("Line 1\n")
    f1.write("Line 2\n")
    f1.write("Line 3\n")

with open("file1","r") as f1: #Copia de um ficheiro para outro
    with open("file2","w") as f2:
        for line in f1:
            f2.write(line)

Lista=["Linha 1","Linha 2","Linha 3","Linha 4"]
with open("file3","w") as f3: # Passar lista para ficheiro
    for line in Lista:
        f3.write(line)
        f3.write(".\n")

# Pode-se usar "a+" para acrescentar ou ler ficheiro
# "w+" para escrever ou ler ficheiro
# "r+" para ler ou escrever ficheiro

with open("file3","a+") as f3:
    f3.write("Linha 5.\n") #Ponteiro aponta para linha seguinte
    f3.seek(0) #seek aponta para inicio do ficheiro
    print(f3.read()) # sem o seek começa a ler no fim do ficheiro