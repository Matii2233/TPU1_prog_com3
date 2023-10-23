def insercion (arr):
    length = len(arr)

    for i in range(1, length):
        aux = arr[i]
        j = i-1
        while (j > -1 and (aux < arr[j])):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = aux

    print(arr)
        


# metodo 3: insercion
arr = [40, 35, 50, 15, 25, 30, 20]
print("la lista desordenada es:")
print(arr)
print()

print("La lista ordenada es")
insercion(arr)