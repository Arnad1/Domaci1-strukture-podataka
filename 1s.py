#Napisati rekurzivnu funkciju koja provjerava da li su sve cifre zadatog broja m djelioci broja n. Brojevi m i n su prirodni brojevi.

def da_li_su_djelioci(m,n):
    if m!=0:
        if n%(m%10)==0:
            return da_li_su_djelioci(m//10,n)
        else:
            return "Ne"
    return "Da"    

m = 223
n = 12
print(da_li_su_djelioci(223,12))
