from funciones import get_sheet_dimensions

# Escribí una función recursiva medidas_hoja_A(N) que para una entrada N mayor que cero, devuelva el ancho y el largo de la hoja A(N)
# calculada recursivamente a partir de las medidas de la hoja A(N−1), usando la hoja A0 como caso base.
# La función debe devolver el ancho y el largo -en ese orden- en una tupla.

n = 5
width, length = get_sheet_dimensions(n)
print(f"Medidas de la hoja A{n}: Ancho = {width} mm, Largo = {length} mm")