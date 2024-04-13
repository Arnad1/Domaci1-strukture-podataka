#Napisati rekurzivnu funkciju koja vraća poslednje veliko slovo zadatog stringa.

def poslednje_veliko_slovo(str):
    if len(str) > 0:
        if str[-1].isupper() and str[-1]!=' ':
            return str[-1]
        else:
            return poslednje_veliko_slovo(str[0:-1])

string = "Neki tamo String Koji iMa VELIKA slOva"
print(poslednje_veliko_slovo(string))