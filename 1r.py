#Napisati rekurzivnu funkciju koja okreće string

def obrni(str):
    if len(str)>0:
        return str[-1] + obrni(str[0:-1])
    else:
        return str
    
string = 'zdravo'
print(obrni(string))