#Servidor para exponenciar dos datos

import socket 
import marshal

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5008

ss.bind((host,port))
print("Servidor de potencia")
ss.listen()

while True:
    cs,addr = ss.accept()#acepta la conexion del dhcp
    print("Conexion lista con", str(addr))
    datos = cs.recv(1024)#4Recibe datos y procesa
    deserializa = marshal.loads(datos)
    print("Datos recibidos", deserializa)
    #hacer ciclo para sumar losvalores y enviar los resultados al clineete
    pot = 0
    x1 = int(deserializa[0])#número 1
    x2 = int(deserializa[1])#número 2
    pot = pow(x1, x2)   
    cs.send(str(pot).encode("ascii"))#5Envia datos procesados
    cs.close()#5.1 cierra el la conexión con el dhcp
ss.close()
