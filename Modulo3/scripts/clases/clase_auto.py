# 1. librerias
from datetime import datetime

# 2. constantes
CURRENT_YEAR = datetime.today().year 

# 3. funciones y/o clases
class Auto:
    # declaro una constante para la clase
    nro_pruerta= 4

    # metodo constructor
    def __init__(self, marca, modelo, anio, nro_placa):
        """
        Clase constructura la cual me permite inicializar mi clase Auto
        """
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.nro_placa = nro_placa

    # construccion de metodos
    def encender_motor(self):
        print('Encendiendo el motor ... ')

    def anios_uso(self):
        print('El auto tiene una antiguedad de {} años'.format(CURRENT_YEAR - self.anio))
    
    pass



# mi programa

if __name__ == '__main__':

    # Generando objetos a partir de la clase(molde)
    auto1 = Auto('Toyota', 'Corona', 2018, 'AZ500')

    print('Marca:{}\nModelo:{}\nPuertas:{}'.format(auto1.marca, auto1.modelo, auto1.nro_pruerta))

    # llamando al metodo encender_moto del objeto
    auto1.encender_motor()

    auto1.anios_uso()

    # generando un objeto 2
    auto2 = Auto('Kia', 'Rio', 2014, 'EQ789')

    pass


