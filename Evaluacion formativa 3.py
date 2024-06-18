"""
reparto de gas
registrar pedidos
la empresa vende gas de 5,15,45 kilos
"""

import Funciones as fn

pedidos = []
menu = 0

while menu == 0:
    print("Bienvenido a menu principal \n")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")
    menu = int(input("Favor escoga una opcion: "))

    while menu == 1:
        fn.registrar_pedido(pedidos)
        menu = 0


    while menu == 2:
        fn.listar_pedido(pedidos)
        menu = 0


    while menu == 3:
        fn.imprimir_hoja_ruta(pedidos)
        menu = 0

    while menu == 4:
        print("Usted ha salido del sistema")
        break
