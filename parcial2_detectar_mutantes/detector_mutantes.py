from funciones import fill_dna_secuence, is_mutant

#Inicializacion de la matriz#
dna = [
    ['' , '' , '' , '' , '' , ''],
    ['' , '' , '' , '' , '' , ''],
    ['' , '' , '' , '' , '' , ''],
    ['' , '' , '' , '' , '' , ''],
    ['' , '' , '' , '' , '' , ''],
    ['' , '' , '' , '' , '' , '']
]

# LLAMADA A FUNCION PARA LLENAR MATRIZ
dna = fill_dna_secuence(dna)


# prueba MUTANTE
'''dna = [
    ['C' , 'A' , 'C' , 'A' , 'G' , 'A'],
    ['A' , 'A' , 'G' , 'T' , 'G' , 'G'],
    ['T' , 'A' , 'C' , 'T' , 'C' , 'A'],
    ['C' , 'A' , 'T' , 'A' , 'C' , 'A'],
    ['C' , 'T' , 'G' , 'G' , 'G' , 'G'],
    ['T' , 'A' , 'C' , 'G' , 'T' , 'T'],
]
# prueba NO MUTANTE
dna = [
    ['A' , 'C' , 'C' , 'C' , 'T' , 'A'],
    ['G' , 'C' , 'T' , 'T' , 'C' , 'G'],
    ['C' , 'A' , 'G' , 'A' , 'A' , 'T'],
    ['G' , 'C' , 'T' , 'C' , 'T' , 'A'],
    ['A' , 'C' , 'A' , 'G' , 'G' , 'T'],
    ['T' , 'A' , 'G' , 'C' , 'C' , 'A']
]
'''

# se muestra la secuencia de ADN
print()
print("Secuencia de ADN:")
for letter in dna:
    print(f" {letter}")
print()
print("# True = 'mutante'    # False = 'no mutante'")
print()

# se muestra el resultado
mutant = is_mutant(dna)
print(f" resultado :'{mutant}'")
print()