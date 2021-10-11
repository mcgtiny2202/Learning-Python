# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 21:18:39 2021

@author: Usuario
"""

#EJERCICIOS DE CONDICIONALES

# EJERCICIO 1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de 
# edad o no.


edad = int(input("Qué edad tienes ? "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    
    
#******************************************************************************

# EJERCICIO 2
# Escribir un programa que almacene la cadena de caracteres <contraseña> en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y 
# minúsculas.
    
variable1 = "contraseña"
cont_usuario = input("Cuál es tu contraseña? ") 

if cont_usuario == variable1:
    print("La contraseña coincide")
else: 
    print("La contraseña NO coincide")
    
    
#*****************************************************************************

# EJERCICIO 3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.
   
num1 = int(input("Ingrese el primer nro: "))
num2 = int(input("Ingrese el segundo nro: "))

if num2 != 0:
    print("El resultado de la division es: ", num1/num2)
else:
    print("El nro debe ser distinto de 0")

#*****************************************************************************

# EJERCICIO 4
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par
#  o impar.

numero = int(input("Ingrese un nro: "))

if (numero % 2) == 0:
    print("El nro ingresado es par")
else:
    print("Error")
    

#*****************************************************************************

# EJERCICIO 5
# Para tributar ganancias, se debe ser mayor de 18 años y tener unos ingresos iguales o 
# superiores a $175.000 mensuales. Escribir un programa que pregunte al usuario su edad y 
# sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
    

edad = int(input("Cuál es tu edad ? "))
ingresos = float(input("Cual es tu ingreso mensual ? "))

if (edad > 18)  and (ingresos >= 175000):
    print("El usuario debe tributar ganancias")
else:
    print("El usuario no debe tributar ganancias")
    

#*****************************************************************************

# EJERCICIO 6
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un 
# nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al 
# usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


nombre = input("Cuál es tu nombre: ? ")
print(nombre)
sexo = input("Cual es tu sexo: ? ")
print(sexo)

# print(nombre[0])
# print(nombre[0]< 'M')


if (sexo == "mujer") and (nombre[0]< 'M'):
    print("Pertenece al gruoo A")
elif (sexo == "hombre") and (nombre[0]> 'N'):
    print("Pertenece al grupo A")
else:
    print("Pertenece al grupo B")
            