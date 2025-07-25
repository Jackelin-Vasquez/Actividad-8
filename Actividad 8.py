productos=[]

while True:
    print("1.Agregar producto a lista:")
    print("2.Modificar un producto existente:")
    print("3.Eliminar un producto")
    print("4.Ver todos lo productos:")
    print("5.Salir del programa")

    opcion = input("Ingrese una opcion:")

    match opcion:

        case "1":
            agregar_producto= input("Escriba producto a agrgar:")
            productos.append(agregar_producto)
            print("Producto agregado:")
        case "2":
            print(productos)
            producto_modificado= int(input("Ingrese indice de producto a modificar:"))
            nuevo= input("INgrese nuevo producto:")
            productos[producto_modificado] = nuevo
            print(f"Producto modificado\n Nueva lista{productos}")
        case "3":
            print(productos)
            eliminar_producto= input("Ingrese producto a eliminar:").lower()
            if eliminar_producto in productos:
                productos.remove(eliminar_producto)
                print(f"{eliminar_producto} eliminado exitosamente")
            else:
                print("Producto  no encontrado")
        case "4":
            print(f"PRODUCTOS:")
            for i in productos:
                print(i)
        case "5":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no disponible ")