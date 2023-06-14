import funcionesCarrito

    


print("Bienvenido a la tienda de zapatillas")
opcion=funcionesCarrito.menuPrincipal()
print("Usted selecciono la opción: ", opcion)
while opcion != 6:
    if opcion == 1:
        funcionesCarrito.productosDispo()
        print("-------------------------Mostrar productos en detalle-------------------------")
        funcionesCarrito.mostrarProductosEnDetalle()
    elif opcion == 2:
        funcionesCarrito.productosDispo()
        print("-------------------------Mostrar informacion breve-------------------------")
        funcionesCarrito.mostrarProductosBreve()
    elif opcion == 3:
        funcionesCarrito.productosDispo()
        print("-------------------------Buscar producto por codigo-------------------------")
        funcionesCarrito.buscarProductoPorCodigo(codigo=int(input("Ingrese el codigo del producto: ")))
    elif opcion == 4:
        print("-------------------------Realizar compra-------------------------")
        funcionesCarrito.realizarCompra()
    elif opcion == 5:
        print("-------------------------Finalizar compra-------------------------")
        funcionesCarrito.finalizarCompra()
    else:
        print("Opción incorrecta")
    opcion=funcionesCarrito.menuPrincipal()
    print("Usted selecciono la opción: ", opcion)
print("Gracias por su visita")

    
