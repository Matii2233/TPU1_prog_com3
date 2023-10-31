from Persona import Persona

''' Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
    •	Un constructor, donde los datos pueden estar vacíos.
    •	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
    •	mostrar(): Muestra los datos de la persona.
    •	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
'''

ps = Persona()


print()
ps.show_persona()
print()

ps.set_name("Marcos")
ps.set_age(22)
ps.set_dni(44362528)

print("Los atributos con valores agregados de la persona son:")
ps.show_persona()
print(f"{ps.get_name()} es mayor de edad?")
print(f"  {ps.is_legal_age()}")
print()