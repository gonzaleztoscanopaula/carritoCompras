
class Productos:
    def __init__(self, codigo, nombre, marca, precio, stock, color, caracteristicas):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock
        self.color = color
        self.caracteristicas = caracteristicas

    def detalleCompleto(self):
        return f"Producto código: {self.codigo} = Nombre: {self.nombre}\n Marca: {self.marca}\n Precio: {self.precio}\n Stock: {self.stock}\n Color: {self.color}\n Caracteristicas:{self.caracteristicas}"
    def detalleBreve(self):
        return f"Producto código: {self.codigo} = Nombre: {self.nombre} - Marca:{self.marca} - Precio:{self.precio} - Stock:{self.stock}"
    def buscarProductoPorCodigo(self):
        return f"El producto código: {self.codigo} = Nombre: {self.nombre} - Marca:{self.marca} - Precio:{self.precio} - Stock:{self.stock}"



producto1= Productos(1, "zapatillas", "new balance", 23000, 7, "negro", "zapatillas negras con inscripcion en blanco, todos los talles")
producto2= Productos(2, "zapatillas", "adidas", 45000, 3, "Verdes", "Zapatillas verdes con suela roja, todos los talles")
producto3= Productos(3, "zapatillas", "puma", 32000, 5, "blanco", "Zapatillas blancas con cordones celestes, todos los talles") 
producto4= Productos(4, "ojotas", "new balance", 15000, 9, "azul", "Ojotas azules, con lineas blancas, todos los talles")   


def menuPrincipal():
    print("1. Mostrar productos en detalles")
    print("2. Mostrar información breve del producto")
    print("3. Buscar producto por código")
    print("4. Realizar compra")
    print("5. Ver mi carro")
    print("6. Finalizar compra")
    print("7. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion.isnumeric():
        opcion = int(opcion)
        if opcion >= 1 and opcion <= 6:
                continuar = True
                while continuar:
                    if opcion == 1:
                        print("-------------------------Mostrar productos en detalle-------------------------")
                        mostrarProductosEnDetalle()
                    elif opcion == 2:
                        print("-------------------------Mostrar informacion breve-------------------------")
                        mostrarProductosBreve()
                    elif opcion == 3:
                        print("-------------------------Buscar producto por codigo-------------------------")
                        print("Los productos disponibles son:")
                        print(producto1.detalleBreve())
                        print(producto2.detalleBreve())
                        print(producto3.detalleBreve())
                        print(producto4.detalleBreve())
                        buscarProductoPorCodigo(codigo=input("Ingrese el codigo del producto: "))
                    elif opcion == 4:
                        print("-------------------------Realizar compra-------------------------")
                        realizarCompra()
                    elif opcion == 5:
                        print("-------------------------Ver mi carro-------------------------")
                        verCarrito()
                    elif opcion == 6:
                        print("-------------------------Finalizar compra-------------------------")
                        finalizarCompra()
                    else:
                        print("Opción incorrecta")
                        print("Ingrese una opción válida del 1 al 7")
                        print("Presione enter para volver a menu principal")
                        input()
                        menuPrincipal()
        elif opcion == 7:
            print("Gracias por su visita")
            print("Hasta luego")
            exit()                
        else:
            print("Opción incorrecta")
            print("Ingrese una opción válida del 1 al 6")
            print("Presione enter para volver a menu principal")
            input()
            menuPrincipal()  






def mostrarProductosEnDetalle():
    print("1. Mostrar productos en detalles")
    print(producto1.detalleCompleto())
    print(producto2.detalleCompleto())
    print(producto3.detalleCompleto())
    print(producto4.detalleCompleto())
    print("Presione enter para volver a menu principal")
    input()
    menuPrincipal()

def mostrarProductosBreve():
    print("2. Mostrar informacón breve del producto")
    print(producto1.detalleBreve())
    print(producto2.detalleBreve())
    print(producto3.detalleBreve())
    print(producto4.detalleBreve())
    print("Presione enter para volver a menu principal")    
    input()
    menuPrincipal()



#-------------------------------------3funcion para buscar los productos por codigo
def buscarProductoPorCodigo(codigo):
    if codigo.isnumeric():
        codigo = int(codigo)
        if codigo >= 1 and codigo <= 4:
            if codigo == 1:
                print(producto1.detalleBreve())
            elif codigo == 2:
                print(producto2.detalleBreve())
            elif codigo == 3:
                print(producto3.detalleBreve())
            elif codigo == 4:
                print(producto4.detalleBreve())
            
            opcion = input("Desea buscar otro producto? (1. Si / 2. No): ")
            if opcion == "1":
                buscarProductoPorCodigo(input("Ingrese el código del producto: "))
            elif opcion == "2":
                menuPrincipal()
            else:
                print("Opción incorrecta")
                print("Ingrese una opción válida (1 o 2)")
                buscarProductoPorCodigo(input("Ingrese el código del producto: "))
        else:
            print("El código ingresado no se encuentra disponible")
            input("Presione enter para volver a ingresar el código")
            buscarProductoPorCodigo(input("Ingrese el código del producto: "))
    else:
        print("El código ingresado no es válido")
        input("Presione enter para volver a ingresar el código")
        buscarProductoPorCodigo(input("Ingrese el código del producto: "))



compras = {}
def realizarCompra():
    print("Realizar compra")
    print(producto1.detalleBreve())
    print(producto2.detalleBreve())
    print(producto3.detalleBreve())
    print(producto4.detalleBreve())
    while True:
        codigo = input("Ingrese el código del producto que desea comprar (0 para finalizar): ")
        if codigo == '0':
            print("Presione enter para volver al menú principal")
            input()
            menuPrincipal()
            return compras
        if codigo.isnumeric():
            codigo = int(codigo)
            if codigo < 1 or codigo > 4:
                print("Código de producto inválido")
                print("Ingrese un código de producto válido")
                print("Presione enter para volver al menú principal")
                input()
                menuPrincipal()
            producto = None
            if codigo == 1:
                producto = producto1
            elif codigo == 2:
                producto = producto2
            elif codigo == 3:
                producto = producto3
            elif codigo == 4:
                producto = producto4
            if producto is None:
                print("El código del producto no existe")
                print("Presione enter para volver al menú principal")
                input()
                menuPrincipal()
            cantidad = input("Ingrese la cantidad que desea comprar: ")
            if cantidad.isnumeric():
                cantidad = int(cantidad)
                if cantidad <= producto.stock:
                    producto.stock -= cantidad
                    precio_unitario = producto.precio
                    costo_total = cantidad * precio_unitario
                    compra = {
                        "nombre": producto.nombre,
                        "cantidad": cantidad,
                        "precio_unitario": precio_unitario,
                        "costo_total": costo_total
                    }
                    compras[codigo] = compra
                    print("Compra realizada con éxito:")
                    print(compra)
                    print("Presione enter para volver a comprar")
                    input()
                    realizarCompra()
                    return globals(compras) 
                else:
                    print("No hay suficiente stock")
                    print("Presione enter para volver a comprar")
                    input()
                    realizarCompra()
            else:
                print("La cantidad debe ser un número válido")
                print("Presione enter para volver a comprar")
                input()
                realizarCompra()
        else:
            print("El código del producto debe ser un número válido")
            print("Presione enter para volver a comprar")
            input()
            realizarCompra()


def finalizarCompra():
    global compras    
    if len(compras) == 0:
        print("No hay productos en el carrito")
        print("Presione enter para volver al menú realizar compra")
        input()
        return menuPrincipal()
    else:
        print("Los productos comprados son:")  
        imprimirDiccionario(compras)
        total = sum(compra["costo_total"] for compra in compras.values())
        print("El total de la compra es:", float(total))    
    while True:
        print("Desea finalizar la compra?")
        print("1. Sí")
        print("2. No")
        opcion = input("Ingrese una opción: ")     
        if opcion.isnumeric():
            opcion = int(opcion)  
            if opcion == 1:
                print("¿Cómo quiere abonar su compra?")
                print("1. Efectivo")
                print("2. Tarjeta de crédito")
                print("3. Tarjeta de débito")
                opcion = input("Ingrese una opción: ")
                if opcion.isnumeric():
                    opcion = int(opcion)
                    if opcion == 1:
                        imprimirTicket(total, "EFECTIVO")
                        print("Gracias por su compra, presione enter para volver al menu")
                        input()
                        menuPrincipal()
                    elif opcion == 2:
                        imprimirTicket(total, "TARJETA DE CRÉDITO")
                        print("Gracias por su compra, presione enter para volver al menu")
                        input()
                        menuPrincipal() 
                    elif opcion == 3:
                        imprimirTicket(total, "TARJETA DE DÉBITO")
                        print("Gracias por su compra, presione enter para volver a menu")
                        input()
                        menuPrincipal()
                    else:
                        print("Opción incorrecta")
                else:
                    print("Opción incorrecta")
            elif opcion == 2:
                print("Presione enter para volver al menú principal")
                input()
                return menuPrincipal()
            else:
                print("Opción incorrecta")
        else:
            print("Opción incorrecta")


def imprimirTicket(total, forma_pago):
    print("----------------TICKET DE LA ABUELA----------------")
    print("El total de la compra es: $" + str(total))
    print("Forma de pago: " + forma_pago)
    print("Los productos comprados son:")
    imprimirDiccionario(compras)
    print("La compra se ha realizado con éxito. Gracias por ayudar a la economía de la abuela.")



def verCarrito():
    global compras
    print("6. Ver carrito")
    if len(compras) == 0:
        print("No hay productos en el carrito")
        print("Presione enter para volver al menu realizar compra")
        input()
        return menuPrincipal()
    else:
        print("Los productos comprados son: ")
        imprimirDiccionario(compras)
        print("¿Quiere eliminar algun producto el carro?")
        print("1. Si")
        print("2. No")
        opcion = input("Ingrese una opcion: ")
        if opcion.isnumeric():
            opcion = int(opcion)
            if opcion == 1:
                return eliminarProductos()
            if opcion == 2:
                print("Presione enter para volver al menu principal")
                input()
                return menuPrincipal()
            else:
                print("Opción incorrecta")
                print("Ingrese una opción valida del 1 al 2")
                return verCarrito()
        else:
            print("Opción incorrecta")
            print("Ingrese una opción valida del 1 al 2")
            return verCarrito()


def eliminarProductos():
    global compras
    codigo = input("Ingrese el código del producto que desea eliminar: ")
    if codigo.isnumeric():
        codigo = int(codigo)
        if codigo in compras:
            cantidad = input("Ingrese la cantidad que desea eliminar: ")
            if cantidad.isnumeric():
                cantidad = int(cantidad)
                if cantidad > compras[codigo]["cantidad"]:
                    print("La cantidad ingresada es mayor a la cantidad comprada")
                    print("Presione enter para volver a ingresar la cantidad")
                    input()
                    eliminarProductos()
                elif cantidad == compras[codigo]["cantidad"]:
                    producto = obtenerProductoPorCodigo(codigo)  
                    if producto is not None:
                        producto.stock += cantidad 
                    del compras[codigo]
                    print("El producto se ha eliminado con éxito")
                    print("Presione enter para volver al menú principal")
                    input()
                    return menuPrincipal()
                else:
                    compras[codigo]["cantidad"] = compras[codigo]["cantidad"] - cantidad
                    compras[codigo]["costo_total"] = compras[codigo]["costo_total"] - compras[codigo]["precio_unitario"] * cantidad
                    producto = obtenerProductoPorCodigo(codigo) 
                    if producto is not None:
                        producto.stock += cantidad  
                    print("El producto se ha eliminado con éxito")
                    imprimirDiccionario(compras)
                    print("Presione enter para volver al menú principal")
                    input()
                    return menuPrincipal()
            else:
                print("La cantidad ingresada no es válida")
                print("Presione enter para volver a ingresar la cantidad")
                input()
                eliminarProductos()
        else:
            print("El código ingresado no es válido")
            print("Presione enter para volver a ingresar el código")
            input()
            eliminarProductos()
    else:
        print("El código ingresado no es válido")
        print("Presione enter para volver a ingresar el código")
        input()
        eliminarProductos()

def obtenerProductoPorCodigo(codigo):
    if codigo == 1:
        return producto1
    elif codigo == 2:
        return producto2
    elif codigo == 3:
        return producto3
    elif codigo == 4:
        return producto4
    else:
        return None

def imprimirDiccionario(compras):
    for clave, valor in compras.items():
        print(clave, ":", valor)
        print() 
