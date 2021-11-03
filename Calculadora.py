# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 14:09:21 2021

@author: Usuario
"""

# Calculadora

print("calculadora")

print("""
    1) Suma       3) Producto
    2) Resta      4) Division
    5) Modulo     6) Potencia
    7) Promedio
    """)

opcion = " "

while(opcion != "-1"):
    #opcion que elige el usuario
    opcion=input("-Selecciona un calculo: ")
    
    if(opcion == "1"):
        nro1 = int(input("ingrese un nro: "))
        nro2 = int(input("ingrese un nro: "))
        print("Resultado: ",nro1+nro2)
    elif (opcion == "2"):
        nro1 = int(input("ingrese un nro: "))
        nro2 = int(input("ingrese un nro: "))
        print("Resultado: ",nro1-nro2)
    elif (opcion == "3"):
        nro1 = int(input("ingrese un nro: "))
        nro2 = int(input("ingrese un nro: "))
        print("Resultado: ",nro1*nro2)
    elif (opcion == "4"):
        nro1 = int(input("ingrese un nro: "))
        nro2 = int(input("ingrese un nro: "))
        print("Resultado: ",(nro1/nro2))
    elif (opcion == "5"):
        nro1 = int(input("ingrese un nro: "))
        nro2 = int(input("ingrese un nro: "))
        print("Resultado: ",nro1%nro2)
    elif (opcion == "6"):
        nro1 = int(input("ingrese un nro: "))
        nro2 = int(input("ingrese un nro: "))
        print("Resultado: ",nro1**nro2)
    elif (opcion == "7"):
        nro1 = int(input("ingrese un nro: "))
        nro2 = int(input("ingrese un nro: "))
        print("Resultado: ",(nro1 + nro2) /2)
    else:
        print("Salir del programa")
       
       