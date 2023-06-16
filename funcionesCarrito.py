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
    
producto1 = Productos(1, "zapatillas", "new balance", 23000, 7, "negro", "zapatillas negras con inscripcion en blanco, todos los talles")
producto2= Productos(2, "zapatillas", "adidas", 45000, 3, "Verdes", "Zapatillas verdes con suela roja, todos los talles")
producto3= Productos(3, "zapatillas", "puma", 32000, 5, "blanco", "Zapatillas blancas con cordones celestes, todos los talles") 
producto4= Productos(4, "ojotas", "new balance", 15000, 9, "azul", "Ojotas azules, con lineas blancas, todos los talles")   
 
#funcion para Mostrar el menu principal
def menuPrincipal():
    print("1. Mostrar productos en detalles")
    print("2. Mostrar informacón breve del producto")
    print("3. Buscar producto por código")
    print("4. Realizar compra")
    print("5. Finalizar compra")
    print("6. Salir")



#funcion para mostrar productos en detalles
def mostrarProductosEnDetalle():
    print(producto1.detalleCompleto())
    print(producto2.detalleCompleto())
    print(producto3.detalleCompleto())
    print(producto4.detalleCompleto())

#funcion para mostrar productos con detalle breve
def mostrarProductosBreve():
    print(producto1.detalleBreve())
    print(producto2.detalleBreve())
    print(producto3.detalleBreve())
    print(producto4.detalleBreve())



#funcion para buscar los productos por codigo
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
                        return validarOpciones()
                    else:
                        print("Opción incorrecta")
                        print("Ingrese una opción valida del 1 al 2")
                        return buscarProductoPorCodigo()
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
                        menuPrincipal()
                        return funcionMenu(opcion=(input("Ingrese una opcion: ")))
                    else:
                        print("Opción incorrecta")
                        print("Ingrese una opción valida del 1 al 2")
                        return buscarProductoPorCodigo()                
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
                        return funcionMenu(opcion=(input("Ingrese una opcion: ")))
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
                        return funcionMenu(opcion=(input("Ingrese una opcion: ")))
                    else:
                        print("Opción incorrecta")
                        print("Ingrese una opción valida del 1 al 2")
                        return buscarProductoPorCodigo()                
        else:
            print("El código ingresado no se encuentra disponible")
    else:
        print("El código ingresado no es valido")
        return buscarProductoPorCodigo()

#funcion para validar opciones ingresados en el menu principal
def validarOpciones():
    opcion = input("Ingrese una opcion: ")   
    if opcion.isnumeric():
        opcion = int(opcion)
        if opcion >= 1 and opcion <= 6:
            funcionMenu(opcion)     
    else:
        print("Opción incorrecta")
        print("Ingrese una opción valida del 1 al 6")
        return validarOpciones()
        
def funcionMenu(opcion):
    while opcion != 6:
                if opcion == 1:
                    mostrarProductosBreve()
                    print("-------------------------Mostrar productos en detalle-------------------------")
                    return mostrarProductosEnDetalle()
                elif opcion == 2:
                    print("-------------------------Mostrar informacion breve-------------------------")
                    return mostrarProductosBreve()
                elif opcion == 3:
                    mostrarProductosBreve()
                    print("-------------------------Buscar producto por codigo-------------------------")
                    return buscarProductoPorCodigo(codigo=(input("Ingrese el codigo del producto: ")))
                    print(buscarProductoPorCodigo(codigo))
                elif opcion == 4:
                    print("-------------------------Realizar compra-------------------------")
                    #realizarCompra()
                else:
                     print("-------------------------Finalizar compra-------------------------")
                     #finalizarCompra()


#def realizarCompra():

#def finalizarCompra():
