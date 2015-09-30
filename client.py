import socket
import protocols
from threading import Thread

hote ='129.194.185.75'
#hote = '86.119.30.14'
port = 12001

connecServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connecServeur.connect((hote,port))

print("connexion avec le serveur sur le port {}".format(port))


def envoi():
    msgEnvoi=""
    while 1 : #msgEnvoi != "/quit":
        msgEnvoi=input("> ")
        msgEnvoi=protocols.envoyer(msgEnvoi,"001")
        connecServeur.send(msgEnvoi)

    print("Fermeture connec")
    connecServeur.close()
    return


def ecoute():
    while 1:
        msgRecu = connecServeur.recv(1024)
        msgRecu2 = protocols.recevoir(msgRecu)["msg"]
        print(msgRecu2)


t1 = Thread(target=ecoute,args=())
t2 = Thread(target=envoi,args=())
t1.start()
t2.start()

