"""Chiffrage de Cesar et son déchiffrage (ASCII)"""

#Chiffrage

def cesar(chaine,k):
    
    chaine_crypt = ''
    for car in chaine:
        if car == ' ' :
            chaine_crypt += ' '
        else:
            chaine_crypt += chr((ord(car)+k)%126+32*((ord(car)+k)//126))
    return chaine_crypt

#Déchiffrage

def cesar_reverse(chaine,clé):
   
    chaine_decrypt = ''
    
    for element in chaine :
        if element == ' ':
            chaine_decrypt += ' '
        else:
            chaine_decrypt += chr(ord(element)-clé+94*((126-ord(element)+clé)//94))
    
    return chaine_decrypt