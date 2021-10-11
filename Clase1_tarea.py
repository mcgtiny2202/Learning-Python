# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 17:42:11 2021

@author: Usuario
"""

# Ejercicio 1
# Escribir un programa que muestre por pantalla la cadena “¡Hola Mundo!”

print("Hola Mundo")


# Ejercicio 2
# Escribir un programa que almacene la cadena “¡Hola Mundo!” en una variable y luego muestre 
# por pantalla el contenido de la variable.

cadena = "¡Hola Mundo!"
print(cadena)


# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el 
# usuario lo introduzca muestre por pantalla la cadena “¡Hola <nombre>!”, donde <nombre> es 
# el nombre que el usuario haya introducido.

nombre = input("Cuál es tu nombre? ")
print("Hola", nombre ,end = '!')


# Ejercicio 4
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación
# aritmética   

# ((3+2) / (2*5))^2


valor1 = 3+2
valor2 = 2*5

resultado = (valor1 / valor2)**2

print(resultado)


# Ejercicio 5
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo 
# por hora. Después debe mostrar por pantalla el sueldo que le corresponde.

horas = int(input("Cuantas horas trabajas ? "))
costo = int(input("Cual es el costo de la hora ? "))
sueldo = horas * costo
print('El sueldo que corresponde es: ', sueldo)


# Ejercicio 6
# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después 
# muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los números 
# enteros positivos puede ser calculada de la siguiente forma: 

n = int(input("Ingrese el valor de n: "))    
suma = (n*(n+1)) / 2
print("La suma de nros enteros positivos es: ", suma)  


# Ejercicio 7
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule 
# el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase 
# “Tu índice de masa corporal es <imc>”, donde <imc> es el índice de masa corporal calculado 
# redondeado con dos decimales.

peso = float(input("Cual es tu peso: ? "))
estatura = float(input("Cual es tu estatura: ? "))
imc = peso / ((estatura)**2)
print("Tu indice de masa corporal es: ", round(imc,2))


# Ejercicio 8
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la 
# frase “<n> entre <m> da un cociente <c> y un resto <r>” donde <n> y <m> son los números 
# introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera 
# respectivamente.

n = int(input("Ingrese el primer nro: "))
m = int(input("Ingrese el segundo nro: "))
c = n // m
r = n % m

print(n, 'entre', m, 'da un cociente', c, 'y un resto', r)


# Ejercicio 9
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
# el número de años, y muestre por pantalla el capital obtenido en la inversión

# M = C × (1 + i)n​

capital = int(input("Ingresa el monto a invertir: "))
i = float(input("Ingresa la tasa de interes anual: "))
n = int(input("Ingresa la cantidad de años: "))

Monto = capital * ((1+i)**n)
print("El capital obtenido en la inversion es: ",Monto)


# Ejercicio 10
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer 
# venta por correo y la empresa de logística les cobra por peso de cada paquete así que 
# deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de 
# payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que 
# será enviado.

peso_payaso = 112
peso_muñeca = 75

cant_payasos = int(input("Ingrese la cantidad de payasos vendidos: "))
cant_muñecas = int(input("Ingrese la cantidad de muñecas vendidas: "))

payasos = peso_payaso * cant_payasos
muñecas = peso_muñeca * cant_muñecas

total_paquete = payasos + muñecas
print("El peso total del paquete en grs es: ", total_paquete)


# Ejercicio 11
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero 
# e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número 
# introducido.

nombre = input("Ingresa tu nombre: ")
numero = input("Ingresa un nro entero: ")
print((nombre +"\n") * int(numero))


# Ejercicio 12
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después 
# muestre por pantalla el nombre completo del usuario dos veces, una con todas las letras 
# minúsculas y otra con todas las letras mayúsculas. El usuario puede introducir su nombre 
# combinando mayúsculas y minúsculas como quiera.

nombre = input("Cual es tu nombre ? ")
print("Nombre en mayuscula: " , nombre.upper())
print("Nombre en minuscula: " , nombre.lower())
print("Nombre combinado: ", nombre.title())   #muestra combinadas
print("Nombre combinado: ", nombre.capitalize()) 


# Ejercicio 13
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo, Matemáticas, 
# Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

asignaturas = ['Matematicas','Fisica','Quimica','Historia','Lengua']
print("Lista de asignaturas:" ,asignaturas)


# Ejercicio 14
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo, Matemáticas, 
# Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje 
# Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista


asignaturas = ['Matematicas','Fisica','Quimica','Historia','Lengua']
print("Yo estudio: ", asignaturas[2])
