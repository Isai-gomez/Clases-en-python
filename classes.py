# class Terrestre:
#     def desplazar(self):
#         print("El animal anda")
# class Acuatico:
#     def desplazar(self):
#         print("El animal nada")
# class Cocodrilo(Acuatico, Terrestre):
#     pass


l = [4,3,2,6]
l2 = [n for n in l if n == 3]
print(l2)


# class Instrumento:
#     def __init__(self, precio):
#         self.precio = precio
#     def tocar(self):
#         print("Tocar musica")
#     def romper(self):
#         print("Eso lo pagas tu")
#         print("Son ", self.precio, "$$")
# class Bateria(Instrumento):
#     pass
# class Guitarra(Instrumento):
#     pass


# class Carro:
#     """Abstracion de los objetos coches"""
#     def __init__(self,gasolina):
#         self.gasolina = gasolina
#         print("Tenemos", gasolina, "litros")
#     def arracar(self):
#         if self.gasolina > 0:
#             print("Arrancar")
#         else:
#             print("No arrancar")
#     def conducir(self):
#         if self.gasolina > 0:
#             self.gasolina -= 1
#             print("Queda ", self.gasolina, "litros")
#         else:
#             print("No se mueve")


