class viajeroFrecuente:
    __numViajero = 0
    __dni = ''
    __Nombre = ''
    __Apellido=''
    __millasacum = 0.0
    def __init__(self, numViajero, dni, Nombre, Apellido, millasacum):
        self.__numViajero = numViajero
        self.__dni = dni
        self.__Nombre = Nombre
        self.__Apellido = Apellido
        self.__millasacum = millasacum
    def cantidadTotalM(self):
        return self.__millasacum
    def acumMillas(self,millas):
        self.__millasacum = self.__millasacum + millas
    def canjeM(self,millas):
        if self.__millasacum>=millas:
            self.__millasacum = self.__millasacum - millas
            return print ("La cantidad de millas acumuladas son {}".format(self.__millasacum))
        else:return print("error")


class ViajeroFrecuente:
    pass
