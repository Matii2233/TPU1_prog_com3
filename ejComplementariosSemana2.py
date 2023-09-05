# (1) Crea una variable llamada "numero1" y asígnale un número entero de tu elección.
numero1 = 1

# (2) No borres la variable número uno y crea una variable llamada "numero2" asignándole un número decimal.
numero2 = 1.5

# (3) Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2".
suma = numero1+numero2

# (4) Ahora crear tres variables más. Una para resta, otra para multiplicación y otra para división. Imprime estas variables.
resta = numero1-numero2
multiplicacion = numero1*numero2
division = numero1/numero2
print("la suma es: ", suma)
print("la resta es: ", resta)
print("el producto es: ", multiplicacion)
print("la razon es ", division)
print("------------------------------------")

# (5) Crea una variable llamada "nombre" y asígnale tu nombre como valor.
nombre = "Matias"

# (6) crea una variable llamada precio y asignale el valor de un objeto ficticio
precio = 250.50

# (7) ahora sin borrar nada, crea la variable "descuento" y asignale un valor decimal, que sera el descuento al articulo.
#    por ejemplo: si se quiere un 25% de descuento a un articulo, la varible valdra 0.25. 1 = 100%; 0 = 0%.
descuento = 0.2

# (8) ahora calcula el precio final asignandole a la variable precio_final el precio resultado de asignar el descuento.
precio_final = precio-precio*descuento
print("el precio final es ", precio_final)
print("-------------------------------------")

# (9) crea las variable "cadena" e introduce una palabra, texto o lo que quieras a tu eleccion.
cadena = "sapito"

# (10) ahora una variable llamada longitud que contentra la cantidad de caracteres de "cadena".
longitud = len(cadena)
print("la longitud de la palabra ", cadena, "es de ", longitud, " caracteres")
print("-------------------------------------")

# (11) Crea denuevo la variable "precio" con un valor decimal y conviertelo, en la misma variable o en otra, a un numero entero.
precio = 120.88
precio = int(precio)

# (12) crea las variables "nombre" y "apellido" y concatenalas con un espacio entre medio de ambas.
#     utiliza la form que quieras para concatenar
nombre = "Matias"
apellido = " Salinas"
nombre_completo = nombre + apellido
print("mi nombre completo es ", nombre_completo)
print("-------------------------------------")

# (13) pon tu edad en una variable, incrementala en 5 y disminuyela en 10.
edad = 20
edad += 5
edad -= 10

# (14) Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y centímetros.

altura = 1.69
altura *= 4
altura /= 3

# (15) Crea una variable que contenga tu nombre completamente en mayúsculas. Después transfórmalo todo en minúsculas.
nombre = "MATIAS"
print("nombre en mayus: ", nombre)
nombre.lower()
print("nombre en minus: ", nombre.lower())

# (16) Por último, con la variable con el nombre en mayúsculas, aplica un método parecido para que se transforme todo en minúsculas
#     excepto la primera letra.
nombre.capitalize()
print("nombre con la primera letra mayus: ", nombre.capitalize())








