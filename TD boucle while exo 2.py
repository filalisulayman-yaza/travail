def decroissant_for(n):
    for i in range(n,0,-1):
        print(i, end='  ')

def decroissant_while(n):
    while n > 0 :
        print(n)
        n = n - 1
decroissant_while(9)