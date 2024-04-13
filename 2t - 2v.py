class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList():
    def __init__(self, head = None):
        self.head = head

    def prepend(self,new_element):
        new_element.next = self.head
        self.head = new_element

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
        
    #2t - Napisati funkciju custom_count(value) koja za zadatu jednostruko olančanu listu prebrojava koliko elemenata je veće od zadate vrijednosti 
    def custom_count(self,value):
        brojac = 0
        current = self.head
        if self.head:
            while current:
                if current.value>value:
                    brojac = brojac + 1
                current = current.next
        return brojac
    
    # 2u. Date su dvije jednostruko povezane liste prirodnih brojeva. Ispitati da li su iste

    def da_li_su_iste (self,l2):
        current1 = self.head
        current2 = l2.head
        while current1 and current2:
            if current1.value == current2.value:
                pass
            else:
                return "Nisu iste"
            current1 = current1.next
            current2 = current2.next
        return "Iste"
    
    #2v. Napisati funkciju intersection(l1, l2) koja za dvije unijete liste vraca trecu listu koja se dobija kao presjek te dvije unesene liste.

    def intersection(self,l1,l2):
        current1 = l1.head
        current2 = l2.head
        while current1 and current2:
            if current1.value == current2.value:
                self.append(Node(current1.value))   
                current1 = current1.next
                current2 = current2.next
    
    def stampaj(self):
        current = self.head
        if self.head:
            while current:
                print(current.value)
                current = current.next

            
    

n1 = Node(5)
n2 = Node(3)
n3 = Node(6)
n4 = Node(9)
n5 = Node(8)

n6 = Node(5)
n7 = Node(3)
n8 = Node(6)
n9 = Node(9)
n10 = Node(8)


l1 = LinkedList()
l1.append(n1)
l1.append(n2)
l1.append(n3)
l1.append(n4)
l1.append(n5)

print(l1.custom_count(5))
print('\n')
l2 = LinkedList()
l2.append(n6)
l2.append(n7)
l2.append(n8)
l2.append(n9)
l2.append(n10)

print(l1.da_li_su_iste(l2))
print('\n')
l3 = LinkedList()
l3.intersection(l1,l2)
l3.stampaj()