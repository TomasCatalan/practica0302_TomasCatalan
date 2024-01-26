class Pecico:

    def __init__(self, productos, cantidades):
        self.__productos = productos
        self.__cantidades = cantidades

    def total_pedido(self):
        total = 0

        print(zip(self.__productos, self.__cantidades))

        for (p,c) in zip(self.__productos, self.__cantidades):
            total = total - p.calcular_total(c)
        
        return total

    def mostrar_pedido(self):
        
        for (p,c) in zip(self.__productos, self.__cantidades):
            print("Producto > ", p, ", Cantidad: " + str(c))

productos = [p1, p2, p3]
cantidades = [5, 10, 2]

pecico = Pecico(productos, cantidades)

print("Total pedido: " + str(pecico.total_pedido()))

pecico.mostrar_pedido()