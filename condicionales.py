"""
Condicionales: Permiten validar cunado se cumple o no una condición.
"""

#Crear Variable 
"""print("Por favor ingrese los siguientes datos\n")

var_nombre = input("Nombre: ")
var_edad = int(input("Edad: "))

#Crear condición
if var_edad >= 18 :
    print(f"{var_nombre} Eres mayor de Edad.")
else: 
    print(f"{var_nombre} Eres menor de Edad.")
    """
"""#Ejempplo 2
print("Ejercicio: Nota Final")
var_nombre = input("Nombre: ")
var_notaFinal = float(input("Nota Final: "))

if var_notaFinal < 0 or var_notaFinal >5: 
    print("Nota invalida")

elif var_notaFinal >= 3.5 :
    print(f"Estudiante {var_nombre} GANO 🥳")

else:
    print(f"Estudiante {var_nombre} PERDIO 😢")
    """
#Ejercicio 1 Calculo edad mayor
"""
var_nombre = input("Ingresa tu nombre: ")
var_edad = float(input("Ingresa tu edad: "))
mayor_edad = 18

if var_edad < 18 :
    print(f"{var_nombre} Es menor de edad, te faltan {mayor_edad - var_edad} años para ser mayor de edad.")

elif var_edad <0 :
    print(f"{var_edad} No es edad valida")
"""

#Ejercicio 2 Nombre de estudiante y calificacion final
"""
var_NombreEstudiante = input("Ingresa nombre de estudiante: ")
nota = float(input("Ingresa tu nota final:  "))

#0-3 = Insuficiente
if nota < 0 or nota > 5 :
    print(f"{nota} Invalida")

elif nota <3:
    print(f"{nota} Insuficiente")

elif nota < 3.4:
    print(f"{nota} Aceptable")

elif nota < 4.5:
    print(f"{nota} Bueno")

else :
    print(f"{nota} Excelente")
"""


#Ejercicio 3 Descuento Compra
"""print("Ejercicio: Valor compra y descuento")
var_nombreCliente = input("Nombre: ")
var_totalCompra = float(input("Ingrese total compra: "))

var_Compra10 = var_totalCompra * 0.1
var_Compra15 = var_totalCompra * 0.15
var_Compra20 = var_totalCompra * 0.20



if var_totalCompra <= 100000:
    print(f"{var_nombreCliente} Sin Descuento")

elif var_totalCompra <299999 :
    print(f"{var_nombreCliente} tienes 10% de descuento por tu compra de: ${var_Compra10}, su valor real a pagar es ${var_totalCompra - var_Compra10}  ")
    
elif var_totalCompra < 499999 :
    print(f"{var_nombreCliente} tienes 15% de descuento por tu compra de: ${var_Compra15}, su valor real a pagar es ${var_totalCompra - var_Compra15}  ")
    
else : 
    print(f"{var_nombreCliente} tienes 20% de descuento por tu compra de ${var_Compra20}, su valor real a pagar es ${var_totalCompra - var_Compra20}  ")"""

# Ejercicio 4 Clima
"""
ciudad = input("Ingresa la ciudad: ")
temp_actual = float(input("Ingrese la temperatura actual de la ciduad: "))

if temp_actual <10 :
    print(f"En {ciudad}, El clima esta muy frío, se recomienda usar abrigo")

elif temp_actual <17 :
    print(f"En {ciudad}, El clima esta frío, se recomienda usar abrigo")

elif temp_actual <25 :
    print(f"En {ciudad}, El clima esta templado")

elif temp_actual <32 :
    print(f"En {ciudad}, El clima esta caliente")

else:
    print(f"En {ciudad}, El clima esta muy caliente")
"""


# Ejercicio 5 Horas trabajadas

Empleado = input("Ingresa el nombre del empleado: ")
HorasMes = int(input("Ingresar las horas trabajadas por el empleado: "))

valor_Hora = float(input("valor hora: "))

if HorasMes < 160 :
    salario = HorasMes * valor_Hora
    descuento = salario * 0.08
    print(f"Total a pagar: {salario-descuento} ")

elif HorasMes > 160 :
    salario = HorasMes * valor_Hora
    descuento = salario * 0.08 
    horaExtra = 1.25
    print(f"Total a pagar: {salario-descuento} + {horaExtra} ")





