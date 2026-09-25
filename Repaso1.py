#variables
print("=== Tienda donde Ely ===")

print("Por favor ingrese la siguiente información: \n")
cliente =input("Nombre de cliente: ")
producto =input("Nombre de producto: ")
cantidad =int(input("Cantidad: "))
precio = float(input("Precio: "))

#Variable para preguntar si la compra es a domicilio
domicilio =input("La compra es para domicilio (SI - NO): ")
#Condicional, verificar que responde el usuario

if domicilio.upper() =="NO": 
    print("=== RESUMEN DE COMPRA ===")
    print(f"""
    -Cliente : {cliente}
    -Producto : {producto}
    -Cantidad : {cantidad}
    -Precio : {precio}
    -Total : {cantidad*precio}

    🛒 Gracias por su compra👌
    """)

elif domicilio.upper ()=="SI":
    direccion=input("Ingrese municipio de envio (Medellín, Itagüi, Bello) :")
    valor_domicilio=0
    if direccion.lower()=="medellín":
        valor_domicilio =5000
    elif direccion.lower()=="Itagüi":
        valor_domicilio=10000
    elif direccion.lower()=="Bello":
        vaor_domicilio=8000
    else:
        print("Dirección Invalida")

    #Mostrar Resumen de Venta
    print("=== RESUMEN DE COMPRA ===")
    print(f"""
    -Cliente: {cliente}
    -Producto: {producto}
    -Cantidad: {cantidad}
    -Precio: {precio}
    -Subtotal: {cantidad*precio}
    -Domicilio: {valor_domicilio}
    -Total a Pagar: {valor_domicilio + (cantidad*precio)}
    
        🛒 Gracias por su compra👌
    """)

else:
    print("Opcion Invalida")
    