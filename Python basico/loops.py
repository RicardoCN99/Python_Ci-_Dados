#LOOP---FOR

array=[9,9,9,9,9]

for i in range(5):
    array[i]=i

print(array) # altera para [0,1,2,3,4]

#------------------------------------------------------

array=[8,8,8]

for i in range(0,3):
    array[i]=i

print(array) # altera para [0,1,2]

#------------------------------------------------------

squares=("blue","white","yellow","black")

for i in squares: # posso iterar sobre tuple diretamente, sem usar indice
    print(i)

#-------------------------------------------------------

for i,square in enumerate(squares): # se necessário indice ussa-se função enumerate
    print(i,square)

#LOOP---WHILE

square_list=list(squares)
square_list.extend(["green","brown"])

i=0

while square_list[i]!="green":
    print("wrong square, ",square_list[i])
    i=i+1

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i=0

while i<len(squares) and squares[i]=="orange":
    new_squares.append(squares[i])
    i=i+1

print(new_squares)