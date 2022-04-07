#Módulo de utilidades del proyecto.

from os import system, name
from time import sleep
from random import randint
import Encomiendas

#Función para limpiar la pantalla dependiendo del sistema operativo
def clear():
    if name == "nt": #on windows
        _ = system("cls")

    # for mac and linux os.name == 'posix'
    else:
        _ = system("clear")

def mensajeDeBienvenida():
    print("*******************************COORDINADORA****************************")
    print("***********************************************************************")
    print("**\033[1;32;99m ooooooo  oooo  ooooo ooooooooo oo   oo    oo   ooo   ooooo  ooooo \033[0;37;99m**")
    print("**\033[1;32;99m ooo     oo  oo oo    ooooooooo oo   oo    oo  oo oo  oo  oo oo    \033[0;37;99m**")
    print("**\033[1;32;99m ooooooo oo  oo ooooo    oo      oo oooo  oo  ooooooo oooo   oooo  \033[0;37;99m**")
    print("**\033[1;32;99m     ooo oo  oo oo       oo      oo oo oo oo  oo   oo oo oo  oo    \033[0;37;99m**")
    print("**\033[1;32;99m ooooooo  oooo  oo       oo       oo    oo    oo   oo oo  oo ooooo \033[0;37;99m**")
    print("***********************************************************************")
    print("**************************Sección de encomiendas***********************")
    print(" ")

#Función que despliega el menú
def menu():
    flag=1
    while(flag != 0):
        clear()
        print(" ")
        print("--------------------------------")
        print("|Bienvenido al menú de opciones|")
        print("--------------------------------")
        print("")
        print("Opciones: ")
        print("1. Registro del envio")
        print("2. Actualización del envio")
        print("3. Consulta del estado de envio.")
        print("4. Observación del envío")
        print("5. Información del envío")
        print("6. Salir")
        respuesta = input("Digite su selección: ")
        if(respuesta == '1'):
            registrarEnvio()
        elif(respuesta == '2'):
            actualizarEnvio()
        elif(respuesta == '3'):
            consultarEnvio()
        elif(respuesta == '4'):
            observacionEntrega()
        elif(respuesta == '5'):
            informacionEntrega()
        elif(respuesta == '6'):
            exit(0);
        else:
            print("opción no valida")

#Funciones de cálculos

#Función para calcular el valor del envío
def calcularValorEnvio():
    peso = float(input("Por favor, digite el peso de la caja en Kg: "))
    valorFinal = peso*float(3500)
    valorFinal = '{0:.7g}'.format(valorFinal)

    return valorFinal

def generadorDeNumerosAleatorios(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return int(randint(range_start, range_end))


#Funciones del menú principal

def registrarEnvio():
    clear()
    print("             <[Módulo de registro de encomienda]>")
    print(" ")
    Identificador= int(input("Por favor, digite la cédula del cliente: "))
    for i in range(len(Encomiendas.listaEncomiendas)):
        if Encomiendas.listaEncomiendas[i][0] == Identificador:
            print("Cliente: "+str(Encomiendas.listaEncomiendas[i][1])+" "+str(Encomiendas.listaEncomiendas[i][2]))
            opc = input("¿Desea registrar la encomienda? [Y/n]: ")
            if opc == 'Y' or opc == 'y':
                tmpNGuia = generadorDeNumerosAleatorios(10)
                Encomiendas.listaEncomiendasRegistradas.append([tmpNGuia]+Encomiendas.listaEncomiendas[i])
                print("[[[Cliente Registrado satisfactoriamente con N° de guía: "+str(tmpNGuia)+" ]]]")
                input("Presione [Enter] para continuar...")
            else:
                print("[[[Cliente no registrado...]]]")
        else:
            continue

def actualizarEnvio():
    clear()
    print("             <[Módulo de actualización de datos de encomienda]>")
    print(" ")
    numeroGuiaEncomienda = int(input("Por favor, digite el número de guía de la encomienda a actualizar: "))

    for i in range(len(Encomiendas.listaEncomiendasRegistradas)):
        if Encomiendas.listaEncomiendasRegistradas[i][0] == numeroGuiaEncomienda:
            print("Número de guía encontrado...")
            estadoEnvioActualizado = input("Por favor, ingrese el estado del envío: ")
            Encomiendas.listaEncomiendasRegistradas[i][12] = estadoEnvioActualizado
            print("¡Estado del envío actualizado!")
            input("Presione [Enter] para continuar...")
        else:
            continue

def consultarEnvio():
    clear()
    print("             <[Módulo de consulta del estado del envío]>")
    print(" ")
    print("Por favor, digite el número de guía de la encomienda: ")
    numeroGuiaEncomienda = int(input(">"))
    for i in range(len(Encomiendas.listaEncomiendasRegistradas)):
        if Encomiendas.listaEncomiendasRegistradas[i][0] == numeroGuiaEncomienda:
            print("Estado del envío: "+str(Encomiendas.listaEncomiendasRegistradas[i][13]))
            input("Presione [Enter] para continuar...")
        else:
            continue


def observacionEntrega():
    clear()
    print("             <[Módulo de consulta de la observación de entrega]>")
    print(" ")
    print("Por favor, digite el número de guía de la encomienda: ")
    numeroGuiaEncomienda = int(input(">"))
    for i in range(len(Encomiendas.listaEncomiendasRegistradas)):
        if Encomiendas.listaEncomiendasRegistradas[i][0] == numeroGuiaEncomienda:
            print("Observación de la entrega: ")
            print(Encomiendas.listaEncomiendasRegistradas[i][14])
            input("Presione [Enter] para continuar...")
        else:
            continue

def informacionEntrega():
    clear()
    print("             <[Módulo de información de la encomienda]>")
    print("Por favor, digite el número de guía de la encomienda: ")
    numeroGuiaEncomienda = int(input(">"))
    for i in range(len(Encomiendas.listaEncomiendasRegistradas)):
        if Encomiendas.listaEncomiendasRegistradas[i][0] == numeroGuiaEncomienda:
            print(" ")
            print("Cédula de ciudadanía: "+str(Encomiendas.listaEncomiendasRegistradas[i][1]))
            print("Nombres: "+Encomiendas.listaEncomiendasRegistradas[i][2])
            print("Apellidos: "+Encomiendas.listaEncomiendasRegistradas[i][3])
            print("Dirección de origen: "+Encomiendas.listaEncomiendasRegistradas[i][4])
            print("Dirección de destino: "+Encomiendas.listaEncomiendasRegistradas[i][5])
            print("E-mail: "+Encomiendas.listaEncomiendasRegistradas[i][6])
            print("Fecha del envío: "+Encomiendas.listaEncomiendasRegistradas[i][7])
            print("Hora del envío: "+Encomiendas.listaEncomiendasRegistradas[i][8])
            print("Tamaño de la caja...")
            for j in range(len(Encomiendas.listaEncomiendasRegistradas[i][9])):
                if j == 0:
                    print("X: "+str(Encomiendas.listaEncomiendasRegistradas[i][9][j]))
                if j == 1:
                    print("Y: "+str(Encomiendas.listaEncomiendasRegistradas[i][9][j]))
                if j == 2:
                    print("W: "+str(Encomiendas.listaEncomiendasRegistradas[i][9][j]))
            print("Contenido de la caja...")
            for k in range(len(Encomiendas.listaEncomiendasRegistradas[i][10])):
                print("Nombre del item: "+str(Encomiendas.listaEncomiendasRegistradas[i][10][k][0]))
                print("Cantidad: "+str(Encomiendas.listaEncomiendasRegistradas[i][10][k][1]))
            print("Nombre del destinatario: "+str(Encomiendas.listaEncomiendasRegistradas[i][11]))
            print("Estado del envío: "+str(Encomiendas.listaEncomiendasRegistradas[i][12]))
            print("Valor del envío: "+str(Encomiendas.listaEncomiendasRegistradas[i][13]))
            print("Observación en la entrega: ")
            print(Encomiendas.listaEncomiendasRegistradas[i][14])


