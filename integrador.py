# EJERCICIO INTEGRADOR

# SOLICITAR CANTIDAD DE ESTUDIANTES
while True: 
    try:
        cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
        if cantidad_estudiantes > 0:
            break
        else:
            print("La cantidad debe ser mayor que 0.")

    except ValueError:
        print("Debe ingresar un número entero.")

# VARIABLES ACUMULADORAS
suma_promedios = 0
aprobados = 0
reprobados = 0

# REGISTRAR ESTUDIANTES
for estudiantes in range(1, cantidad_estudiantes + 1):
    print("\n--- Estudiante", estudiantes, "---")
    nombre = input("Nombre: ")

    # PRIMERA NOTA
    while True:
        try:
            nota1 = float(input("Primera nota (0 - 5): "))
            if nota1 >= 0 and nota1 <= 5:
                break
            else:
                print("La nota debe estar entre 0 y 5.")
        except ValueError:
            print("Debe ingresar un número.")

    # SEGUNDA NOTA
    while True:
        try:
            nota2 = float(input("Segunda nota (0 - 5): "))
            if nota2 >= 0 and nota2 <= 5:
                break
            else:
                print("La nota debe estar entre 0 y 5.")
        except ValueError:
            print("Debe ingresar un número.")

    # TERCERA NOTA
    while True:
        try:
            nota3 = float(input("Tercera nota (0 - 5): "))
            if nota3 >= 0 and nota3 <= 5:
                break
            else:
                print("La nota debe estar entre 0 y 5.")
        except ValueError:
            print("Debe ingresar un número.")

    # CALCULAR PROMEDIO
    promedio = (nota1 + nota2 + nota3) / 3

    # DETERMINAR ESTADO
    if promedio >= 3:
        print("Promedio:", round(promedio, 2))
        print("Estado: Aprobado")
        aprobados = aprobados + 1

    else: 
        print("Promedio:", round(promedio, 2))
        print("Estado: Reprobado")
        reprobados = reprobados + 1

    suma_promedios = suma_promedios + promedio

    # CALCULAR PROMEDIO GENERAL 
    promedio_grupo = suma_promedios / cantidad_estudiantes

    # RESUMEN
    print("\n==========")
    print("  RESUMEN DEL GRUPO")
    print("============")
    print("Total estudiantes:", cantidad_estudiantes)
    print("Aprobados:", aprobados)
    print("Reprobados:", reprobados)
    print("Promedio General:", round(promedio_grupo, 2))
    print("============")

            