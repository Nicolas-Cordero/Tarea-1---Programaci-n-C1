# -*- coding: utf-8 -*-
# Nicolás Gonzalo Cordero Varas - ICCI - RUT: 20.543.155-1

# contadores

contador_total_naranja = 0
contador_anual_naranja = 0
contador_mensual_naranja = 0

contador_total_manzana = 0
contador_anual_manzana = 0
contador_mensual_manzana = 0

contador_total_pera = 0
contador_anual_pera = 0
contador_mensual_pera = 0

contador_total_kiwi = 0
contador_anual_kiwi = 0
contador_mensual_kiwi = 0
añoAnterior = -1
mesAnterior = -1

# frutas_posibles

frutas_posibles = ["naranja", "manzana", "pera", "kiwi"]

# se abre el archivo

datos = input("Ingrese datos: ")

while datos != "":

    partes = datos.split(" ")
    añoIngresado = int(partes[0])
    mesIngresado = int(partes[1])
    diaIngresado = int(partes[2])
    tipoFrutaIngresada = str(partes[3]).lower()
    cantidadFrutaIngresada = int(partes[4])

    if tipoFrutaIngresada == str(frutas_posibles[0]):

        contador_total_naranja += cantidadFrutaIngresada
        contador_anual_naranja += cantidadFrutaIngresada
        contador_mensual_naranja += cantidadFrutaIngresada

    elif tipoFrutaIngresada == str(frutas_posibles[1]):

        contador_total_manzana += cantidadFrutaIngresada
        contador_anual_manzana += cantidadFrutaIngresada
        contador_mensual_manzana += cantidadFrutaIngresada

    elif tipoFrutaIngresada == str(frutas_posibles[2]):

        contador_total_pera += cantidadFrutaIngresada
        contador_anual_pera += cantidadFrutaIngresada
        contador_mensual_pera += cantidadFrutaIngresada

    elif tipoFrutaIngresada == str(frutas_posibles[3]):

        contador_total_kiwi += cantidadFrutaIngresada
        contador_anual_kiwi += cantidadFrutaIngresada
        contador_mensual_kiwi += cantidadFrutaIngresada

    else:
        print("Por favor, ingrese bien el nombre de la fruta")

    if añoIngresado != añoAnterior and añoAnterior != -1:

        print(
            "> Año",
            añoAnterior,
            "n=",
            contador_anual_naranja,
            "m=",
            contador_anual_manzana,
            "p=",
            contador_anual_pera,
            "k=",
            contador_anual_kiwi,
        )

        contador_anual_naranja = 0
        contador_anual_manzana = 0
        contador_anual_pera = 0
        contador_anual_kiwi = 0

        contador_mensual_naranja = 0
        contador_mensual_manzana = 0
        contador_mensual_pera = 0
        contador_mensual_kiwi = 0

    if mesIngresado != mesAnterior and mesAnterior != -1:

        print(
            "> Total Mes",
            str(mesAnterior) + str("/") + str(añoIngresado),
            "n=",
            contador_mensual_naranja,
            "m=",
            contador_mensual_manzana,
            "p=",
            contador_mensual_pera,
            "k=",
            contador_mensual_kiwi,
        )

        contador_mensual_naranja = 0
        contador_mensual_manzana = 0
        contador_mensual_pera = 0
        contador_mensual_kiwi = 0

        mesAnterior = mesIngresado
        añoAnterior = añoIngresado
    datos = input("Ingrese datos: ")


print("Fin del programa")


print(contador_total_manzana)
