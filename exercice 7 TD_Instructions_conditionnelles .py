def triangle(c1,c2,c3):
    """
    description de la fonction : affiche une des caractéristiques du triangle suivante : équilatéral, isocèle ou scalène
    c1, c2, c3 (int ou float) : trois côtés du triangle
    précondition sur les entrées : on considère que les valeurs de c1, c2 et c3 doivent permettre de construire un triangle
    return (None)
    """
    if c1 == c2 == c3:
        print("équilatéral")
    elif c1 == c2:
        print("isocèle")
    elif c2 == c3:
        print("isocèle")
    elif c1 == c3:
        print("isocèle")
    else:
        print("scalène")
        
triangle(1,52,4)
    