"""
for i in range (2, 11, 2): 
    print(f" {i} - Ely 👾")
"""
"""
mensaje = input("Escribe tu mensaje : ")
repeticion = int(input("Cuantas veces quieres repetir el mensaje : "))

for i in range(repeticion):
    print(mensaje)
"""
"""
# Preguntar nombre de estudiante
# Preguntar al profe cuantas notas quiere registrar.
# Hacer el promedio de las notas y mostrarlo.
# Promedio es >=3.5 Mostrar Estudiante Gano - Contrario Perdió 

print("=== Sistema de calificacion. ===")
estudiante = input("Nombre de estudiante : ")
can_notas = int(input("Cuantas notas vas a registrar : "))


promedio = 0
for i in range(can_notas):
    notas=float(input(f"Ingrese nota {i+1} : "))

    if notas not in range (0,5):
        print("Nota Invalida")
        break 

    promedio += notas 
promedio_final =promedio/can_notas

if (promedio_final) >=3.5:
    print(f"El estudinate {estudiante} - promedio {promedio_final:.1f} Gano👌")
else:
        print(f"El estudiante {estudiante} - promoedio {promedio_final:.1f} Perdió😢")
"""


while True:

    menu =int(input("""
    Selecciones opción a realizar : 
    1. Sumar
    2. Restar
    3. Salir
    : """))
    if menu == 1 : 
        n1 = int(input("Ingrese el número : "))
        n2 = int(input("Ingrese el número : "))
        n3 = int(input("Ingrese el número : "))
        print(f"Resultado {n1+n2+n3}")
    elif menu == 2 :
        n1 = int(input("Ingrese el número : "))
        n2 = int(input("Ingrese el número : "))
        n3 = int(input("Ingrese el número : "))
        print(f"Resultado {n1-n2-n3}")
    elif menu == 3 :
        print("Saliendo del sistema")
        break 

# Ejercicio 1: Mostrar la tabla de multiplicar de un número
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(1, 11):          # recorre los valores del 1 al 10
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 2: Sumar los primeros n números naturales
n = int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(1, n + 1):
    suma = suma + i

print(f"La suma de los primeros {n} números naturales es: {suma}")

# Ejercicio 3: Contar cuántos números pares hay entre 1 y n
n = int(input("Ingrese un número entero positivo: "))

contador = 0
numero   = 1
while numero <= n:
    if numero % 2 == 0:
        contador = contador + 1
    numero = numero + 1

print(f"Hay {contador} números pares entre 1 y {n}")

# Ejercicio 4: Solicitar una contraseña hasta que sea correcta
clave_correcta  = "python2026"
clave_ingresada = input("Ingrese la contraseña: ")

while clave_ingresada != clave_correcta:
    print("Contraseña incorrecta, intente de nuevo")
    clave_ingresada = input("Ingrese la contraseña: ")

print("Contraseña correcta, acceso concedido")

# Ejercicio 5: Calcular el factorial de un número
n = int(input("Ingrese un número entero no negativo: "))

factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print(f"El factorial de {n} es: {factorial}")

