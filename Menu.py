import claseViajeroFrecuente
import csv


class Menu:

    __op = int
    def __init__(self):
        self.__op=None
    def getOpcion(self):
        return self.__op
    def manejoMenu(self, op):
        If op == 1
            print("El viajero tiene:{}".format(ViajeroFrecuente.cantidadTotalM()))
        elif op==2:
            i = int(input("Ingrese cantidad de millas"))
            ViajeroFrecuente.acumMillas(i)
        elif op==3:
            i=int(input("Ingrese cantidad de millas a canjear"))
            ViajeroFrecuente.canjeM(i)


