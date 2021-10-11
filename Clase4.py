# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 19:02:09 2021

@author: Usuario
"""

# Bucle WHILE

# Recomendado para contextos en los que no se sabe exactamente el nro de iteraciones que se
# tienen que ejecutar.
# Se ejecutan iteraciones hasta que deje de cumplirse una condición.

# La condición que se utiliza para comprobar si se tiene que ejecutar una iteración deberá ser
# TRUE para que se ejecute.  Si la condición es FALSE, la ejecución finalizará.

# La condición es comprobada en cada iteración del bucle.
# Las variables que se utilizan en la iteración del bucle se llaman variables de control


i = 0
while i<10:
    print (i,end=" ")
    i = i+1
    

# En el siguiente ejercicio la condición es un booleano que cambiará de valor si el nro que introduce
# el usuario dentro del bucle es superior a 100.
    
continuar = True
while continuar:
    valor = int(input("Ingrese un nro superior a 100: "))
    if valor > 100:
        continuar = False
        
print("Programa acabado")        



# Bucle for

# Recomendado para contextos en los que se sabe el nro de iteraciones exactas que se van a dar
# en ejecución.
# Busca ejecutar un conjunto de instrucciones de forma repetitiva hasta llegar al máximo nro de
# iteraciones definidas
# Se usan en listas, tuplas, cadenas de texto o diccionarios.
# El nro de iteraciones que se ejecutarán dependerá del nro de elementos de los que está compuest
# el elemento iterable

lista = [1,2,3,4,5,6,7,8,9]
for item in lista:
    print(item, end="\n")
    
    
#se recorre una lista de cadena de texto

lista = ["computadora", "teclado", "mouse"]
for item in lista:
    print(item, end= " ")
    
    
# en el siguiente ejemplo se ejecuta un bucle for por sobre los elementos que devuelve la
# instruccion RANGE.  Nos va a permitir tener una lista secuencial de elementos enteros empezando por 0
# y con tantos elementos como se indique en el parametro.
    

for item in range(10):
    print(item, end=" ")
    


# BUCLES ANIDADOS

# Utilizacion de bucles como parte de los bloques de instrucciones de otros bucles
# El bucle que se encuentra dentro de otro bucle se llama bucle interno o interior.
# El bucle que contiene un bucle interior se llama bucle externo o exterior


for item1 in range(3):
    for item2 in range(5):
        print("item1 = " + str(item1) + " item2 = " + str(item2))
    
for item1 in range(3):
    for item2 in range(5):
        print(str(item1) + "  " + str(item2))    
    print("---------- ")        
    

# En el siguiente ejemplo se anida un bucle WHILE y un bucle FOR
# El nro de iteraciones del bucle WHILE viene dado por item1, variable inicializada
# antes de declarar el bucle y que irá incrementando su valor dentro del bucle a medida
# que ese ejecuta cada iteración del bucle

item1 = 0
while item1 <3:
    for item2 in range(5):
        print("item1 = " + str(item1) + " item2 = " + str(item2))
    item1 = item1 + 1
    
    
item1 = 0
while item1 <3:
    for item2 in range(5):
        print(str(item1) + "  " + str(item2))
    print("---------- ")     
    item1 = item1 + 1    
    
    
# Anidamiento de dos bucles WHILE 

item1 = 0
while item1 <3:
      item2 = 0
      while item2 in range(5):
          print("item1 = " + str(item1) + " item2 = " + str(item2))
          item2 = item2 + 1
      item1 = item1 + 1
          
      
item1 = 0
while item1 <3:
      item2 = 0
      while item2 in range(5):
          print(str(item1) + "  " + str(item2))
          
          item2 = item2 + 1
      print("---------- ")
      item1 = item1 + 1       
      
      
      