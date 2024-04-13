class Node:
    def __init__(self, ime : str, prezime : str, godine : int, prosjek : float):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.prosjek = prosjek
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self, head = None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
            new_element.prev = current
        else:
            self.head = new_element
    
    def stampaj(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    #6. Kreirati dvostruko olančanu listu sa bar 5 elemenata, gdje svaki čvor sadrži 4 podatka i to ime (string), prezime (string), godina (int), prosjek (float) studenta.
    
    # a. Izdvojiti one studente čiji je prosjek veći od zadatog (zadaje se kao parametar). Prebrojati koliko studenata ima veći prosjek od zadatog.
    
    def izdvoji_studente(self, value):
        current = self.head
        brojac = 0
        if self.head:
            while current:
                if current.prosjek > value:
                    print(current.ime)
                    brojac = brojac + 1
                current = current.next
        return print (f"{brojac} studenta imaju prosjek veci od zadatog")

    # b. Štampati sve elemente liste koji se pojavljuju prije zadatog indeksa u obrnutom poretku.

    def stampaj_prije_indeksa(self,value):
        current = self.head
        index = value
        brojac = 1
        if self.head:
            while current and brojac<index:
                current = current.next
                brojac = brojac + 1
            while current.prev:
                print(current.prev.ime)
                current = current.prev            

                
n1 = Node("Arnad","Lekic",22,9.8)
n2 = Node("Elvis","Taruh",22,10)
n3 = Node("Anesa","Abazovic",23,9.1)
n4 = Node("Nikola","Kavaric",21,8.4) 
n5 = Node("Josif","Vukicevic",22,8.2)               

l1 = DoublyLinkedList()
l1.append(n1)
l1.append(n2)
l1.append(n3)
l1.append(n4)
l1.append(n5)

l1.izdvoji_studente(8.5)
print('\n')
l1.stampaj_prije_indeksa(5)
