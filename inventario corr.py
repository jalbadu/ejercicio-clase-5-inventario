lista_articulos = []

def menu():
    print("Bienvenido\n")
    print("\t1. Ver productos")
    print("\t2. Agregar productos")
    print("\t3. Modificar inventario")
    print("\t4. Dar de baja productos")
    print("\t5. Salir")
    try:
        opcion = int(input("\nEscoja una opción del Menú... "))
        if opcion in [1, 2, 3, 4, 5]:
            return opcion
        else:
            print("Opción inválida.\n")
            return None
    except ValueError:
        print("Debe ingresar un número.\n")
        return None

def ver_articulos():
    if not lista_articulos:
        print("El inventario está vacío.\n")
    else:
        print("\nArtículos en inventario:")
        for art, cant, prec in lista_articulos:
            print(f"- {art} : {cant} unidades a ${prec:.2f} cada una")
        print()

def agregar_articulo():
    while True:
        articulo = input("Escriba el artículo: ")
        cantidad = int(input("Escriba la cantidad: "))
        precio = float(input("Escriba el precio: "))

        lista_articulos.append([articulo, cantidad, precio])

        continuar = input("¿Desea agregar otro artículo? (s/n): ").strip().lower()
        if continuar != 's':
            break

def modificar_inventario():
    buscar = input("Digite el nombre del artículo que desea modificar: ").strip().lower()
    encontrado = False

    for item in lista_articulos:
        if item[0].strip().lower() == buscar:
            print(f"Artículo encontrado: {item[0]} - Cantidad: {item[1]}, Precio: ${item[2]:,.2f}")
            accion = input("¿Desea agregar (A) o quitar (Q) unidades?: ").strip().upper()
            if accion == "A":
                unidades = int(input("¿Cuántas unidades desea agregar?: "))
                item[1] += unidades
                print("Unidades agregadas.\n")
            elif accion == "Q":
                unidades = int(input("¿Cuántas unidades desea quitar?: "))
                if unidades <= item[1]:
                    item[1] -= unidades
                    print("Unidades retiradas.\n")
                else:
                    print("No hay suficientes unidades para quitar.\n")
            else:
                print("Opción inválida.\n")
            encontrado = True
            break

    if not encontrado:
        print("Artículo no encontrado.\n")

# Bucle principal
while True:
    opcion = menu()
    if opcion == 1:
        ver_articulos()
    elif opcion == 2:
        agregar_articulo()
    elif opcion == 3:
        modificar_inventario()
    elif opcion == 4:
        print("Función para dar de baja aún no implementada.\n")  # Puedes agregarla si deseas
    elif opcion == 5:
        print("Gracias por usar el sistema. Hasta luego.")
        break
