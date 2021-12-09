# -*- coding: utf-8 -*-
# Nicolás Gonzalo Cordero Varas - ICCI - RUT: 20.543.155-1

# contadores

contadorTotalGlobal = 0 

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

#Ciclo While

while datosIngresados != "":

    #Le hacemos split al input

    partes = datosIngresados.split()
    añoIngresado = int(partes[0])
    mesIngresado = int(partes[1])
    diaIngresado = int(partes[2])
    frutaIngresada = partes[3].lower()
    cantidadIngresada = int(partes[4])
   
    contadorTotalGlobal += cantidadIngresada

    #Cambio de mes

    if (mesIngresado != mesAnterior or añoIngresado != añoAnterior) and mesAnterior != -1:
    
        print(">Total Mes",str(mesAnterior)+str("/")+str(añoAnterior),"n=",contadorMensualNaranja,"m=",contadorMensualManzana,"p=",contadorMensualPera,"k=",contadorMensualKiwi)

        contadorMensualNaranja = 0 
        contadorMensualManzana = 0 
        contadorMensualPera = 0 
        contadorMensualKiwi = 0 

    #Cambio de año

    if añoIngresado != añoAnterior and añoAnterior != -1:

        print(">Año",añoAnterior,"n=",contadorAnualNaranja,"m=",contadorAnualManzana,"p=",contadorAnualPera,"k=",contadorAnualKiwi)

        contadorAnualNaranja = 0 
        contadorAnualManzana = 0 
        contadorAnualPera = 0 
        contadorAnualKiwi = 0 


    #Modificamos contadores dependiendo del tipo de fruta   

    if frutaIngresada == str(frutas_posibles[0]):
        contadorTotalNaranja += cantidadIngresada
        contadorAnualNaranja += cantidadIngresada
        contadorMensualNaranja += cantidadIngresada

    elif frutaIngresada == str(frutas_posibles[1]):
        contadorTotalManzana += cantidadIngresada
        contadorAnualManzana += cantidadIngresada
        contadorMensualManzana += cantidadIngresada
    elif frutaIngresada == str(frutas_posibles[2]):
        contadorTotalPera += cantidadIngresada
        contadorAnualPera += cantidadIngresada
        contadorMensualPera += cantidadIngresada
    elif frutaIngresada == str(frutas_posibles[3]):
        contadorTotalKiwi += cantidadIngresada
        contadorAnualKiwi += cantidadIngresada
        contadorMensualKiwi += cantidadIngresada

    mesAnterior = mesIngresado
    añoAnterior = añoIngresado 
    

    datosIngresados = input("Ingrese datos: ")

#Porcentajes por fruta

porcentajeNaranjas = ((contadorTotalNaranja/contadorTotalGlobal)*100)
porcentajeManzanas = ((contadorTotalManzana/contadorTotalGlobal)*100)
porcentajePeras = ((contadorTotalPera/contadorTotalGlobal)*100)
porcentajeKiwis = ((contadorTotalKiwi/contadorTotalGlobal)*100)

print("Programa finalizado")
print("")
print(">Total Vendido:",contadorTotalGlobal,"unidades de fruta")
print(">Total Naranjas:",contadorTotalNaranja,"unidades","/",round(porcentajeNaranjas,2),"%","del total vendido")
print(">Total Manzanas:",contadorTotalManzana,"unidades","/",round(porcentajeManzanas,2),"%","del total vendido")
print(">Total Peras:",contadorTotalPera,"unidades","/",round(porcentajePeras,2),"%","del total vendido")
print(">Total Kiwis:",contadorTotalKiwi,"unidades","/",round(porcentajeKiwis,2),"%","del total vendido")

