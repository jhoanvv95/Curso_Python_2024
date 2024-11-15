'''  
Contador regresivo
'''

numero_conteo = int(input("Introduce el número inicial del conteno regresivo "))
numero2 = numero_conteo

#Bucle while para el contador regresivo
# print('Ciclo while')
# while numero_conteo >= 0:
#     print(numero_conteo)
#     numero_conteo -= 1

print('Ciclo for')
for i in range(numero2,-1,-1):    
    print(i)