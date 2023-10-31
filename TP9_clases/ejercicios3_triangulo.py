from Triangulo import Triangulo

'''Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos 
   para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es 
   (equilátero, isósceles o escaleno).'''

tri = Triangulo()
tri.setSideA(3.3)
tri.setSideB(4.5)
tri.setSideC(2.9)
'''tri.setSideA(3.3)
tri.setSideB(2.4)
tri.setSideC(2.4)'''
'''tri.setSideA(3.5)
tri.setSideB(3.5)
tri.setSideC(3.5)'''


print()
print(f"Los valores del triangulo son:")
print(f"  {tri.getSideA()}")
print(f"  {tri.getSideB()}")
print(f"  {tri.getSideC()}")
print()
tri.type()
print()