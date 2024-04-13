class Node:
    def __init__(self,naziv : str,zanr : str, godina : int, ocjena : float):
        self.naziv = naziv
        self.zanr = zanr
        self.godina = godina
        self.ocjena = ocjena
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, new_element):
        current =self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def prepend(self, new_element):
        if self.head:
            new_element.next = self.head
            self.head = new_element
        else:
            self.head = new_element
    
    def stampaj(self):
        current = self.head
        if self.head:
            while current:
                print(current)
                current = current.next

    #2w.Kreirati jednostruko olančanu listu, gdje svaki čvor predstavlja pjesmu. Data dio svakog čvora sadrži 4 podatka i to naziv (string), zanr (string), godina (int), ocjena (float) pjesme.

    #i. Izračunati ukupnu prosječnu ocjenu svih pjesama za zadatu godinu (godina parametar funkcije).

    def prosjecna_ocjena(self,god):
        current = self.head
        suma = 0
        brojac = 0
        if self.head:
            while current:
                if god == current.godina:
                    suma = suma + current.ocjena
                    brojac = brojac + 1    
                current = current.next
            return suma/brojac
        else:
            return None

    # ii. Štampati one pjesme čija je čija je godina manja od zadate godine (parametar funkcije max_godina).
    
    def max_godina (self,god):
        current = self.head
        if self.head:
            while current:
                if god > current.godina:
                    print(current.naziv)
                current = current.next       
        else:
            return None            
    
    # iii. Štampati pjesme koje imaju veću ocjenu od prosječne ocjene svih pjesama. Iskoristiti funkciju pod a) za računanje prosječne ocjene.  
    '''funkcija pod a racuna prosjek samo za naznacenu godinu, tako da ce i ova naredna funkcija jer koristi funkciju pod a), isto tako da racuna samo za navedenu godinu,
      nisam znao treba li nova funkcija za prosjek koja racuna prosjek za sve'''
    def vece_od_prosjeka(self, value):
        current = self.head
        if self.head:
            while current:
                if current.ocjena>value:
                    print(current.naziv)
                current = current.next
        else:
            return None
        
n1 = Node("Pjesma 1","Pop",2018,5)
n2 = Node("Pjesma 2","Pop",2018,10)
n3 = Node("Pjesma 3","Rok",2016, 9)
n4 = Node("Pjesma 4", "Balada", 2018,7)
n5 = Node("Pjesma 5","Rock",2022, 10)

l1 = LinkedList()
l1.append(n1)
l1.append(n2)
l1.append(n3)
l1.append(n4)
l1.append(n5)

print(l1.prosjecna_ocjena(2018))
print('\n')
l1.max_godina(2020)
print('\n')
l1.vece_od_prosjeka(l1.prosjecna_ocjena(2018))