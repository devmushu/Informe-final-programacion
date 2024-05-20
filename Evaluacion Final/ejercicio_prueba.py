from funciones import *

clientes = {} #====> lista vacia
usuarios = {}  #====> lista vacia x2
idcliente = 0 #=====> contador id cliente
idusuario = 0 #=====> Contador idusuario


while True: #===========> creamos el while del menu y lo mostramos llamando funciones
    menuUsuarios()
    opUsu = int(input("INGRESE OPCIÓN: "))  #=========> Seleccion de opcion

    if opUsu == 1:  #============> opcion 1 iniciar sesion
        user = input("Ingrese nombre de usuario: ")
        clave = input("Ingrese password: ")
        if usuarios.get(user):
            usuario = usuarios.get(user)
            if usuario[2] == clave:
                print(f"Bienvenido {usuario[3]} {usuario[4]} - {usuario[2]} - id: {usuario[0]}.")
                input("Presiona ENTRAR para ingresar al Menú Principal.")
                while True:  # Bucle para el Menú Principal
                    menuprincipal()
                    op = int(input("INGRESE OPCIÓN: "))
                    if op == 1:
                        ingresardatos()
                    elif op == 2:
                        mostrar()
                    elif op == 3:
                        modificardatos()
                    elif op == 4:
                        eliminardatos()
                    elif op == 5:
                        opSalir = input("¿DESEA SALIR [SI/NO]: ")
                        if opSalir.lower() == "si":
                            break  # Salir del bucle del Menú Principal
                    else:
                        print("Opción Fuera de Rango")
                break  # Salir del bucle del Menú de Usuarios
            else:
                input("Contraseña incorrecta. Presiona ENTER para volver al Menú de Usuarios.")
        else:
            input("Usuario no registrado. Presiona ENTER para volver al Menú de Usuarios.")
    elif opUsu == 2: #=================> opcion crear usuario
        ingresoUsuarios()
    elif opUsu == 3: #================> opcion salir
        opSalir = input("¿DESEA SALIR [SI/NO]: ")
        if opSalir.lower() == "si":
            break
    else: #====================> seleccion fuera de rango
        print("Opción Fuera de Rango")
