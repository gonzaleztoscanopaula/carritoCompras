carrito=[]
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

#----------------------------1 funcion para Mostrar el menu principal
def menuPrincipal():
    print("1. Mostrar productos en detalles")
    print("2. Mostrar informacón breve del producto")
    print("3. Buscar producto por código")
    print("4. Realizar compra")
    print("5. Finalizar compra")
    print("6. Salir")
    opcion = input("Ingrese una opcion: ")   
    if opcion.isnumeric():
        opcion = int(opcion)
        if opcion >= 1 and opcion <= 6:
                funcionMenu(opcion)     
    else:
        print("Opción incorrecta")
        print("Ingrese una opción valida del 1 al 6")
        print("Presione enter para volver a menu principal")
        input()
        return menuPrincipal()

        
#----------------------------2 funcion del menu principal        
def funcionMenu(opcion):
    while opcion !=0 and opcion != 6:
                if opcion == 1:
                    print("-------------------------Mostrar productos en detalle-------------------------")
                    return mostrarProductosEnDetalle()
                elif opcion == 2:
                    print("-------------------------Mostrar informacion breve-------------------------")
                    return mostrarProductosBreve()
                elif opcion == 3:
                    print("-------------------------Buscar producto por codigo-------------------------")
                    print("Los productos disponibles son:")
                    print(producto1.detalleBreve())
                    print(producto2.detalleBreve())
                    print(producto3.detalleBreve())
                    print(producto4.detalleBreve())                    
                    return buscarProductoPorCodigo(codigo=(input("Ingrese el codigo del producto: ")))
                elif opcion == 4:
                    print("-------------------------Realizar compra-------------------------")
                    print("Los productos disponibles son:")
                    print(producto1.detalleBreve())
                    print(producto2.detalleBreve())
                    print(producto3.detalleBreve())
                    print(producto4.detalleBreve()) 
                    return realizarCompra(codigo=(input("Ingrese el codigo del producto que desea comprar: ")))
                else:
                     print("-------------------------Finalizar compra-------------------------")
                     #finalizarCompra()




#---------------------------------1funcion para mostrar productos en detalles
def mostrarProductosEnDetalle():
    print("1. Mostrar productos en detalles")
    print(producto1.detalleCompleto())
    print(producto2.detalleCompleto())
    print(producto3.detalleCompleto())
    print(producto4.detalleCompleto())
    print("Presione enter para volver a menu principal")
    input()
    return menuPrincipal()

#----------------------------------2funcion para mostrar productos con detalle breve
def mostrarProductosBreve():
    print("2. Mostrar informacón breve del producto")
    print(producto1.detalleBreve())
    print(producto2.detalleBreve())
    print(producto3.detalleBreve())
    print(producto4.detalleBreve())
    print("Presione enter para volver a menu principal")    
    input()
    return menuPrincipal()



#-------------------------------------3funcion para buscar los productos por codigo
def buscarProductoPorCodigo(codigo):
    if codigo.isnumeric():
        codigo = int(codigo)
        if codigo >= 1 and codigo <= 4:  
            if codigo == 1:
                print(producto1.detalleBreve())
                print("Desea buscar otro producto?")
                print("1. Si")
                print("2. No")
                opcion = input("Ingrese una opcion: ")
                if opcion.isnumeric():
                    opcion = int(opcion)
                    if opcion == 1:
                        return buscarProductoPorCodigo(codigo=(input("Ingrese el codigo del producto: ")))
                    elif opcion == 2:
                        return menuPrincipal()
                    else:
                        print("Opción incorrecta")
                        print("Ingrese una opción valida del 1 al 2")
                        return buscarProductoPorCodigo(codigo=(input("Ingrese el codigo del producto: ")))
            elif codigo == 2:
                print(producto2.detalleBreve())
                print("Desea buscar otro producto?")
                print("1. Si")
                print("2. No")
                opcion = input("Ingrese una opcion: ")
                if opcion.isnumeric():
                    opcion = int(opcion)
                    if opcion == 1:
                        return buscarProductoPorCodigo(codigo=(input("Ingrese el codigo del producto: ")))
                    elif opcion == 2:
                        return menuPrincipal()
                    else:
                        print("Opción incorrecta")
                        print("Ingrese una opción valida del 1 al 2")
                        return buscarProductoPorCodigo(codigo=(input("Ingrese el codigo del producto: ")))                
            elif codigo == 3:
                print(producto3.detalleBreve())
                print("Desea buscar otro producto?")
                print("1. Si")
                print("2. No")
                opcion = input("Ingrese una opcion: ")
                if opcion.isnumeric():
                    opcion = int(opcion)
                    if opcion == 1:
                        return buscarProductoPorCodigo(codigo=(input("Ingrese el codigo del producto: ")))
                    elif opcion == 2:
                        return menuPrincipal()
                    else:
                        print("Opción incorrecta")
                        print("Ingrese una opción valida del 1 al 2")
                        return buscarProductoPorCodigo()                
            elif codigo == 4:
                print(producto4.detalleBreve())
                print("Desea buscar otro producto?")
                print("1. Si")
                print("2. No")
                opcion = input("Ingrese una opcion: ")
                if opcion.isnumeric():
                    opcion = int(opcion)
                    if opcion == 1:
                        return buscarProductoPorCodigo(codigo=(input("Ingrese el codigo del producto: ")))
                    elif opcion == 2:
                        return menuPrincipal()
                    else:
                        print("Opción incorrecta")
                        print("Ingrese una opción valida del 1 al 2")
                        return buscarProductoPorCodigo(codigo=(input("Ingrese el codigo del producto: ")))                
        else:
            print("El código ingresado no se encuentra disponible")
            print("Presione enter para volver a ingresar el codigo")
            input()
            return buscarProductoPorCodigo(codigo=(input("Ingrese el codigo del producto: ")))
    else:
        print("El código ingresado no es valido")
        print("Presione enter para volver a ingresar el codigo")
        input()        
        return buscarProductoPorCodigo(codigo=(input("Ingrese el codigo del producto: ")))


#Realizar compra: Permite al usuario agregar productos al carrito de compras. 
#Se generará un nuevo diccionario con el nombre del producto, la cantidad comprada, 
#el precio unitario y el costo total por cada item añadido.

def realizarCompra(codigo):
#4-Realizar compra: Permite al usuario agregar productos al carrito de compras. 
#Se generará un nuevo diccionario con el nombre del producto, la cantidad comprada, 
#el precio unitario y el costo total por cada item añadido.
    if codigo.isnumeric():
        codigo = int(codigo)
        if codigo >= 1 and codigo <= 4:
            if codigo == 1:
                print(producto1.detalleBreve())
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
                                return realizarCompra()
                            elif opcion == 2:
                                print("Desea eliminar el producto del carrito?")
                                print("1. Si")
                                print("2. No")
                                opcion = input("Ingrese una opcion: ")
                                if opcion.isnumeric():
                                    producto1.stock = producto1.stock + cantidad
                                    opcion = int(opcion)
                                    if opcion == 1:
                                        carrito.pop(producto1.nombre)
                                        print("Los productos comprados son: ")
                                        print(carrito)
                                        print("Presione enter para volver al menu realizar compra")
                                        input()
                                        return realizarCompra(codigo=(input("Ingrese el codigo del producto: ")))
                                    elif opcion == 2:
                                        print("Presione enter para volver al menu realizar compra")
                                        return menuPrincipal()
                                    else:
                                        print("Opción incorrecta")
                                        print("Ingrese una opción valida del 1 al 2")
                                        return realizarCompra(codigo=(input("Ingrese el codigo del producto: ")))
                                else: 
                                    return realizarCompra(codigo=(input("Ingrese el codigo del producto: ")))    
                            else:
                                print("Opción incorrecta")
                                print("Ingrese una opción valida del 1 al 2")
                                return realizarCompra(codigo=(input("Ingrese el codigo del producto: ")))
                    else:
                        print("La cantidad ingresada no se encuentra disponible")
                        print("Presione enter para volver a ingresar la cantidad")
                        input()
                        return realizarCompra(codigo=(input("Ingrese el codigo del producto: ")))
                else:
                    print("La cantidad ingresada no es valida")
                    print("Presione enter para volver a ingresar la cantidad")
                    input()
                    return realizarCompra(codigo=(input("Ingrese el codigo del producto: ")))
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
                                return realizarCompra(codigo=(input("Ingrese el codigo del producto: ")))
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
                                        return realizarCompra(codigo=(input("Ingrese el codigo del producto: ")))
                                    elif opcion == 2:
                                        print("Presione enter para volver al menu realizar compra")
                                        return menuPrincipal()
                                    else:
                                        print("Opción incorrecta")
                                        print("Ingrese una opción valida del 1 al 2")
                                        return realizarCompra(codigo=(input("Ingrese el codigo del producto: ")))
                                else: 
                                    return realizarCompra(codigo=(input("Ingrese el codigo del producto: ")))    
                            else:
                                print("Opción incorrecta")
                                print("Ingrese una opción valida del 1 al 2")
                                return realizarCompra(codigo=(input("Ingrese el codigo del producto: ")))
                    else:
                        print("La cantidad ingresada no se encuentra disponible")
                        print("Presione enter para volver a ingresar la cantidad")
                        input()
                        return realizarCompra(codigo=(input("Ingrese el codigo del producto: ")))
                else:
                    print("La cantidad ingresada no es valida")
                    print("Presione enter para volver a ingresar la cantidad")
                    input()
                    return realizarCompra(codigo=(input("Ingrese el codigo del producto: ")))
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
                        print("2. No, eliminarlo del carrito")
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
                                return realizarCompra(codigo=(input("Ingrese el codigo del producto: ")))
                            elif opcion == 2:
                                print("Desea eliminar el producto del carrito?")
                                print("1. Si")
                                print("2. No")
                                opcion = input("Ingrese una opcion: ")
                                if opcion.isnumeric():
                                    producto3.stock = producto3.stock + cantidad
                                    opcion = int(opcion)
                                    if opcion == 1:
                                        carrito.pop(producto3.nombre)
                                        print("Los productos comprados son: ")
                                        print(carrito)
                                        print("Presione enter para volver al menu realizar compra")
                                        input()
                                        return realizarCompra(codigo=(input("Ingrese el codigo del producto que quiere comprar: ")))
                                    elif opcion == 2:
                                        print("Presione enter para volver al menu realizar compra")
                                        return menuPrincipal()
                                    else:
                                        print("Opción incorrecta")
                                        print("Ingrese una opción valida del 1 al 2")
                                        return realizarCompra(codigo=(input("Ingrese el codigo del producto que quiere comprar: ")))
                                else: 
                                    return realizarCompra(codigo=(input("Ingrese el codigo del producto que quiere comprar: ")))    
                            else:
                                print("Opción incorrecta")
                                print("Ingrese una opción valida del 1 al 2")
                                return realizarCompra(codigo=(input("Ingrese el codigo del producto que quiere comprar: ")))
                    else:
                        print("La cantidad ingresada no se encuentra disponible")
                        print("Presione enter para volver a ingresar la cantidad")
                        input()
                        return realizarCompra(codigo=(input("Ingrese el codigo del producto que quiere comprar: ")))
                else:
                    print("La cantidad ingresada no es valida")
                    print("Presione enter para volver a ingresar la cantidad")
                    input()
                    return realizarCompra(codigo=(input("Ingrese el codigo del producto que quiere comprar: ")))
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
                                return realizarCompra(codigo=(input("Ingrese el codigo del producto que quiere comprar: ")))
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
                                        return realizarCompra(codigo=(input("Ingrese el codigo del producto que quiere comprar: ")))
                                    elif opcion == 2:
                                        print("Presione enter para volver al menu realizar compra")
                                        return menuPrincipal()
                                    else:
                                        print("Opción incorrecta")
                                        print("Ingrese una opción valida del 1 al 2")
                                        return realizarCompra(codigo=(input("Ingrese el codigo del producto: ")))
                                else: return realizarCompra(codigo=(input("Ingrese el codigo del producto que quiere comprar: ")))    
                            else:
                                print("Opción incorrecta")
                                print("Ingrese una opción valida del 1 al 2")
                                return realizarCompra()
                    else:
                        print("La cantidad ingresada no se encuentra disponible")
                        print("Presione enter para volver a ingresar la cantidad")
                        input()
                        return realizarCompra()
                else:
                    print("La cantidad ingresada no es valida")
                    print("Presione enter para volver a ingresar la cantidad")
                    input()
                    return realizarCompra()
        else:
            print("El código ingresado no es valido")
            print("Presione enter para volver a ingresar el codigo")
            input()        
            return realizarCompra()       
    else:
        print("El código ingresado no es valido")
        print("Presione enter para volver a ingresar el codigo")
        input()        
        return realizarCompra()    
        
    





#def realizarCompra():

#def finalizarCompra():
