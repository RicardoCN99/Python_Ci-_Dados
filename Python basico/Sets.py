#Sets-- input podem ser varios tipos, diferente de tuplos e listas não são ordenados, apenas aceita 1 elemento de cada

Set1={1,2,3.1,"ai","ai","um dois tres"}
print(Set1) # 1 "ai" é eliminado do set

Lista=[1,2,3.1,"ai","ai","um dois tres"]
Lista_para_Set=set(Lista)  # Transforma lista em set( elimina duplicados)
print(Lista_para_Set)

Set1.add("UIUIUI")  #adiciona elemento
print(Set1)  

Set1.remove("ai")  # remove elemento (como duplicados são logo removidos, Set1 fica sem nenhum "ai")
print(Set1)

print("um dois tres" in Set1)
print("um dois" in Set1)

intercecao_de_sets= Set1 & Lista_para_Set  #cria set com interseçao entre os 2 sets
print(intercecao_de_sets)

uniao_de_sets=Set1.union(Lista_para_Set)
print(uniao_de_sets)

Set3={1,2}
print(Set3.issubset(Set1)) #true se todos os elementos de set3 existirem no set1

SomaSet3=sum(Set3) #Soma set
print(SomaSet3)