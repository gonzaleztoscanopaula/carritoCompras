#Compras
Crear un carrito de compras en Python que funcione únicamente en la consola. 
El programa debe presentar un menú con las siguientes opciones:
1-Mostrar productos en detalle: Muestra el código del producto, nombre, marca, precio, stock, color y características de cada producto en la tienda.
2-Mostrar información breve del producto: Muestra el código del producto, nombre, precio y cantidad disponible de cada producto en la tienda.
3-Buscar producto por código: Permite al usuario ingresar un código de producto y muestra la información detallada de ese producto.
4-Realizar compra: Permite al usuario agregar productos al carrito de compras. Se generará un nuevo diccionario con el nombre del producto, la cantidad comprada, el precio unitario y el costo total por cada item añadido.
5-Finalizar compra: Cierra la compra y muestra un detalle de los productos comprados, incluyendo el nombre, la cantidad, el precio unitario y el costo total.
6-Salir: Permite al usuario salir del programa.

Deberá contar el programa con una visualización previa de los productos añadidos en el carrito en la cual se le consulte al usuario si está conforme o no con los productos añadidos , teniendo en cuenta el desarrollo que pueda desencadenar si el usuario desea MODIFICAR lo que tiene en el carrito , es decir que si desea modificar lo que tiene en el carrito pueda modificar la cantidad de un producto determinado , para aumentar o disminuir la cantidad o eliminar del carrito completamente algún producto.

*Además, se debe actualizar permanentemente el stock de los productos y validar la existencia de la cantidad de productos antes de realizar una compra. 

*El programa debe mostrar al usuario un diccionario con la información de los productos disponibles en la tienda.

*Debe validar las opciones seleccionadas por el usuario en el menú.

*Mientras el usuario esté navegando en el carrito de compras, los datos deben permanecer disponibles. 

El programa debe incluir una opción en el menú para cerrar la compra y mostrar un detalle de los productos comprados.

También se debe validar que el resultado total de la compra pueda incluir números decimales.

Para buscar productos, se debe validar el ingreso del ID del producto.

Por cada acción que el usuario seleccione, se debe validar si la respuesta es 'SI' o 'NO'."

Se validará todos los ingresos y egresos de información del sistema.

Este programa debe ser una réplica de  todas las aplicaciones de compras en línea conocidas. 

Fecha inicio: 29-05-2023
Fecha fin: 22-06-2023 (sin excepción)



"""
def realizarCompra(codigo):
#4-Realizar compra: Permite al usuario agregar productos al carrito de compras. 
#Se generará un nuevo diccionario con el nombre del producto, la cantidad comprada, 
#el precio unitario y el costo total por cada item añadido.
    if codigo.isnumeric():
        codigo = int(codigo)
        if codigo >= 1 and codigo <= 4:
            print(Productos.detalleBreve())
            if codigo in Productos.codigo: 
                cantidad = input("Ingrese la cantidad que desea comprar: ")
                if cantidad.isnumeric():
                    cantidad = int(cantidad)
                    if cantidad >= 1 and cantidad <= producto1.stock:
                        print("El precio unitario es de: ", producto1.precio)
                        print("El costo total es de: ", producto1.precio*cantidad)
                        print("Desea agregar este producto al carrito?")
                        print("1. Si, agregarlo a mi carrito")
                        print("2. No, eliminarlo del carrito")
                        opcion = input("Ingrese una opcion: ")
                        if opcion.isnumeric():
                            opcion = int(opcion)
                            if opcion == 1:
                                producto1.stock = producto1.stock - cantidad
                                carrito = {producto1.nombre:{"marca":producto1.marca, "cantidad":cantidad, "precio unitario":producto1.precio, "costo total":producto1.precio*cantidad}}
                                print("Los productos comprados son: ")
                                print(carrito)
                                print("Presione enter para volver al menu realizar compra")
                                input()
                                return funcionMenu(4)
                            elif opcion == 2:
                                print("Desea eliminar el producto del carrito?")
                                print("1. Si")
                                print("2. No")
                                opcion = input("Ingrese una opcion: ")
                                if opcion.isnumeric():
                                    producto1.stock = producto1.stock + cantidad
                                    opcion = int(opcion)
                                    if opcion == 1:
                                        carrito = list(carrito)
                                        carrito.remove(producto1.nombre)
                                        print("Los productos comprados son: ")
                                        print(carrito)
                                        carrito= dict(carrito)
                                        print("Presione enter para volver al menu realizar compra")
                                        input()
                                        return funcionMenu(4)
                                    elif opcion == 2:
                                        print("Presione enter para volver al menu realizar compra")
                                        return menuPrincipal()
                                    else:
                                        print("Opción incorrecta")
                                        print("Ingrese una opción valida del 1 al 2")
                                        return funcionMenu(4)
                                else: 
                                    return funcionMenu(4)  
                            else:
                                print("Opción incorrecta")
                                print("Ingrese una opción valida del 1 al 2")
                                return funcionMenu(4)
                    else:
                        print("La cantidad ingresada no se encuentra disponible")
                        print("Presione enter para volver a ingresar la cantidad")
                        input()
                        return funcionMenu(4)
                else:
                    print("La cantidad ingresada no es valida")
                    print("Presione enter para volver a ingresar la cantidad")
                    input()
                    return funcionMenu(4)
            elif codigo == 2:
                print(producto2.detalleBreve())
                cantidad = input("Ingrese la cantidad que desea comprar: ")
                if cantidad.isnumeric():
                    cantidad = int(cantidad)
                    if cantidad >= 1 and cantidad <= producto2.stock:
                        print("El precio unitario es de: ", producto2.precio)
                        print("El costo total es de: ", producto2.precio*cantidad)
                        print("Desea agregar este producto al carrito?")
                        print("1. Si, agregarlo a mi carrito")
                        print("2. No, eliminarlo del carrito")
                        opcion = input("Ingrese una opcion: ")
                        if opcion.isnumeric():
                            opcion = int(opcion)
                            if opcion == 1:
                                producto2.stock = producto2.stock - cantidad
                                carrito = {producto2.nombre:{"marca":producto2.marca, "cantidad":cantidad, "precio unitario":producto2.precio, "costo total":producto2.precio*cantidad}}
                                print("Los productos comprados son: ")
                                print(carrito)
                                print("Presione enter para volver al menu realizar compra")
                                input()
                                return funcionMenu(4)
                            elif opcion == 2:
                                print("Desea eliminar el producto del carrito?")
                                print("1. Si")
                                print("2. No")
                                opcion = input("Ingrese una opcion: ")
                                if opcion.isnumeric():
                                    producto2.stock = producto2.stock + cantidad
                                    opcion = int(opcion)
                                    if opcion == 1:
                                        carrito.pop(producto2.nombre)
                                        print("Los productos comprados son: ")
                                        print(carrito)
                                        print("Presione enter para volver al menu realizar compra")
                                        input()
                                        return funcionMenu(4)
                                    elif opcion == 2:
                                        print("Presione enter para volver al menu realizar compra")
                                        return menuPrincipal()
                                    else:
                                        print("Opción incorrecta")
                                        print("Ingrese una opción valida del 1 al 2")
                                        return funcionMenu(4)
                                else: 
                                    return funcionMenu(4)   
                            else:
                                print("Opción incorrecta")
                                print("Ingrese una opción valida del 1 al 2")
                                return funcionMenu(4)
                    else:
                        print("La cantidad ingresada no se encuentra disponible")
                        print("Presione enter para volver a ingresar la cantidad")
                        input()
                        return c
                else:
                    print("La cantidad ingresada no es valida")
                    print("Presione enter para volver a ingresar la cantidad")
                    input()
                    return funcionMenu(4)
            elif codigo == 3:
                print(producto3.detalleBreve())
                cantidad = input("Ingrese la cantidad que desea comprar: ")
                if cantidad.isnumeric():
                    cantidad = int(cantidad)
                    if cantidad >= 1 and cantidad <= producto3.stock:
                        print("El precio unitario es de: ", producto3.precio)
                        print("El costo total es de: ", producto3.precio*cantidad)
                        print("Desea agregar este producto al carrito?")
                        print("1. Si, agregarlo a mi carrito")
                        print("2. No")
                        opcion = input("Ingrese una opcion: ")
                        if opcion.isnumeric():
                            opcion = int(opcion)
                            if opcion == 1:
                                producto3.stock = producto3.stock - cantidad
                                carrito = {producto3.nombre:{"marca":producto3.marca, "cantidad":cantidad, "precio unitario":producto3.precio, "costo total":producto3.precio*cantidad}}
                                print("Los productos comprados son: ")
                                print(carrito)
                                print("Presione enter para volver al menu realizar compra")
                                input()
                                return funcionMenu(4)
                            elif opcion == 2:
                                print("Eliminar producto del carrito")
                                carrito = {producto3.nombre:{"marca":producto3.marca, "cantidad":cantidad, "precio unitario":producto3.precio, "costo total":producto3.precio*cantidad}}
                                producto3.stock = producto3.stock + carrito[producto3.nombre]["cantidad"]
                                #eliminar producto del diccionario carrito
                                carrito.pop(producto3.nombre)
                                print("Presione enter para volver al menu realizar compra")
                                input()
                                return funcionMenu(4)
                            else:
                                print("Opción incorrecta")
                                print("Ingrese una opción valida del 1 al 2")
                                return funcionMenu(4)
                        else:
                            print("La cantidad ingresada no se encuentra disponible")
                            print("Presione enter para volver a ingresar la cantidad")
                            input()
                            return funcionMenu(4)                   
                    else:
                        print("La cantidad ingresada no se encuentra disponible")
                        print("Presione enter para volver a ingresar la cantidad")
                        input()
                        return funcionMenu(4)
                else:
                    print("La cantidad ingresada no es valida")
                    print("Presione enter para volver a ingresar la cantidad")
                    input()
                    return funcionMenu(4)
            elif codigo == 4:
                print(producto4.detalleBreve())
                cantidad = input("Ingrese la cantidad que desea comprar: ")
                if cantidad.isnumeric():
                    cantidad = int(cantidad)
                    if cantidad >= 1 and cantidad <= producto4.stock:
                        print("El precio unitario es de: ", producto4.precio)
                        print("El costo total es de: ", producto4.precio*cantidad)
                        print("Desea agregar este producto al carrito?")
                        print("1. Si, agregarlo a mi carrito")
                        print("2. No, eliminarlo del carrito")
                        opcion = input("Ingrese una opcion: ")
                        if opcion.isnumeric():
                            opcion = int(opcion)
                            if opcion == 1:
                                producto2.stock = producto4.stock - cantidad
                                carrito = {producto4.nombre:{"marca":producto4.marca, "cantidad":cantidad, "precio unitario":producto4.precio, "costo total":producto4.precio*cantidad}}
                                print("Los productos comprados son: ")
                                print(carrito)
                                print("Presione enter para volver al menu realizar compra")
                                input()
                                return funcionMenu(4)
                            elif opcion == 2:
                                print("Desea eliminar el producto del carrito?")
                                print("1. Si")
                                print("2. No")
                                opcion = input("Ingrese una opcion: ")
                                if opcion.isnumeric():
                                    producto4.stock = producto4.stock + cantidad
                                    opcion = int(opcion)
                                    if opcion == 1:
                                        carrito.pop(producto4.nombre)
                                        print("Los productos comprados son: ")
                                        print(carrito)
                                        print("Presione enter para volver al menu realizar compra")
                                        input()
                                        return funcionMenu(4)
                                    elif opcion == 2:
                                        print("Presione enter para volver al menu realizar compra")
                                        return menuPrincipal()
                                    else:
                                        print("Opción incorrecta")
                                        print("Ingrese una opción valida del 1 al 2")
                                        return funcionMenu(4)
                                else: return funcionMenu(4)    
                            else:
                                print("Opción incorrecta")
                                print("Ingrese una opción valida del 1 al 2")
                                return realizarCompra()
                    else:
                        print("La cantidad ingresada no se encuentra disponible")
                        print("Presione enter para volver al menu compras")
                        input()
                        return funcionMenu(4)
                else:
                    print("La cantidad ingresada no es valida")
                    print("Presione enter para volver al menu compras")
                    input()
                    return funcionMenu(4)
        else:
            print("El código ingresado no es valido")
            print("Presione enter para volver al menu compras")
            input()        
            return funcionMenu(4)       
    else:
        print("El código ingresado no es valido")
        print("Presione enter para volver al menu compras")
        input()        
        return funcionMenu(4)
"""





