import socket
import select
import json
#import server

"""
def jsonification(message):
if message == /exit:
code = 003
    if code == 001:

    return messageJson
"""


def envoyer(message,code,recepteur = "all",emetteur = "client"):
    mess={}
    mess["msg"] = message
    mess["emetteur"] = emetteur
    mess["code"] = code
    mess["recepteur"] = recepteur
    mess=json.dumps(mess)
    return mess.encode()

def isLoginOK(login, password):

    return True

def recevoir(mess):
    message=json.loads(mess.decode())



    if message["code"] == 1:
        sendtoall()
    elif == 2
        if loginisOK():
            envoyer(34)
        else:
            envoyer()32

    #emetteur=mess["emetteur"]
    #recepteur=mess["recepteur"]
    #message=mess["msg"]
    #code = mess["code"]
    #for personne in server.clientsConnectes :
    return message