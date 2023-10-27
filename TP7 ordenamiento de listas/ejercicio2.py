def selection_by_letter (words):
    # El primer indice recorre cada posicion y la compara con todas las demas posiciones a partir de la posicion i
    for i in range(len(words)):
        minor = words[i]
        pos = i

        # El segundo indice busca el numero menor desde la posicion i hasta el final del arreglo
        for j in range(i,len(words)):
            word = words[j]
            if word[:1]<minor[:1]:
                minor = words[j]
                pos = j

        aux = words[i]
        words[i] = words[pos]
        words[pos] = aux

    return words






words = ["tiro", "arreglo", "litro", "kilo", "metro", "altura"]
print("Lista original:")
print(words)
print()
print("Lista ordenada por metodo SELECCION:")
print(selection_by_letter(words))