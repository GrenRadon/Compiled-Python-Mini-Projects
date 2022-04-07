# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# CÓDIGO REALIZADO POR JULIÁN VILLAMIZAR PEÑA


import Utilidades
import Encomiendas
import UtilidadesEncomiendas

#Variable global
flagSiPrimeraVez = 1

def main():
    Utilidades.clear()
    Utilidades.mensajeDeBienvenida()
    UtilidadesEncomiendas.siCargarEncomiendasNuevas()
    Utilidades.menu()

if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
