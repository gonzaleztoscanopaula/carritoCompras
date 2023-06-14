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
        return f"El producto código: {self.codigo} = {self.nombre} de la marca {self.marca} tiene un precio de {self.precio} pesos, hay {self.stock} unidades disponibles, es de color {self.color} y sus caracteristicas son {self.caracteristicas}"
    def detalleBreve(self):
        return f"El producto código: {self.codigo} = {self.nombre} tiene un precio de {self.precio} pesos, hay {self.stock} unidades disponibles"
    def productosDisponibles(self):
        return f"Producto código: {self.codigo} = Nombre: {self.nombre} - Marca:{self.marca} - Precio:{self.precio} - Stock:{self.stock}"
    def buscarProductoPorCodigo(self):
        return f"El producto código: {self.codigo} = {self.nombre} de la marca {self.marca} tiene un precio de {self.precio} pesos, hay {self.stock} unidades disponibles, es de color {self.color} y sus caracteristicas son {self.caracteristicas}"
    

producto1 = Productos(1, "zapatillas", "new balance", 23000, 7, "negro", "zapatillas negras con inscripcion en blanco, todos los talles")
producto2= Productos(2, "zapatillas", "adidas", 45000, 3, "Verdes", "Zapatillas verdes con suela roja, todos los talles")
producto3= Productos(3, "zapatillas", "puma", 32000, 5, "blanco", "Zapatillas blancas con cordones celestes, todos los talles") 
producto4= Productos(4, "ojotas", "new balance", 15000, 9, "azul", "Ojotas azules, con lineas blancas, todos los talles")   

print(producto1.detalleCompleto()) 
print(producto1.detalleBreve())   





def menuPrincipal():
    print("1. Mostrar productos en detalles")
    print("2. Mostrar informacón breve del producto")
    print("3. Buscar producto por código")
    print("4. Realizar compra")
    print("5. Finalizar compra")
    print("6. Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def mostrarProductosEnDetalle():
    print(producto1.detalleCompleto())
    print(producto2.detalleCompleto())
    print(producto3.detalleCompleto())
    print(producto4.detalleCompleto())

def mostrarProductosBreve():
    print(producto1.detalleBreve())
    print(producto2.detalleBreve())
    print(producto3.detalleBreve())
    print(producto4.detalleBreve())

def productosDispo():
    print(producto1.productosDisponibles())
    print(producto2.productosDisponibles())
    print(producto3.productosDisponibles())
    print(producto4.productosDisponibles())

def buscarProductoPorCodigo(codigo):
    if codigo == 1:
        print(producto1.detalleBreve())
    elif codigo == 2:
        print(producto2.detalleBreve())
    elif codigo == 3:
        print(producto3.detalleBreve())
    elif codigo == 4:
        print(producto4.detalleBreve())
    else:
        print("El código ingresado no existe")

def realizarCompra():
