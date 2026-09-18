print("ejercicio 1: Suma de dos números")
print(".."*20)

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = numero1 + numero2    # Se le calcula la suma
print(f"La suma es: {suma}")


print("ejercicio 2: Área de un rectángulo")
print(".."*20)

base =float(input("Ingresa la base del rectángulo: "))
altura =float(input("Ingresa la altura del restángulo: "))

area = base * altura    #formula: base * altura

print(f"El área del rectángulo es: {area}")


print("ejercicio 3: Conversión de minutos a horas y minutos")
print(".."*20)

minutos_totales = int(input("Ingresa la cantidad de minutos: "))

horas = minutos_totales // 60  #división entera - horas completas
minutos = minutos_totales % 60 #módulo - minutos restantes

print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos")


print("ejercicio 4: Cálculo del precio con descuento")
print(".."*20)

precio =float(input("Ingrese el precio del producto: "))
descuento =float(input("Ingrese el porcentaje de desceunto: "))

valor_descuento = precio + (descuento / 100)        #valor que se descuenta
precio_final    = precio - valor_descuento          #precio con descuento

print(f"El precio final a pagar es: {precio_final}")


print("ejercicio 5: Intercambio de valores entre dos variables")
print(".."*20)

a = float(input("Ingrese el valor de a: "))
b = float(input("ingrese el valor de b: "))

auxiliar = a                #guardar temporalmente el valor de a
a = b                       #a tomar el valor de b
b = auxiliar                #b toma el valor original de a

print(f"Después del intercambio: a = {a} , b = {b}")
