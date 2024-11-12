'''   
Crear una aplicación Para un centro deportivo (GIMNASIO) que cuenta con las siguientes características
-   	Bronce – Plata – Oro, dicha clasificación es determinada por el número de horas que realiza en el mes.

Nombre Plan:
Bronce  (0 -- 15]
Plata (15 -- 30]
Oro   >= 30

Valor por hora:
Bronce 5.000
Plata 3.500
Oro 2.000 

Hacer un programa en Python 
Para la gestión del centro deportivo.
-   	La facturación del servicio y descuento aplicado

'''

nombre = input('Ingrese el nombre del usuario:  ')
horas = int(input('Ingrese el numero de horas:  '))

vplan_bronce = 5000 
vplan_plata =  3500
vplan_oro =    2000
valor_mes = 0



if horas < 15: 
    valor_mes = horas*vplan_bronce

elif horas < 30:
    valor_mes = horas * vplan_plata
else :
    valor_mes = horas * vplan_oro

    
print('El valor a pagar por el mes es para el cliente: ' ,nombre, ' es: ',valor_mes,'$')




# # Opción 2 


# def calculo(horas, vplan_bronce, vplan_plata, vplan_oro):
#     if horas < 15: 
#         valor_mes = horas * vplan_bronce
#     elif horas < 30:
#         valor_mes = horas * vplan_plata
#     else:
#         valor_mes = horas * vplan_oro
#     return valor_mes

# valor_mes = calculo(horas, vplan_bronce, vplan_plata, vplan_oro)


# print('El valor a pagar por el mes es para el cliente: ' ,nombre, ' es: ',valor_mes)