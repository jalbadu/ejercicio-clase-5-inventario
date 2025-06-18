lista_articulos = []




def menu():
    
        print("Bienvenido\n")
        print("\t 1.  Ver productos")
        print("\t 2.  Agregar productos")
        print("\t 3.  Modificar inventario")
        print("\t 4.  Dar de baja productos")
        print("\t 5.  Salir")
        opcion = int(input("\n Escoja una opción del Menú... "))
        if  opcion ==1 or opcion ==2 or opcion ==3 or opcion==4 or opcion ==5:
                return opcion
        else:
            print("Opción inválida. Intente nuevamente.\n")
        







    
def ver_articulos():
    '''if len(lista_articulos) == 0:
        print("El inventario está vacío")
    else:
        print("hay artículos")
   '''

1
def agregar_articulo():
    while True:
        articulo = input("Escriba el artículo: ")
        cantidad = int(input("Escriba la cantidad: "))
        precio = float(input("Escriba el precio: "))

        # Agregar como tupla a la lista
        lista_articulos.append((articulo, cantidad, precio))

        continuar = input("¿Desea agregar otro artículo? (s/n): ").strip().upper()
        if continuar != 'S':
            break

    print("\n Artículos registrados:")
    for art, cant, prec in lista_articulos:
        print(f"-*- {art}        {cant} unidades a ${prec:.2f} de la unidad")
        print(lista_articulos)


def modificar_inventario():
    articulo= input("Escribir el artículo:  ")
    num_articulo= input("Escribir el número:  ")
    opcion_inventario = int(input("Que desea hacer: Agregar (A) o Quitar artículos (E) ?"))
    buscar = input("Digite el nombre del artículo que desea buscar: ")

    encontrado = False
    for elemento in lista_articulos:
        if elemento[0] == buscar:
            print(f"Artículo encontrado: {elemento[0]} - Cantidad: {elemento[1]}, Precio: ${elemento[2]:,.0f}")
            encontrado = True
            break

        if not encontrado:
            print("Artículo no encontrado.")
                

#recoger la escogencia del usuario en el menu y ejecutar opciones
opcion = menu()

while True:
    
    if opcion ==1:
        ver_articulos()
    if opcion ==2:
        agregar_articulo()
    if opcion ==3:
        modificar_inventario()
    if opcion ==5:
        break
