#Servidor para sumar dos datos

import socket 
import marshal

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5003

ss.bind((host,port))
print("Servidor suma")
ss.listen()

while True:
    cs,addr = ss.accept()#acepta la conexion del dhcp
    print("Conexion lista con", str(addr))
    datos = cs.recv(1024)#4Recibe datos y procesa
    deserializa = marshal.loads(datos)
    print("Datos recibidos", deserializa)
    #hacer ciclo para sumar losvalores y enviar los resultados al clineete
    suma = 0
    for i in deserializa:
        suma += int(i)  
    cs.send(str(suma).encode("ascii"))#5Envia datos procesados
    cs.close()#5.1 cierra el la conexión con el dhcp
ss.close()
