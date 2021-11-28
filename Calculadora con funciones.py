# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:12:50 2021

@author: Usuario
"""

# calculadora con funciones


def sumar(num1,num2):
    num1 = int(input("ingrese un nro: "))
    num2 = int(input("ingrese un nro: "))
    print("Resultado: ",num1+num2)
    return num1+num2


def restar(num1,num2):
    num1 = int(input("ingrese un nro: "))
    num2 = int(input("ingrese un nro: "))
    print("Resultado: ",num1-num2)
    return num1-num2


def multiplicar(num1,num2):
    num1 = int(input("ingrese un nro: "))
    num2 = int(input("ingrese un nro: "))
    print("Resultado: ",num1*num2)
    return num1*num2


def dividir(num1,num2):
    num1 = int(input("ingrese un nro: "))
    num2 = int(input("ingrese un nro: "))
    print("Resultado: ",(num1/num2))
    return num1/num2




def calculadora(opcion):
    opcion = " "
    num1 = 0
    num2 = 0

    while(opcion != "-1"):
    # opcion que elige el usuario
        opcion=input("-Selecciona un calculo: ")
        if(opcion == "1"):
            sumar(num1,num2)
        elif (opcion == "2"):
            restar(num1,num2)
        elif (opcion == "3"):
            multiplicar(num1,num2)
        elif (opcion == "4"):
            dividir(num1,num2)
        else:
            print(f'Al ingresar la opción {opcion} ud ha salido del programa')
    return opcion
    
  
    
  # main
print("calculadora")

opcion = " "
print("""
    1) Suma       3) Producto
    2) Resta      4) Division
    """)
   
#Llamada a calculadora    
calculadora(opcion)    
    