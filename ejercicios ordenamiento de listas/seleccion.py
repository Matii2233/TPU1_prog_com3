# Funcion, ordenamiento de un arreglo por el metodo de seleccion
def selection(arr):
    # el primer for es el indice a que establece un rango en el cual se realizara el intercambio de un numero y el numero menor
    for a in range(0, len(arr)):
        minor = arr[a]
        pos   = a

        # el segundo indice inicia en la posicion siguiente al primero y sera el que busque el numero menor
        for j in range(a+1, len(arr)):
            if arr[j]<minor : 
                minor = arr[j]
                pos = j

        # una vez se encuentre el numero menor se realiza el cambio y se vuelve a empezar
        aux = arr[a]
        arr[a] = arr[pos]
        arr[pos] = aux

    print(arr)




# Metodo 2: Selection
arr = [4, 12, 23, 85, 37, 1, 29]
print("la lista desordenada es:")
print(arr)
print()

print("La lista ordenada es")
selection(arr)