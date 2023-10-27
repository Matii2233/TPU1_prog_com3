def words_chain_insertion(words):
    for i in range(1, len(words)):
        for j in range(i-1,0):
            print(j,end="")
            '''if len(words[j+1]) < len(words[j]):
                aux = words[j]
                words[j] = words[j+1]
                words[j+1] = aux'''
            

    return words





words = ["Cambio","Teclado","Raton","Jirafa","Elefante","Arbol","PLanta","Flor"]
print("La lista original es:")
print(words)
print()
print("La lista ordenada por INSERCION es:")
print(words_chain_insertion(words))