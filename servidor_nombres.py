#Servidor para enviar y recibir varios datos

import socket 
import marshal

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5002
ss.bind((host,port))#recibe un cliente
print("Servidor de nombres activado")
ss.listen()


while True:
    cs,addr = ss.accept()#acepta la conexión y recibe el socket y la dirección del cliente 
    print("Conexion lista con", str(addr))
    datos = cs.recv(1024)#Recibe peticion y valida
    deserializa = marshal.loads(datos)#los desencripta
    print("Datos recibidos", deserializa)
    opc = int(deserializa[0])#lo convierte a entero
    x1 = int(deserializa[1])#número 1
    x2 = int(deserializa[2])#número 2

    
    if opc == 1:
        print("SUMA")
        datos = []# se crea un array para almacenar los datos
        ss1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Se pone el ipv4 y UDP
        host = socket.gethostname() #se obtine la direccion del socket
        ss1.connect((host, 5003))# se conecta con el dhcp
        datos.append(x1)
        datos.append(x2)
        serealizar = marshal.dumps(datos)#se codifica en codigo binario dentro den un fichero
        ss1.send(serealizar)#3 Envia datos apra procesar
        datos.clear()#limpia array
        msg = ss1.recv(1024)#6 Recibe datos procesados
        ss1.close()
    if opc == 2:
        print("RESTA")
        datos = []# se crea un array para almacenar los datos
        ss2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Se pone el ipv4 y UDP
        host = socket.gethostname() #se obtine la direccion del socket
        ss2.connect((host, 5004))# se conecta con el dhcp
        datos.append(x1)
        datos.append(x2)
        serealizar = marshal.dumps(datos)#se codifica en codigo binario dentro den un fichero
        ss2.send(serealizar)#3 Envia datos apra procesar
        datos.clear()#limpia array
        msg = ss2.recv(1024)#6 Recibe datos procesados
        ss2.close()
    if opc == 3:
        print("MULTIPLICACIÓN")
        datos = []# se crea un array para almacenar los datos
        ss3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Se pone el ipv4 y UDP
        host = socket.gethostname() #se obtine la direccion del socket
        ss3.connect((host, 5005))# se conecta con el dhcp
        datos.append(x1)
        datos.append(x2)
        serealizar = marshal.dumps(datos)#se codifica en codigo binario dentro den un fichero
        ss3.send(serealizar)#3 Envia datos apra procesar
        datos.clear()#limpia array
        msg = ss3.recv(1024)#6 Recibe datos procesados
        ss3.close()
    if opc == 4:
        print("DIVISIÓN")
        datos = []# se crea un array para almacenar los datos
        ss4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Se pone el ipv4 y UDP
        host = socket.gethostname() #se obtine la direccion del socket
        ss4.connect((host, 5006))# se conecta con el dhcp
        datos.append(x1)
        datos.append(x2)
        serealizar = marshal.dumps(datos)#se codifica en codigo binario dentro den un fichero
        ss4.send(serealizar)#3 Envia datos apra procesar
        datos.clear()#limpia array
        msg = ss4.recv(1024)#6 Recibe datos procesados
        ss4.close()
    if opc == 5:
        print("MÓDULO")
        datos = []# se crea un array para almacenar los datos
        ss5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Se pone el ipv4 y UDP
        host = socket.gethostname() #se obtine la direccion del socket
        ss5.connect((host, 5007))# se conecta con el dhcp
        datos.append(x1)
        datos.append(x2)
        serealizar = marshal.dumps(datos)#se codifica en codigo binario dentro den un fichero
        ss5.send(serealizar)#3 Envia datos apra procesar
        datos.clear()#limpia array
        msg = ss5.recv(1024)#6 Recibe datos procesados
        ss5.close()
    if opc == 6:
        print("POTENCIA")
        datos = []# se crea un array para almacenar los datos
        ss6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Se pone el ipv4 y UDP
        host = socket.gethostname() #se obtine la direccion del socket
        ss6.connect((host, 5008))# se conecta con el dhcp
        datos.append(x1)
        datos.append(x2)
        serealizar = marshal.dumps(datos)#se codifica en codigo binario dentro den un fichero
        ss6.send(serealizar)#3 Envia datos apra procesar
        datos.clear()#limpia array
        msg = ss6.recv(1024)#6 Recibe datos procesados
        ss6.close()


    cs.send(str(msg).encode("ascii"))#7Envá los datos procesados 
    cs.close()
ss.close()
        

