# Cada vez que instâncio uma variavel (List,float,int,string,dicionary), crio um objeto.
# Cada objeto tem um tipo(float,int),metodos(sort(),reverse())

class Circl(object):
    diameter=10

    def __init__(self,radius,color): # Sintaxe de iniciação de objeto / Construtor
        self.radius=radius      # self para atribuir valores ao objeto
        self.color=color
    def changeRadius(self,r):
        self.radius=self.radius+r

circulo1=Circl(6,"red") # instância objeto
print(circulo1.radius)

print(circulo1.diameter) #Posso criar atributos padrões antes de iniciar Construtor

circulo1.color="white" 
print(circulo1.color)#Dá para mudar atributo diretamente mas é boa prática criar metodos dentro da classe

circulo1.changeRadius(6) # Para alterar atributos do objeto
print(circulo1.radius)

print(dir(circulo1))  # dir(NomeDoObjeto) para verificar atributos


class Car(object):
    color="white"
    def __init__(self,maxSpeed,mileage):
        self.maxSpeed=maxSpeed
        self.mileage=mileage
    def seatingCapacity(self,sc):
        self.seatingCapacity=sc
    def displayProperties(self):
        print("color=",self.color)
        print("maxSpeed=",self.maxSpeed)
        print("Maximum Speed:", self.maxSpeed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seatingCapacity)

car1=Car(200,20)
car1.seatingCapacity(5) #Para chamar metodo dentro de Classe faz-se obj.metodo
car1.displayProperties()

car2=Car(180,25)
car2.seatingCapacity(4)
car2.displayProperties()