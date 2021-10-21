def croissant(a,b,c):
    if a <= b :
        if b <= c :
            resultat = True
        else :
           resultat = False
    else :
        resultat = False
    return resultat

print(croissant(1,2,6))