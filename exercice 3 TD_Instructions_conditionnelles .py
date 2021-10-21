def bowling(boule1, boule2):
    """
    Description de la fonction : Affiche à l'écran les performances d'un joueur de bowling
    boule1 (int) : nombre de quilles renversées avec la première boule
    boule2 (int) : nombre de quilles renversées avec la deuxième boule
    préconditions sur les entrées : boule1 + boule2 <= 10 
    """
    if boule1 == 10 :
        print("X")
    elif boule2+boule1 == 10 :
        print("/")
    else:
        print(boule1+boule2)
        
bowling(6,3)