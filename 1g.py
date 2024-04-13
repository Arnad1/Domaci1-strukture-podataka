#Napisati rekurzivnu funkcija koja pretvara prirodan dekadni broj u birani broj

def to_binary(br):
    if br>0:
        return to_binary(br//2) + str(br%2)
    else:
        return ''

print(to_binary(24))

