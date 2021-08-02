from socket import *
import time

servidorNombre = "54.147.175.249" 
servidorPuerto = 12000

def request(ind,val):
    Request = ['saldo','debitar {}'.format(val+50),'debitar {}'.format(val-20),'saldo','acreditar {}'.format(val*2),'saldo']
    return Request[ind]

sal=0
for i in range(6):
    clienteSocket = socket(AF_INET, SOCK_STREAM)
    clienteSocket.connect((servidorNombre,servidorPuerto))
    mensaje = request(i,sal)
    print(mensaje)
    clienteSocket.send(bytes(mensaje, "utf-8"))
    if (mensaje=='saldo'):
        sal = int(str(clienteSocket.recv(1024), "utf-8"))
        print("Respuesta_S:\n"+str(sal))
    else:
        mensajeRespuesta= clienteSocket.recv(1024)
        print("Respuesta:\n" + str(mensajeRespuesta, "utf-8"))
    clienteSocket.close()
    time.sleep(2)