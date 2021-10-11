# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 18:35:26 2021

@author: Usuario
"""

#ejemplos de funcion PRINT

print("hola mundo")
print("Cristina")
print(1,2,3,4,5)


print(1,2,3,4,5,sep = ("."))  #separa por puntos los elementos
print(1,2,3,4,5,sep = ("-"))  #separa por guiones los elementos
print(1,2,3,4,5,sep = ("/"), end = ("-"))
print(1,2,3,4,5,sep = ("5"), end = "A")


# input
print("bienvenido, cómo te llamas ? ")
nombre = input()
print("gracias por elegirme", nombre)
edad = input("Cuantos años tienes ? ")
print("tienes", edad, "años")


#Listas
lista = ["computadora", "teclado", "mouse",["placa de sonido", "microfono", "parlantes"]]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

#accedo a los distintos elementos de la lista interna
print(lista[3][0])
print(lista[3][1])
print(lista[3][2])


#tuplas
tupla = ("computadora","teclado", "mouse" )
print(tupla)
print(len(tupla))
print(tupla[0])
print(tupla[1])
print(tupla[2])


#diccionarios
mesestraducidos = {"Enero": "January",
                   "Febrero": "February",
                   "Marzo": "March",
                   "Abril": "April",
                   "Mayo": "May",
                   "Junio": "June",
                   "Julio": "July",
                   "Agosto": "August",
                   "Septiembre": "September",
                   "Octubre": "October",
                   "Noviembre": "November",
                   "Diciembre": "December"}

print(mesestraducidos)
print(mesestraducidos["Enero"])
print(mesestraducidos["Febrero"])
print(mesestraducidos["Marzo"])
print(mesestraducidos["Abril"])
print(mesestraducidos["Mayo"])
print(mesestraducidos["Junio"])
print(mesestraducidos["Julio"])
print(mesestraducidos["Agosto"])
print(mesestraducidos["Septiembre"])
print(mesestraducidos["Octubre"])
print(mesestraducidos["Noviembre"])
print(mesestraducidos["Diciembre"])


#CAPITALIZE() - primera letra en mayuscula
cadenaejemplo = "en un lugar de buenos aires..."
print(cadenaejemplo.capitalize())

#UPPER() - pone en mayuscula una cadena de texto
cadenaejemplo = "en un lugar de buenos aires..."
print(cadenaejemplo.upper())

#LOWER() - pone un texto completo en minuscula
cadenaejemplo = "EN UN LUGAR DE BUENOS AIRES..."
print(cadenaejemplo.lower())

#LEN() - saber el nro de caracteres de una cadena
cadenaejemplo = "en un lugar de buenos aires..."
print(len(cadenaejemplo))

#ISALNUM() - comprueba si los elementos de una cadena son alfanumericos o no
cadenaejemplo = "en un lugar de buenos aires..."  #es falso porque el texto tiene espacios
print(cadenaejemplo.isalnum())

cadenaejemplo = "1234567890"
print(cadenaejemplo.isalnum())

cadenaejemplo = "abcdefg123456789"
print(cadenaejemplo.isalnum())

cadenaejemplo = "abcdefg 1234567890" #es falso porque el texto tiene espacio
print(cadenaejemplo.isalnum())

#ISALPHA() - comprueba si todos los caracteres del texto son alfabéticos
cadenaejemplo = "enunlugardebuenosaires"
print(cadenaejemplo.isalpha())

cadenaejemplo = "En un lugar de Buenos Aires..." #los puntos no son caracteres alfabeticos
print(cadenaejemplo.isalpha())

cadenaejemplo = "1234567890"      #los nros no son caracteres alfabeticos
print(cadenaejemplo.isalpha())

cadenaejemplo = "abcdefg 1234567890"   #los espacios no son caracteres alfabeticos
print(cadenaejemplo.isalpha())

#ISDIGIT() - comprueba si todos los caracteres son nros
cadenajemplo = "En un lugar de buenos aires"
print(cadenaejemplo.isdigit())

cadenaejemplo = "1234567890"
print(cadenaejemplo.isdigit())

cadenaejemplo = "abcdefg 1234567890"
print(cadenaejemplo.isdigit())

#ISLOWER() - comprueba si todos los caracteres que componen la cadena son minuscula
cadenaejemplo = "En un lugar de Buenos Aires"
print(cadenaejemplo.islower())
cadenaejemplo = "en un lugar de buenos aires"
print(cadenaejemplo.islower())

#ISUPPER() - comprueba si todos los caracteres que componen la cadena de texto estan enmayuscula
cadenaejemplo = "En un lugar de buenos aires"
print(cadenaejemplo.isupper())
cadenaejemplo = "EN UN LUGAR DE BUENOS AIRES"
print(cadenaejemplo.isupper())

#LSTRIP() - eliminar los caracteres en blanco del comienzo de la cadena
#RSTRIP() - eliminar los caracteres del final de la cadena
#STRIP() - eliminar a la vez los de adelante y los de atras
cadenaejemplo = " en un lugar de buenos aires"
print(cadenaejemplo.lstrip())
cadenaejemplo = "en un lugar de buenos aires "
print(cadenaejemplo.strip())
cadenaejemplo = " en un lugar de buenos aires "
print(cadenaejemplo.strip())

#MAX Y MIX - permite conocer el caracter alfabetico mayor y menor de la cadena de texto
cadenaejemplo ="abcdefghijklmnopqrstuvwxyz"
print(max(cadenaejemplo))
print(min(cadenaejemplo))

#REPLACE - permite reemplazar caracteres de la cadena de texto por otros caracteres
cadenaejemplo = "AEIOU"
print(cadenaejemplo.replace("A", "E"))

#SWAPCASE - invierte mayusculas y minusculas en la cadena de texto
cadenaejemplo = "En un lugar de buenos aires"
print(cadenaejemplo.swapcase())

#SPLIT() - convierte una cadena de texto en una lista de elementos separados por espacios
#en la cadena de texto originar

cadenaejemplo = "En un lugar de buenos aires"
print(cadenaejemplo.split())

cadenaejemplo = "31/12/2020"
print(cadenaejemplo.split("/"))
