class Producto:
    # constructor() { ... }
    def __init__(self, nombre, precio, disponibilidad, imagen):
        # al momento de crear una instancia se deberá declarar los parámetros
        self.nombre = nombre
        self.precio = precio
        self.disponibilidad = disponibilidad
        self.imagen = imagen

    def mostrar_imagen(self):
        return self.imagen
    

shampoo = Producto('Shampoo', 7.40, True, 'https://google.com')
print(shampoo.mostrar_imagen())