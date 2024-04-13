class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinekdList:
    def __init__(self, head = None):
        self.head = head
    
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    
    def prepend(self,new_element):
        if self.head:
            new_element.next = self.head
            self.head = new_element
        else:
            self.head = new_element
    

    # 2x. Data je datoteka brojevi.txt (vi je kreirajte) koja sadrzi cijele brojeve, po jedan u svakom redu.
    
    # i. Napisati funkciju koja iz zadate datoteke učitava brojeve i smješta ih u listu
    
    def ucitaj_brojeve (self, data):
        file = open(data,"r")
        brojevi = file.readlines()
        for broj in brojevi:
            self.append(Node(broj.strip()))

    def stampaj(self):
        current = self.head
        if self.head:
            while current:
                print(current.value)
                current = current.next

    # ii.Napisati funkciju koja u jednom prolazu kroz zadatu listu cijelih brojeva pronalazi maksimalnu strogo rastuću podlistu
    
    def max_rastuca(self):
        current = self.head
        lista = []
        lista1 = []
        brojac = 0
        brojac1 = 0
        if self.head:
            while current.next:
                if  int(current.value) < int(current.next.value):
                    lista.append(current.value)
                    brojac = brojac + 1
                    if current.next.next:
                        if int(current.next.value) > int(current.next.next.value):
                            lista.append(current.next.value)
                            brojac = brojac + 1
                else:
                    if brojac>brojac1:
                        brojac1 = brojac
                        lista1 = lista
                    brojac = 0
                    lista = []
                current = current.next
        return lista1

    # iii.Koristeci funkcije pod a) i b) napisati program koji u datoteku Rezultat.txt upisuje nadjeni strogo rastuci podniz.
    
    def upisi_rastuci(self, brojevi, data):
        file = open(data,"w")
        line = ["Ovo je najduzi rastuci podniz u listi \n"]
        file.writelines(line)
        for broj in brojevi:
            file.writelines(broj)
            file.writelines("\n")

l1 = LinekdList()
l1.ucitaj_brojeve("brojevi.txt")
l1.stampaj()
print('\n')
print(l1.max_rastuca())
print('\n')
l1.upisi_rastuci(l1.max_rastuca(),"Rezultat.txt")