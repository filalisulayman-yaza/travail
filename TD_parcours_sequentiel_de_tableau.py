def recherche_minimum(liste):
    i = 0
    minimum_temp = liste[0] 
    for a in liste:
        if liste[i] < minimum_temp:
            minimum_temp = liste[i]
        i = i + 1 # passage au suivant
    return minimum_temp
print(recherche_minimum([3,15,25,6,7]))
