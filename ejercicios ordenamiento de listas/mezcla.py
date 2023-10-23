# La funcion principal consiste en dividir la lista original en dos mistades y asignar cada una a una lista nueva
def mergeSort(arr):
    # Cuando la lista recibida por la funcion tenga un solo elemento devolvera la lista 
    if len(arr) == 1:
        return arr
    
    # Mientras la lista tenga mas de un elemento sera dividida en dos mitades
    arr_i = arr[:len(arr)//2]
    arr_d = arr[len(arr)//2:]

    # Luego se llama a la funcion principal  con cada una de las mitades para dividirlas en otras dos mitades
    arr_i = mergeSort(arr_i)
    arr_d = mergeSort(arr_d)

    # Luego se llama a la funcion que realizara el ordenamiento y devuelve la lista ordenada la cual sera la que etornemos finalmente
    return merge(arr_i, arr_d)

# La funcion secundaria realiza el ordenamiento y recibe las dos mitades
def merge(list_i, list_d):
    new_list=[]
    while len(list_i)>0 and len(list_d)>0:
        # Tomamos el primer numero de cada lista y añadimos el menor a la lista final. 
        # Luego eliminamos este valor de su lista original para no volver a pasarlo a la lista final.
        if list_i[0] < list_d[0]:
            new_list.append(list_i[0])
            list_i = list_i[1:]
        else:
            new_list.append(list_d[0])
            list_d = list_d[1:]

    # En caso de que una de las dos listas ya halla pasado todos sus valores, pasaremos los valores que queden en la otra lista.
    if len(list_i) > 0:
        new_list = new_list + list_i
    if len(list_d) > 0:
        new_list = new_list + list_d

    return new_list





arr = [2,3,11,45,6,73,22,84,29,57,26,8,4,55,9]
print("Lista desordenada:")
print(arr)
print()

print("Lista ordenada")
print(mergeSort(arr))