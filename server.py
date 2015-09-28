import socket
import select

hote =''
port = 12850

connecMain = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connecMain.bind((hote,port))
connecMain.listen(5)
print("le serveur écoute sur le port {}".format(port))


serveurLance = True
clientsConnectes=[]
while serveurLance :
    connecDemandees,wlist,xlist = select.select([connecMain],[],[],0.05)
    for connexion in connecDemandees:
        connecClient, infosConnec = connexion.accept()
        clientsConnectes.append(connecClient)
    clientsALire = []
    try:
        clientsALire,wlist,xlist = select.select(clientsConnectes,[],[],0.05)
    except select.error:
        pass
    else:
        for client in clientsALire:
            msgRecu = client.recv(1024)
            msgRecu2 = msgRecu.decode()
            print("recu : {}".format(msgRecu2))
            for clients in clientsConnectes :
                if clients != client:
                    clients.send(msgRecu)
            #if msgRecu == "fin":
            #    serveurLance = False

print("fermeture connexion")
for client in clientsConnectes:
    client.close()

connecMain.close()


"""
msgRecu = b""
while msgRecu != b"fin":
    msgRecu = connecClient.recv(1024)
    print(msgRecu.decode())
    connecClient.send(b"recu 5/5")
"""