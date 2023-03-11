def Validar_Usuario():

    Validar_Tarjeta=input("Ingrese Los 16 Digitos De Su Tarjeta :")
    Nick=input("Digite Su NICK :")
    if (Validar_Tarjeta=="1111111111111111" and Nick=="1234"): #PRIMERA CUENTA
        print("***********************")
        print("   BIENVENIDO ALAIN    ")
        print("***********************")

        opcion=1
        while (opcion!=2): #SI CUMPLE LA CONDICION SE HACE UN SUBMENU PARA REALIZAR OPERACIONES
            print ('''*********MENU DE OPERACIONES ATM...CLIENTE ALAIN**********\n''')
            print ('Selecciona la Opcion que deseas?\n')
            print ('1.- Realizar Un Deposito')
            print ('2.- Salir\n')
            print ('************************************************************')

            opcion=int(input('Seleciona la Opcion que deseas:'))

            if (opcion==1):
                print("-------REALIZA UN DEPOSITO :-------\n")
                deposito=0
                print("USTED CUENTA CON UN SALDO DE :",deposito)
                deposito=int(input("Ã‚Â¿Cuanto Deposita?"))
                print("Tiene En Proceso Un Deposito Una Cantidad De $",deposito)
                print("\nAcontinuacion Debera Validar Su NÃ‚Âº De Cuenta, Para Realizar El Deposito")
                Validar_Tarjeta=input("Digite Los 16 Numero De La Cuenta:")
                if (Validar_Tarjeta=="1111111111111111"):
                    print("\nUsted Ha Realizado Un Deposito De $",deposito)
                    print("NUEVO SALDO $",deposito)

                else:
                    print("\nPARA PODER REALIZAR EL DEPOSITO, INGRESE CORRECTAMENTE LOS 16 DIGITOS")
                    break
            elif(opcion==2):
                print("Finalizando...Cerrando Aplicacion")
            break
        else:
            print("Ese numero de Opcion no existe.. Intente de nuevo")
    else:
        print("LO SENTIMOS...ASEGURESE QUE LOS DATOS SEAN CORRECTOS")#termino de la primera cuenta

    #elif (Validar_Tarjeta=="1020304050607080" and Nick=="1990"): #SEGUNDA CUENTA
     #   print("*******************************")
      #  print("     BIENVENIDO PROGRAMADOR    ")
      #  print("*******************************")





def Retirar_Tarjeta():
    print("")

def Retirar_Monto():
    print("saldo",deposito)
def Menu():
    opcion=1
    while (opcion!=4):
        print ('''*********ATM SIMULACION BANCARIO*************\n''')
        print ('Selecciona la Opcion que deseas?\n')
        print ('1.- INGRESAR ATM/OPERAR  ')
        print ('2.- Retirar Monto')
        print ('3.- Consultar Saldo')
        print ('3.- RETIRAR TARJETA')
        print ('4.- SALIR \n')
        print ('************************************************')

        opcion=int(input('Seleciona la Opcion que deseas:'))

        if (opcion==1):
            Validar_Usuario()

        elif (opcion==2):
            Retirar_Monto()
        elif (opcion==3):
            Retirar_Tarjeta()
        elif(opcion==4):
            print("Finalizando...Cerrando Aplicacion")
            break
        else:
            print("Ese numero de Opcion no existe.. Intente de nuevo")

Menu()