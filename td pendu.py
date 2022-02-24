LETTRES_DEJA_CHOISIES = []

def nettoyage_mot(mot):
    mot = mot.lower()
    mot = mot[0:len(mot)-1]
    accent = ['é','è','ë','ê','â','à','ä''ü','û','ï' 'î','ç','ô']
    sans_accent['e','e','e','e''a','a','a','u','u','i','i','c','o']
    i=0
    while i < len(accent):
        mot=mot.replace(accent[i], sans_accent[i])
        i=i+1
    return mot

def tirage_au_sort(nom_fichier):
    fichier = open(nom_fichier,'r', encoding = 'utf8')
    for chiffre in range(randint(1,22274)):
        chaine = fichier.readline()
    fichier.close()
    return chaine

def deja_choisie(lettre):
    global LETTRES_DEJA_CHOISIES
    if lettre in LETTRES_DEJA_CHOISIES:
        print('lettre déjà choisie')
        return True
    else:
        liste = [lettre]
        LETTRES_DEJA_CHOISIES = LETTRES_DEJA_CHOISIES +  liste
        return False
    
        
    