# -*- coding: utf-8 -*-
# Nicolás Gonzalo Cordero Varas - ICCI - RUT: 20.543.155-1

# contadores

contadorTotalNaranja = 0
contadorAnualNaranja = 0
contadorMensualNaranja = 0

contadorTotalManzana = 0
contadorAnualManzana = 0
contadorMensualManzana = 0

contadorTotalPera = 0
contadorAnualPera = 0
contadorMensualPera = 0

contadorTotalKiwi = 0
contadorAnualKiwi = 0
contadorMensualKiwi = 0

añoAnterior = -1
mesAnterior = -1

# frutas_posibles

frutas_posibles = ["naranja", "manzana", "pera", "kiwi"]

datosIngresados = input("Ingrese datos: ")

while datosIngresados != "":

    partes = datosIngresados.split()
    añoIngresado = int(partes[0])
    mesIngresado = int(partes[1])
    diaIngresado = int(partes[2])
    frutaIngresada = partes[3].lower()
    cantidadIngresada = int(partes[4])

    if frutaIngresada == str(frutas_posibles[0]):
        contador


    if (mesIngresado != mesAnterior or añoIngresado != añoAnterior) and mesAnterior != -1:
    
        print("xd")

    if añoIngresado != añoAnterior and añoAnterior != -1:

        print("owo")

    mesAnterior = mesIngresado
    añoAnterior = añoIngresado 
    

    datosIngresados = input("Ingrese datos: ")