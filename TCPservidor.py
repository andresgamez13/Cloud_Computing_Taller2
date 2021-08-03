from socket import *

def saldo():
    f = open("saldo.txt", "r")
    saldo = f.read()
    f.close()
    return(saldo)

def debitar(x):
    f = open("saldo.txt", "r")
    saldo = int(f.read())
    f.close()
    if(x>saldo):
        return "Saldo Insuficiente"
    else:
        file1 = open("saldo.txt","w")
        file1.write(str(saldo-x))
        file1.close()
        return "OK"

def acreditar(y):
    f = open("saldo.txt", "r")
    saldo = int(f.read())
    f.close()
    n_saldo = y+saldo
    f2 = open("saldo.txt", "w")
    f2.write(str(n_saldo))
    f2.close()
    return "Nuevo Saldo: "+ str(n_saldo)

servidorPuerto = 12000
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)
print("El servidor está listo para recibir mensajes")
while 1:
    conexionSocket, clienteDireccion = servidorSocket.accept()
    print("Conexión establecida con ", clienteDireccion)
    mensaje = (str( conexionSocket.recv(1024), "utf-8" )).upper()
    message_l = mensaje.split(" ")
    if (message_l[0] == "DEBITAR"):
        mensaje_f = debitar(int(message_l[1]))
    elif (message_l[0] == "ACREDITAR"):
        mensaje_f = acreditar(int(message_l[1]))
    elif (message_l[0] == "SALDO"):
        mensaje_f = saldo()
    else:
        mensaje_f = "INGRESE UNA OPCIÓN VÁLIDA"

    print("Mensaje recibido de ", clienteDireccion)
    print("El mensaje recibido fue ", mensaje)
    
    print("El mensaje enviado fue ", mensaje_f)
    conexionSocket.send(bytes(mensaje_f.upper(), "utf-8"))
    conexionSocket.close()


