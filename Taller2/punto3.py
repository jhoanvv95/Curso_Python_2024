''' 
Una institución educativa utiliza el siguiente sistema de calificaciones para evaluar el desempeño de sus estudiantes:
Superior: 90 - 100
Alto: 80 - 89
Básico: 70 - 79
Bajo: 60 - 69
Insuficiente: 0 - 59
Crea un programa que permita calcular la calificación final de un estudiante a partir del promedio de sus notas.
El programa debe pedir el nombre del estudiante y sus calificaciones en tres evaluaciones.
Luego, debe calcular el promedio de las notas.
Con base en el promedio, el programa debe asignar la calificación correspondiente (Superior, Alto, Básico, Bajo o Insuficiente) y mostrar el resultado.
Ejemplo de entrada:
María tiene las siguientes notas: 80, 90, 100. ¿Qué calificación sacaría María?
Sergio tiene las siguientes notas: 65, 100, 70. ¿Qué calificación sacaría Sergio?
Salida esperada: El programa debe mostrar el nombre del estudiante, su promedio de notas y la calificación final.


'''

nombre = input('Ingrese el nombre del estudiante: ')
calificacion1 = int(input('Ingrese la calificación 1: '))
calificacion2 = int(input('Ingrese la calificación 2: '))
calificacion3 = int(input('Ingrese la calificación 3: '))


def calcular_promedio(nota1, nota2, nota3):
  promedio_cal = ((nota1+nota2+nota3)/3)
  return promedio_cal

promedio = calcular_promedio(calificacion1,calificacion2,calificacion3)

def nota_final(promedio):
  
  if promedio < 59:
    calificacion = 'Insuficiente'
  elif  promedio < 69: 
    calificacion = 'Bajo'
  elif  promedio < 79: 
    calificacion = 'Básico'    
  elif  promedio < 89: 
    calificacion = 'Alto'    
  else:
        calificacion = 'Superior'    
  return calificacion


nota = nota_final(promedio)

print('El promedio  del estudiante: ',nombre, ' es:',promedio, ' y su calificación final es: ',nota )