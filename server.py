import socket
import select
import protocols

hote =''
port = 12001

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
            msgRecu2 = protocols.recevoir(msgRecu)
            print("recu : {}".format(msgRecu2))
            for clients in clientsConnectes :
                if clients != client:
                    clients.send(msgRecu)
            if msgRecu2["msg"] == "/affiche":
                #print("/affiche")

                msgEnvoi=protocols.envoyer("client","all","001","5/5")
                client.send(msgEnvoi)
            elif msgRecu2["msg"] == "/quit":
                client.close()
print("fermeture connexion")
for client in clientsConnectes:
    client.close()

connecMain.close()
print()