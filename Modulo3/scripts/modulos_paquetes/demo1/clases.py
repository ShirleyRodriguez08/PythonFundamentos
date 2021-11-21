


class Restaurant:
    def __init__(self,restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print('Restaurant name: {}'.format(self.restaurant_name))
        print('Cuisine type: {}'.format(self.cuisine_type))
    
    def open_restaurant(self, hora_actual):

        if hora_actual > 12 and hora_actual<10:
            print("Restaurante abierto")
        else:
            print("Restaurante cerrado")