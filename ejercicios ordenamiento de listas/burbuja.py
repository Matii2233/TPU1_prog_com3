# Funcion ordenamiento metodo burbuja
def bubble(arr):
    # n sera el largo del arreglo
    n = len(arr)
    # flag se inicializa en falso y se entra en el while
    flag = False

    while flag == False :
        # dentro del while flag cambia a verdadero
        flag = True

        for i in range(n-1):
            # si la lista esta desordenada se entra en el condicional y flag cambia a falso
            # caso contrario, flag continua siendo verdadera, lo que impide que se vuelva a entrar en el while y termina la funcion
            if arr[i] > arr[i+1]:
                # se hace un algoritmo simple por el cual un numero "i" se intercambia con "i+1", cuando i es mayor que i+1.
                # Este proceso se repetira siempre que flag sea falso
                aux = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = aux
                flag = False

    print(arr)




# Metodo 1: burbuja
arr = [4, 12, 23, 85, 37, 1, 29]
print("la lista desordenada es:")
print(arr)
print()

print("La lista ordenada es")
bubble(arr)