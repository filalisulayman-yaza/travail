def bac(prenom,nom,moyenne):
    if moyenne >= 10:
        print(prenom,nom, "a obtenu son bac, Félicitations !")
bac('alice','dupont',10)
        
bac('bob', 'martin',9)

def bac2(prenom,nom,moyenne):
    if moyenne >= 10:
        print(prenom,nom, "a obtenu son bac, Félicitations !")
    else:
        print(prenom,nom,"n'a pas obtenu son baccalauréat")
        
bac2("Alice", "Dupont", 12)
bac2("Bob", "Martin", 9)