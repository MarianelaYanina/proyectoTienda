#MENU PRINCIPAL

productos=[] #lista que almacena los productos que almacenemos

while True: #para q el bucle no pare
    #ENTRADA:MENU DE OPCIONES
    print("menu para la gestion de productos: \n")
    print("1.Registro: Alta de productos nuevos.")
    print("2.Visualizacion: Consulta de datos de productos.")
    print("3.Actualizacion: Modificar la cantidad en stock de un producto.")
    print("4.Eliminacion: Dar de baja productos.")
    print("5.Listado: Listado completo de los productos en la base de datos.")
    print("6.Reporte de bajo stock: Lista de productos con cantidad minimo bajo.")
    print("7.SALIR")
    
    try:
        #SOLICITUD DE OPCION (PROCESO)
        opcion=int(input("seleccione una opcion entre 1 y 7: "))

#OPCION 1:

        if opcion == 1:
            print("Ud. ah seleccionado la opcion 1: Registro.") 

            #PETICION DEL NOMBRE DEL PRODUCTO:
            while True: #hacemos otro bucle para q si hay un ingreso invalido, no tenga q ingresar de nuevo al menu principal
                nombre=input("ingrese el nombre del producto: ")
                
                #PETICION DEL PRECIO DEL PRODUCTO:
                while True:
                    try:
                        precio=float(input("ingrese el precio del producto: $"))
                        if precio<=0:
                            print("por favor ingrese un valor mayor a cero.")
                        else:
                            break
                    except ValueError:#por si ingresa una letra
                        print("por favor ingrese un valor numerico.")

                #PETICION DE STOCK DEL PRODUCTO:
                while True:#si ya se cargo el nombre me lo habilita
                    try: #posible error
                        stock=float(input("ingrese el stock del producto: "))
                        if stock<=0:#por si el error es numerico
                            print("el stock debe ser mayor a cero.")
                        else:
                            break
                    except ValueError:
                        print("el stock debe ser un numero.") 

            #DEBEMOS CARGAR TODOS LOS DATOS EN LA LISTA:
                producto=[nombre, precio, stock]
                productos.append(producto)
                print("producto cargado con exito.")

                agregar_mas=input("desea agregar mas productos? (S para si N para no): ")
                if agregar_mas.lower() != "s":
                    break

#OPCION 2: 

        elif opcion == 2:
            print("Ud. ah seleccionado la opcion 2: Visualizacion.")
            ver=input("ingrese el nombre del producto que desea visualizar: ")
            for producto in productos:
                if producto[0] == ver:
                    print(f"el producto {producto[0]}, vale $ {producto[1]} y tenes {producto[2]} disponibles.")  
                    break
                else:
                    print("producto no encontrado, reintente")

#OPCION 3: 

        elif opcion == 3:
            print("Ud. ah seleccionado la opcion 3: Actualizacion.")
            #PRIMERO NECESITO SABER SOBRE QUE PRODUCTO SE VA A HACER LA ACTUALIZACION
            vendido=input("ingrese el nombre del producto que desea actualizar: ")
            for producto in productos:
                if producto[0] != vendido:
                    print("producto no encontrado, reintente.")
                elif producto[0] == vendido:
                    #SOLICITUD DE CANTIDAD VENDIDA Y ACTUALIZACION DE STOCK
                    while True:
                        try: 
                            cantidad_vendida=int(input(f"ingrese la cantidad vendida de {producto[0]}:  "))
                            if cantidad_vendida <= 0:
                                print("por favor ingrese un valor mayor a cero.")
                            elif cantidad_vendida > producto[2]:
                                print("no hay stock suficiente para esta cantidad, intente con un valor menor.")
                            else: #actualizacion de stock
                                producto[2]-=cantidad_vendida
                                print(f"stock actualizado: nueva cantidad en stock de {producto[0]}: {producto[2]}")
                                print("producto actualizado con exito.")
                            eliminar_mas=input("desea actualizar mas productos? (S para si N para no): ")
                            if eliminar_mas.lower() != "s":
                                break 
                        except ValueError:
                            print("por favor ingrese un numero valido.")                      

#OPCION 4:

        elif opcion == 4:
            print("Ud. ah seleccionado la opcion 4: Eliminacion.")
            eliminar=input("ingrese el nombre del producto a eliminar: ")
            for producto in productos:
                if producto[0] == eliminar:
                    productos.remove(producto)
                    print("producto eliminado con exito.")
                    eliminar_mas=input("desea eliminar mas productos? (S para si N para no): ")
                    if eliminar_mas.lower() != "s":
                        break
                

#OPCION 5:

        elif opcion == 5:
            print("Ud. ah seleccionado la opcion 5: Listado.")
            print("\t Listado de Productos Vigentes : \n")
            for articulo in productos:
                print(f"nombre del pord: {articulo[0]} - precio: {articulo[1]} - stock: {articulo[2]}")

#OPCION 6:        
        
        elif opcion == 6:
            print("Ud. ah seleccionado la opcion 6: Reporte Bajo Stock.")
            for articulo in productos:
                if articulo[2] <=5:
                    print(f"tenes en stock {articulo[2]} de {articulo[0]}, reponer urgente.")
                elif articulo[2] <=20:
                    print(f"tenes en stock {articulo[2]} de {articulo[0]}, recomiendo reponer.")
                else:
                    print(f"tenes en stock {articulo[2]} de {articulo[0]}, no hace falta reponer.")

#OPCION 7:

        elif opcion == 7:
            print("Ud. ah seleccionado la opcion 7: Salir.") 
            break 

#POSIBLE ERROR NUMERICO EN LA ENTRADA DEL MENU:

        else: 
            print("opcion no valida, elija entre 1 y 7.")      
    
#POSIBLE ERROR EN LA ENTRADA DE UN STR EN EL MENU:    
    
    except ValueError:
        print("entrada invalida, por favor ingrese un valor numerico del 1 al 7: ")

#NO PUDE HACER QUE SE EJECUTE CORRECTAMENTE LA OPCION 3.
#REALIZE ALGUNAS OPCIONES MAS APARTE DE LAS SOLICITADAS AUNQUE ME PARECEN BASICAS (YA QUE EN TODAS HAY POSIBLES ERRORES) PERO ES UN TEMA QUE DEBO PRACTICAR MAS.