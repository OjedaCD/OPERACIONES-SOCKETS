#cliente que presenta un menu

import socket
import marshal
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Se pone el ipv4 y UDP
host = socket.gethostname() #se obtine la direccion del socket
port = 5002# se estrablece el puerto de comuniación
ss.connect((host, port))# se conecta con el dhcp
datos = []# se crea un array para almacenar los datos

while True:
    
    print("\n[1] sumar")
    print("[2] restar")
    print("[3] multiplicar")
    print("[4] dividir")
    print("[5] módulo")
    print("[6] potencia")
    print("[7] salir")
    aux1 = int(input("Elige una opciion de [1-7]"))

    if aux1 == 7:
        print("Good bye :)")
        break
    else:
        print("\n")
        if aux1 == 1:
            print("SUMA")
        if aux1 == 2:
            print("RESTA")
        if aux1 == 3:
           print("MULTIPLICACIÓN")
        if aux1 == 4:
            print("DIVISIÓN")
        if aux1 == 5:
            print("MÓDULO")
        if aux1 == 6:
            print("POTENCIA")
        datos.append(aux1)
        x1 = input("Ingrese el primer numero: ")
        datos.append(x1)#append agrega un elemento al array de la lista
        x2 = input("Ingrese el segundo numero: ")
        datos.append(x2)
    
        serealizar = marshal.dumps(datos)#se codifica en codigo binario dentro den un fichero
        ss.send(serealizar)#1 Envia peticion 
        datos.clear()#limpia array
        aux1 = 0
    
    msg = ss.recv(1024)#8recibe el resultado
    print("\nEl resultado de la operación es {}".format(msg.decode("ascii")))#8recibe datos porcesados
ss.close()
    



    

