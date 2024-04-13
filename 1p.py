#Napisati rekurzivnu funkciju koja računa koliko niz/lista ima negativnih brojeva koji su djeljivi sa 2.

def neg_djeljivi(lista):
    if len(lista) == 0:
        return 0
    else:
        if lista[0] < 0 and lista[0] % 2 == 0:
            return 1 + neg_djeljivi(lista[1:])
        else:
            return 0 + neg_djeljivi(lista[1:])
    
l1 = [1,5,-4,3,7,-8]

print(neg_djeljivi(l1))