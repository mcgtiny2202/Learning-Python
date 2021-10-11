# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 14:28:26 2021

@author: Usuario
"""

#practica lista
lista = ["computadora", "teclado", "mouse"]
print(lista)
print(len(lista))
print(lista[0])
print(lista[1])
print(lista[2])
lista[0]= "monitor"
lista[1]= "impresora"
lista[2]= "parlantes"
print(lista)

lista = lista + ["mesa"]
print(lista)


listaoriginal = ["computadora", "teclado", "mouse"]
listanueva = ["monitor", "impresora", "parlantes"]
listafinal = listaoriginal + listanueva
print(listafinal)

