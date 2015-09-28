import socket
from threading import Thread

hote ='86.119.30.14'
port = 12820

connecServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connecServeur.connect((hote,port))

print("connexion avec le serveur sur le port {}".format(port))


def envoi():
    msgEnvoi=b""
    while msgEnvoi != b"quit":
        msgEnvoi=input("> ")
        msgEnvoi=msgEnvoi.encode()
        connecServeur.send(msgEnvoi)

    print("Fermeture connec")
    connecServeur.close()


def ecoute():
    while 1:
        msgRecu = connecServeur.recv(1024)
        print(msgRecu.decode())


t1 = Thread(target=ecoute,args=())
t2 = Thread(target=envoi,args=())
t1.start()
t2.start()

