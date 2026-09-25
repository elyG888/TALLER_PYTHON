#Repaso Ciclos
"""
lista_producto=[]  #Lista en blanco
cantidad=int(input("cantidad de productos a comprar: "))

for i in range(cantidad):
    producto=input(f"Nombre del producto {i+1}: ")
    #Agregar producto a la lista
    lista_producto.append(producto)
print(f"Productos comprados: {lista_producto}")
"""
lista_perro=[]
lista_gato=[]

while True:
    pregunta=int(input("""
    1. Registrar perritos 🐶
    2. Registrar Gaticos 🐈
    3. Listado Perritos 🐾
    4. Listado Gaticos 😸
    5. Salir
    """))

    if pregunta ==1:
        perro= input("Ingrese nombre del perro: ")
        lista_perro.append(perro)
        print("perrito registrado")

    elif pregunta ==2:
        gato= input("Ingrese nombre del gato: ")
        lista_gato.append(gato)
        print("Gatico registrado")

    elif pregunta ==3:
        print("Listado perritos", lista_perro)

    elif pregunta ==4:
        print("Listado gaticos", lista_gato)  

    elif pregunta ==5:
        print("Saliendo del sistema")
        break
    else:
        print("Opción Invalida")
        break


