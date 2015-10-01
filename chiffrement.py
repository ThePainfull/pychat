from Crypto.Cipher import AES
#packages qui contiennent des algorithmes de cryptage,on importe le module Advanced Encryption Standard
from Crypto.Util import Counter
#on importe du package utilitaire le module Counter qui contient des fonctions Counter pour le mode CTR

clé="rger6gdg784684g5"#doit faire 16 caractères

def cryptage(msgEnvoi):

 chiffrement=AES.new(clé,AES.MODE_CTR,counter=Counter.new(128))#doit etre 128
 #on définit le chiffrement avec la clé, le mode(CTR) et le compteur

 return chiffrement.encrypt(msgEnvoi)

def décryptage(msgRecu):

 déchiffrement=AES.new(clé,AES.MODE_CTR,counter=Counter.new(128))#doit etre 128

 return déchiffrement.decrypt(msgRecu)
