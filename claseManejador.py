
from claseViajeroFrecuente import ViajeroFrecuente

class Manejador:
    def __init__(self):
        self.__Listaviajeros = []
    def AgregarViajero(self,Unviajero):
        self.__Listaviajeros.append(Unviajero)
    def BuscarV(self,clave):
        for indice,viajero in enumerate(self.__Listaviajeros):
            if (self.__numViajero == clave):
                return indice

    def testViajero(self):
        pass
