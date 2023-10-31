'''Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
   Además deberá mostrar un menú con las siguientes opciones:
    •	Añadir contacto
    •	Lista de contactos
    •	Buscar contacto
    •	Editar contacto
    •	Cerrar agenda
'''

from Agenda import Agenda
ag = Agenda()

# añadir contacto
ag.add_contact()
ag.add_contact()
ag.add_contact()
print()
print()

#obtener un contacto o todos los contactos
print("Un contacto especifico: ")
print()
print(ag.get_contact(0))
print()
print("Todos los contactos:")
ag.get_contacts()
print()

#buscar un contacto
ag.search("dan")
print()

#editar contacto
search_name = input("¿Que nomrbe desea editar?: ")
ag.edit(search_name)
print()

#volver a mostrar contactos
print("Todos los contactos:")
ag.get_contacts()
print()