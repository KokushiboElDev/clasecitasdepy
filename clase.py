import random #biblioteca

lista = []

numero = int(input("Ingrese un numero: "))

for i in range(1,11):
    print(random.randint(1, 500))
    lista.append(numero*i)
    
print(lista)