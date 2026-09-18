#creacion de variables
nombre = "Ely" #Variable string (texto)
documento = 1012 #Variable tipo entero
direccion = "Medellin Cll 41" #Variable tipo string (cadena de texto)
tiene_deudas = True #Variable de tipo bool (booleano)

# ========================================================================
#Mostrar informacion en pantalla
# ========================================================================
print(nombre)

# ========================================================================
#Concatenacion usando +
# ========================================================================
print("concatenacion usando +")
print("=" * 30)

# El operador + permite unir textos.
# Cuando usamos +, todos los elementos deben ser strings
#
# documento es un entero (int), por lo que esta linea
#produciría un error:
#
# print("Mi nombre es: " + Ely + " y mi documentos es: " + documento)

# Para solucionarlo, podemos convertir el número a texto
# Utilizando str()
print("Mi nombre es: " + nombre + " y mi documento es: " + str(documento))

print("\nCONCATENACIÓN USANDO ,")
print("=" * 30)
print("Mi nombre es: " , nombre , " y mi documento es: " , documento)

# ======================================================================
# CONCATENACIÓN USANDO F-STRINGS
# ======================================================================
print("\nCONCATENACIÓN USANDO F-STRINGS")
print("=" * 30)
print(f"Mi nombre es: {nombre} y mi documento es: {documento}")

print("n\MOSTRAR VARIAS VARIABLES CON F-STRINGS")
print("=" * 30)

print(f"""
Nombre: {nombre}
Documento: {documento}
Dirección: {direccion}
¿Tiene deudas?: {tiene_deudas}
""")


# SALTO DE LINEA EN PYTHON

#\n representa un salto de linea.
# Salto de linea al inicio del texto
print(f"\n Hola, {nombre}!")

# Salto de la linea al final del texto
print(f"Bienvenida {nombre} a Python.\n")
