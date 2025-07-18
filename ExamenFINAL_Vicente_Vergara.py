#EXAMEN FINAL PROGRAMACION

productos = {'8475HD': ['HP',15.6,'8GB','DD','1T','Intel Core i5','Nvidia GTX1050'],
             '2175HD': ['Acer',14,'4GB','SSD','512GB','Intel Core i5','Nvidia GTX1050'],
             'JjfFHD': ['Asus',14,'16GB','SSD','256GB','Intel Core i7','Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP',15.6,'12GB','DD','1T','Intel Core i3','Integrada'],
             'GF75HD': ['Asus',15.6,'12GB','DD','1TB','Intel Core i7','Nvidia GTX1050'],
             '123FHD': ['Acer',14,'6GB','DD','1T','AMD Ryzen 5','Integrada'],
             '342FHD': ['Acer',15.6,'8GB','DD','1T','AMD Ryzen 7','Nvidia GTX1050'],
             'UWU131HD': ['Dell',15.6,'8GB','DD','1T','AMD Ryzen 3','Nvidia GTX1050']}

stock = {'8475HD': [387990,10],'2175HD': [327990,4],'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21], '123FHD': [290890,32],'342FHD': [444990,7],
         'GF75HD': [749990,2], 'UWU131HD': [349990,1],'FS1230HD': [249990,0]}

def stock_marca():
    buscar_stock = input("Ingresa la marca para saber el stock:")
    encontrado = False
    for producto in stock:
        if buscar_stock == stock:
            print(f"En stock hay {producto[1]}")
            encontrado = True
            
    if not encontrado:
        print("Producto no encontrado")
        
def busqueda_precio():
    try:
        p_min = int(input("Ingrese el precio minimo:"))
        p_max = int(input("Ingrese precio maximo:"))
    except ValueError:
        print("Ingresar solo valores enteros!!!!")
        return
    encontrado = False
    for stocks in stock:
        if p_min >= stock and p_max <= stock:
            print(f"El precio se relaciona con {productos}")
            encontrado = True
    if not encontrado:
        print("No se encontro un producto relacionado al precio colocado")
        
def eliminar():
    buscar_eliminar = input("Ingrese el modelo a eliminar:")
    encontrado = False
    for producto in productos:
        if buscar_eliminar == producto:
            producto.remove(buscar_eliminar)
            print("Producto eliminado con exito")
            encontrado = True
            otro = input("Desea eliminar otro producto?(S/N):")
            if otro == "S":
                continue
            else:
                return
            
    if not encontrado:
        print("Producto no encontrado")
        
def menu():
    while True:
        print("=====MENU PRINCIPAL=====")
        print("1. Stock marca")
        print("2. Busqueda por precio")
        print("3. Eliminar Producto")
        print("4. Salir")
        try:
            op = int(input("Ingresa una opcion:"))
        except ValueError:
            print("Solo numeros enteros!!!")
            continue
        
        if op == 1:
            stock_marca()
        
        elif op == 2:
            busqueda_precio()
            
        elif op == 3:
            eliminar()
            
        elif op == 4:
            print("Saliendo. . .")
            break
        
        else:
            print("Opcion invalida")
            
menu()