sector = ["norte","centro","sur"]
pedidos = []

def registrar_pedido(pedidos):
    gas_5 = 0
    gas_15 = 0
    gas_45 = 0
    opc_gas = 1
    while True:
        print("Usted ha escogido registrar un pedido")
        #registro cliente
        nombre = input("Por favor ingrese nombre y apellido: ")
        lugar = input("Por favor ingrese su direccion de domicilio: ")
        comuna = input("Por favor ingrese su sector (norte,centro,sur): ")
        if comuna not in sector:
            print("Favor seleccione un sector valido (norte,centro,sur)")
            comuna = input("Por favor ingrese su sector (norte,centro,sur): ")
            #pedido_gas = 1
        #pedido de gas
        while opc_gas == 1: 
            print("1. Cilindro 5KG")
            print("2. Cilindro 15KG")
            print("3. Cilindro 45KG")
            selec_gas = int(input("Por favor escoga el tipo de gas que desee: "))
            if selec_gas == 1:
                gas_5 = gas_5 + 1
            if selec_gas == 2:
                gas_15 = gas_15 + 1
            if selec_gas == 3:
                gas_45 = gas_45 + 1
            opc_gas = input("Desea agregar otro gas? (si/no)").lower
            if opc_gas == "si":
                selec_gas = int(input("Por favor escoga el tipo de gas que desee: "))
            else:
                break
           


        pedidos.append({
            "Cliente" : nombre,
            "Direccion" : lugar,
            "Sector" : comuna,
            "Cil 5kg": gas_5,
            "Cil 15kg": gas_15,
            "Cil 45kg": gas_45
        })
        print("Compra ha sido registrada!! \n")
        return(pedidos)       



def listar_pedido(pedidos):
    print("Usted ha escogido listar todos los pedidos")
    print(pedidos)


def imprimir_hoja_ruta(pedidos):
    print("Usted ha escogido imprimir la hoja de ruta")
    print("1. Sector Norte")
    print("2. Sector Centro")
    print("3. Sector Sur")
    opc_hoja_ruta = int(input("Seleccione algun sector: "))
    
    #if opc_hoja_ruta == 1:
     #   with open("Sector norte.txt","w") as archivo1:
      #  contenido = pedidos[""]