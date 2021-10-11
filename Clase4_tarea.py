# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 19:50:45 2021

@author: Usuario
"""

# EJERCICIO1
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.


palabra = input("Ingresa una palabra: ")
for item in range(10):
    print(palabra, end="\n")
    
# --------------------------------------------------------------------------------------------  

# EJERCICIO2
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años 
# que ha cumplido (desde 1 hasta su edad).
  

edad = int(input("Ingresa tu edad: "))

for item in range(edad):
    print(item+1 , "años cumplidos")
    
    
#---------------------------------------------------------------------------------------------

# EJERCICIO3
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
# todos los números impares desde 1 hasta ese número separados por comas. 

numero = int(input("Ingrese un nro entero positivo: "))

for item in range(numero):
    if (item % 2 != 0):
        print(item, end=",")

# if(numero % 2 !=0):
#     print(numero)
    

#--------------------------------------------------------------------------------------------

# EJERCICIO4
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


for x in range(0,10 + 1):
    print("Tabla de multiplicar de ", x)
    for y in range(0,10 + 1):
        print(f'{x} x {y} = {x*y}')
        #print(x, 'x', y = (x * y))


# ------------------------------------------------------------------------------------------

# EJERCICIO5
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


var1 = "contraseña"
continuar = True
while continuar:
    var2 = input("Ingrese la contraseña: ")
    if var1 == var2:
        continuar = False
   
    
print("Programa finalizado")        


#------------------------------------------------------------------------------------------

# EJERCICIO6
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el 
# usuario escriba “salir” que terminará.


continuar = True
while continuar:
    var1 = input("-> ")
    if var1 == 'salir':
        continuar = False
        print("El programa ha terminado")


    