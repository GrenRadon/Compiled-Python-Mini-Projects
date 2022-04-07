#Módulo de utilidades necesarias para las encomiendas
import Encomiendas
import Utilidades
from datetime import datetime
import main

def siCargarEncomiendasNuevas():
    flagEncomienda = 'Y'
    while(flagEncomienda == 'Y' or flagEncomienda == 'y'):
        if main.flagSiPrimeraVez == 1:
            flagEncomienda = input("¿Desea crear una encomienda? '[Y/N]': ")
            main.flagSiPrimeraVez += 1
        else:
            flagEncomienda = input("¿Desea crear otra encomienda? '[Y/N]': ")

        if flagEncomienda == 'Y' or flagEncomienda == 'y':
            Encomiendas.listaEncomiendas.append(crearEncomienda())
        else:
            continue

def crearEncomienda():

    c_C = int(input("CC: "))
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    direccionOrigen = input("Dirección de origen: ")
    direccionDestino = input("Dirección de destino: ")
    email = input("E-mail: ")
    fechaEnvio = input("Fecha del envio: ")
    #Bloque para capturar la hora
    now = datetime.now()
    print("Hora del envío (HH:mm:ss): "+str(now.strftime("%H:%M:%S")))
    horaEnvio = now.strftime("%H:%M:%S")
    #Terminación del bloque
    tamanioCaja = obteniendoDimensionesEncomienda()
    contenidoCaja = listaItems()
    nombreRecibe = input("Nombre completo del destinatario: ")
    estadoEnvio = input("Estado del envio: ")
    valorEnvio = Utilidades.calcularValorEnvio()
    observacionEntrega = input("Observación de la entrega: ")
    print("Datos de encomienda cargados...")


    return [c_C, nombres, apellidos, direccionOrigen, direccionDestino, email, fechaEnvio, horaEnvio, tamanioCaja, contenidoCaja, nombreRecibe, estadoEnvio, valorEnvio, observacionEntrega]

#Función para cargar items en la lista de items
def listaItems():
    listaItems = []
    bandera = 1
    print("<[Bienvenido a la canasta de items]>")
    print("A continuación procederemos a agregar elementos. Para salir digite '0'")
    while(bandera != 0):
        tmp = input("Por favor, digite el elemento n°"+str(bandera)+": ")
        if(tmp == '0'):
            bandera = 0
            break
        else:
            tmpCantidad = int(input("Por favor, digite la cantidad de "+tmp+": "))
            listaItems.append([tmp]+[tmpCantidad])
            bandera=bandera+1

    Utilidades.clear()
    ##Sección de impresion
    print(" ")
    print("<<Lista de elementos agregados a la canasta>>")
    print(" ")
    for i in range(len(listaItems)):
        print("Elemento N°"+str(i+1)+" "+listaItems[i][0]+" tiene una cantidad de "+str(listaItems[i][1]))

    return listaItems

def obteniendoDimensionesEncomienda():
    X = float(input("Por favor, digite el ancho de la caja en cm: "))
    X = '{0:.3g}'.format(X)
    Y = float(input("Por favor, digite el largo de la caja en cm: "))
    Y = '{0:.3g}'.format(Y)
    W = float(input("Por favor, digite el alto de la caja en cm: "))
    W = '{0:.3g}'.format(W)

    return [X,Y,W]
