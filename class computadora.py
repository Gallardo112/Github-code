class computadora:
    def __init__(self, marca, modelo, procesador, ram):
        self.__marca = marca
        self.__modelo = modelo
        self.__procesador = procesador
        self.__ram = ram
#getters
    def get_id(self):
        return self.__id
    
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_procesador(self):
        return self.__procesador

    def get_ram(self):
        return self.__ram
    
#Setters
    def set_id(self, id):
        self.__id = id

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_procesador(self, procesador):
        self.__procesador = procesador

    def set_ram(self, ram):
        if ram > 0:
            self.__ram = ram

#Metodo aumentar ram
def aumentar_ram(self, cantidad):
        if cantidad > 0:
            self.__ram += cantidad

#metodo redimiento
def rendimiento(self):
        if self.__procesador == "i7" and self.__ram >= 16:
            return "Alto rendimiento"
        elif self.__procesador == "i5" and self.__ram >= 8:
            return "Rendimiento medio"
        else:
            return "Bajo rendimiento"





   
    