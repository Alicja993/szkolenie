import random
from lekcja2  import Figura, Prostokąt, Kwadrat
#for element in kolekcja:
   # print(element)


 #hodowla = ["kot", "pies", "kura", "krowa"]
    ###try :
       # while True:
       #  zwierze = next(iterator)
         #print(zwierze)
   # except StopIteration:
       # pass

class Fibs :
    def __init__(self, limit):
        self.a = 0
        self.b = 1
        self.limit = limit
    def __iter__(self):
     #  return FibsIter(self)
        return self
    def __next__(self):
        (self.a , self.b ) = (self.b , self.a + self.b)
        if self.b > self.limit:
            raise StopIteration
        return self.b

#   #przyklad:
# f = Fibs(10000)
# for wyraz in f:
#     print(wyraz)
#
# print (iter(f), f ==iter(f))
# #print(iter(g), g == iter(g))
# it = iter(f) # f.__iter__()
#   # - > f == it


class Card:
    def __init__(self, value , color):
        self.value = value
        self.color = color
    def __repr__(self):
        return f"{self.color} {self.value}"

class Deck:
    def __init__(self):
        values = [ "A" , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ,10 , "J" , "Q" , "K"]
        colors = ["♠", "♣", "♡", "♢"]
        self.cards = [
            Card(value, color)
            for color in colors
            for value in  values

        ]
    def __iter__(self):
        return iter(self. cards)

    def shuffle(self):
        random.shuffle(self.cards)


d = Deck()
# #print(d.cards[0:10])
#
# for card in d:
#     print(card,end=",")
# print()
# #tasowanie
# d.shuffle()
# for card in d:
#     print(card, end=",")
#     print()
#iterowanie python
#zaawansowana obiektowosc
#funkcje ilustrujace powiazanie klas

print("Czy Prostokat jest pochodna Figury?",issubclass(Prostokąt, Figura))
print("Czy  Kwadrat jest pochodna figury? " , issubclass(Kwadrat,Figura))
print("Czy d jest instancja klasy Deck?", isinstance(d,Deck))
print("Czy d jest instancja klasy Kwadrat?", isinstance(d,Kwadrat))
print("Czy d ma pole cards " ,hasattr(d , "cards"))
print("Czy d.cards[0] ma kolor:",getattr(d.cards[0],"color"))
print( "Czy d.cards.append jest wywolywalne?",callable(d.cards.append))

#skladowe prywatne klasy
