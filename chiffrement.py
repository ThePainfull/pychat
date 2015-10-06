#!!!!le message à crypter ne doit pas comporter les caractères suivants: é , è , à , ö , ü , ä , ç , £ , § , °
#le module AES ne peut pas décrypter ces caractères après les avoir cryptés
from Crypto.Cipher import AES
#packages qui contiennent des algorithmes de cryptage,on importe le module Advanced Encryption Standard
from Crypto.Util import Counter
#on importe du package utilitaire le module Counter qui contient des fonctions Counter pour le mode CTR

clé="rger6gdg794684g5"
#exemple de clé
#la clé doit faire 16 caractères sinon ca ne marche pas

def cryptage(msgEnvoi):
 #le message à envoyer doit être un string entre guillemets ou être en bytes

 chiffrement=AES.new(clé,AES.MODE_CTR,counter=Counter.new(128))
 #on définit un chiffrement avec la clé donnée, le mode de chiffrement choisi(CTR) et le compteur (nécessaire pour CTR)
 #on prend CTR car c'est le seul mode du module AES qui permet de crypter des messages de n'importe quelle longueur
 #la valeur du compteur doit etre 128 sinon ca ne marche pas
 return chiffrement.encrypt(msgEnvoi)
 #cette commande renvoit un message en bytes crypté avec le chiffrement qu'on a défini

def décryptage(msgRecu):
 #le message recu doit être en bytes

 déchiffrement=AES.new(clé,AES.MODE_CTR,counter=Counter.new(128))
 #on doit définir le déchiffrement exactement comme le chiffrement parce qu'on ne peut pas décrypter le message 
 #avec la même fonction qu'on a utilisé pour crypter(ca le crypte à nouveau)

 return déchiffrement.decrypt(msgRecu)
 #cette commande déchiffre le message crypté
