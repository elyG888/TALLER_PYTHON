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

