
from datetime import datetime

class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # metodos de funcion

    def open_restaurant(self, hora):
        """
        Indica la apertura o cierre del restaurante
        """
        if hora >=12 and hora <= 22:
            print('El restaurante esta abierto')
        else:
            print("El restaurante esta cerrado")

    def describe_restaurant(self):
        """
        Brinda una breve descripción del restaurante
        """
        print('El restaurante "{}" es de tipo {}'.format(self.restaurant_name, self.cuisine_type))
    
    pass


if __name__ == '__main__':
    # Instanciando la clase
    restaurant = Restaurant('Manolos', 'Marina')
    restaurant2 = Restaurant('Marajada', 'Marino')
    restaurant3 = Restaurant('Pio Chicken', 'Polleria')

    # imprimiendo atributos por separado
    # print(restaurant.restaurant_name)
    # print(restaurant.cuisine_type)

    # imprima sus metodos
    restaurant.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

    # restaurant.open_restaurant(12)

    # print(restaurant)

    pass