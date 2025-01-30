#funções do python

lista=[1,2,3,4,5] 

print(len(lista)) #função que retorna numero de elementos da lista/tuple/dicionario

print(sum(lista)) #função retorna soma 

lista2=["u","i","o","a","e"]
print(sorted(lista2))  #função retorna lista ordenada mas não troca valores da lista
print(lista2)

lista_ordenada=sorted(lista2) #para obter lista ordenada permanente
print((lista_ordenada))

lista2.sort() # metodo muda valores da própria lista e ordena
print(lista2)

#---------------------------Criar funções--------------------------------------------

def soma1(a):
    """
    Posso commentar e utilizar o comando "help(soma1)" para ver todos os comentários da função
    """
    b=a+1
    return b

d=5
c=soma1(d) #função não muda valor da variavel global que entra

print(c)

help(soma1)

#-----------------

def multiplica(a,b):
    c=a*b
    return c

r=multiplica(d,c)
print(r)

#-----------------

nome="Ricardo"
nome5x=multiplica(d,nome) #Passo um numero e uma string e multiplico o nome pelo numero sem dar erro
print(nome5x)

#----------------

def printaNome(a): #Não precisa retornar nada, não dá erro
    print(a)

def naoFazNada(): # Dá erro se não colocar nada dentro da função, coloca-se pass e ela retorna "None"
    pass

printaNome(nome) 
print(naoFazNada())

#----------------

def printaCoisas(coisas):
    for i,s in enumerate(coisas):
        print("album", i+1, "rating", s) 

rating_albuns=[10,3.5,8,7.4]
printaCoisas(rating_albuns)

#----------------

def printaNomes(nomes): 
    for nome in nomes:
        print(nome)

tuple_nomes=("João","António","Quim","Ricardo")
printaNomes(tuple_nomes)

#----------------

def exEscopo(): # Defini o escopo global de uma variavel dentro da função
    global x
    x=66
    return x

exEscopo() #Variavel pode ser chamada fora da função depois de chamar a função
print(x)