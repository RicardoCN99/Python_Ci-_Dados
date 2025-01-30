a=0
while(a!=4):
    a=input("Digite um numero de 1 a 3 (4 para sair):")

    a=int(a)
    lista=[1,2,3.4,"ui"]
    lista.append(["aiai",3,True]) # acrescenta lista a lista com um unico elemento
    if(a==1):
        print("ai")
        print(1+1)

    if(a==2):
        print(lista)
        print(lista[1])

    if(a==3):
        print(lista)
        print(lista[4][0])

b = "s"
print("---------------------------------------------")
print("---------------Dicionario--------------------")
print("---------------------------------------------")
dicionario={}
while(b!="n"):
    nome=input("chave: ")
    valor=input("Valor: ")
    dicionario[nome]=valor
    b=(input("Continuar? (s/n): "))

print(dicionario)

print(dicionario["lele"])

keys_list =dicionario.keys()
print(keys_list)