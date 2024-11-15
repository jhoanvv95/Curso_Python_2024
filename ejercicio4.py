'''  crear un programa que cuente los numeros impares del 1 al 9'''



i = 0
contador_impares = 0

while i < 9:
    i+=1
    if i%2 != 0: 
        contador_impares = contador_impares +1
        print('Numero impar: ',i)
    
print('El total de numeros impares es: ',contador_impares)

