def dictionary_selection_by_year (books):
    len(books)
    for i in range(len(books)):
        pos = i
        for j in range(i + 1, len(books)):
            if books[j]['añoPubl'] < books[pos]['añoPubl']:
                pos = j

        books[i], books[pos] = books[pos], books[i]

    return books





books = [
            {'titulo':'El Principito'            , 'añoPubl':1943 , 'Autor':'Antoine de Saint' , 'Genero':'Fabula Infantil'            },
            {'titulo':'Historia de Dos Ciudades' , 'añoPubl':1859 , 'Autor':'Charles Dickens'  , 'Genero':'Novela de Ficcion Historica'},
            {'titulo':'El Señor de los Anillos'  , 'añoPubl':1954 , 'Autor':'J.R.R. Tolkien'   , 'Genero':'Literatura Fantastica'      },
            {'titulo':'El Alquimista'            , 'añoPubl':1988 , 'Autor':'Paulo Coelho'     , 'Genero':'Novela de Ficcion'          },
        ]

print("Lista original:")
print(books)
print()

new_booksList = dictionary_selection_by_year(books)
print("Lista de libros ordenada por SELECCION en funcion de los años de publicacion")
for book in new_booksList:
    print(book)