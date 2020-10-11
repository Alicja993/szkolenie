import math
#class KlasaRodzica:

   # atrybut = "wartość"

   # def metoda(self):
      #  print(f"stara: {self.__class__.__name__}:{self.atrybut}")


#class KlasaPochodna(KlasaRodzica):
   # def metoda(self):
      #  super().metoda()
       # print(f"nowa:{self.__class__.__name__}:{self.atrybut}")


#testujemy

#instancja_rodzica = KlasaRodzica()
#instancja_rodzica.metoda()
#instancja_dziecka = KlasaPochodna()
#instancja_dziecka.metoda()




# from lekcja1 import BankAccount
# class KlasaRodzica:
#     atrybut = "wartość"
#     def metoda(self):
#         print(f"STARA: {self.__class__.__name__}: {self.atrybut}")
# class KlasaPochodna(KlasaRodzica):
#     def metoda(self):
#         super().metoda()
#         print(f"NOWA: {self.__class__.__name__}: {self.atrybut}")
# testujemy
# instancja_rodzica = KlasaRodzica()
# instancja_rodzica.metoda()
# print('============================')
# instancja_dziecka = KlasaPochodna()
# instancja_dziecka.metoda()
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def info(self):
        print(f"Konto {self.name}, stan: {self.balance}")
    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
        else:
            print(f"Za niskie saldo do wypłaty {value}")
    def deposit(self, value):
        self.balance += value
    def transfer(self, dest, amount):
        if self.balance >= amount:
            self.balance -= amount
            dest.balance += amount
        else:
            print(f"Za niskie saldo do przelewu {amount}")

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance
    def __bool__(self):
        return bool(self.balance)


class DebitAccount(BankAccount):
    def __init__(self, name, limit, balance=0):
        super().__init__(name, balance)
        self.limit = limit  # negative value, e.g. -100
    def info(self):
        super().info()
        print(f"limit konta: {self.limit}")
    def withdraw(self, value):
        if (self.balance - value) >= self.limit:
            self.balance -= value
        else:
            print("Przekroczony limit")
    def transfer(self, other, value):
        if (self.balance - value) >= self.limit:
            self.balance -= value
            other.balance += value
        else:
            print("Przekroczony limit")
#konto_1 = BankAccount("Jan Kowalski", 1000)
#konto_2 = DebitAccount("Krzysztof Nowak", limit=-100, balance=500)
#konto_1.info()
#konto_2.info()
##konto_2.transfer(konto_1, 601)
#konto_1.info()
#konto_2.info()
#def info(konto: BankAccount):
    # polimorfizm: funkcja akceptuje nie tylko klasę bazową BankAccount,
    # ale także jej klasy pochodne (tutaj: DebitAccount)
    #print(f"Konto dla: {konto.name}")
   # print(f"-- saldo: {konto.balance}")
#info(konto_1)
#info(konto_2)


class Figura:
    def obwod(self):
        raise NotImplementedError
    def pole(self):
        raise NotImplementedError



class Prostokąt(Figura) :
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def obwod(self):
        return 2* self.a + 2* self.b

    def pole(self):
        return self.a * self.b


p1 = Prostokąt(10,20)
#print(p1.obwod())
#print(p1.pole())


class Kwadrat(Prostokąt) :
    def __init__(self,a):
        self.a = a
        self.b = a




p2 = Kwadrat(10)
#print(p2.obwod())
#print(p2.pole())


class Kolo(Figura):
    def __init__(self, r):
        self.r = r

    def obwod(self):
        return 2 * math.pi * self.r

    def pole(self):
        return math.pi * (self.r ** 2)


#p3 = Kolo (10)
#print(p3.obwod())
#print(p3.pole())

class TrojkatRownoramienny(Figura):

    def __init__(self, a , h):
        self.a = a
        self.h = h
    def obwod(self):
        return 2 * (self.h ** 2 + (0.5 * self.a) ** 2) ** 0.5 + self.a

    def pole(self):
        return self.a * self.h * 0.5

#p4 = TrojkatRownoramienny (6,4)
#print(p4.obwod())
#print(p4.pole())


class Rownoleglobok(Figura):
    def __init__(self , a, b ,h):
        self.a = a
        self.b = b
        self.h = h
    def obwod(self):
        return 2 * self.a + 2 * self.b
    def pole(self):
        return self.a * self.h

#figura_5 = Rownoleglobok(4,5,3)
#print(figura_5.obwod())
#print(figura_5.pole())


class TrapezProstokatny(Figura):
    def __init__(self, a , b ,h):
        self.a = a
        self.b  = b
        self.h = h
        self.c = ((self.a - self.b)** 2 + self.h**2 ) ** 0.5
    def pole(self):
        return 0.5 * (self.a  + self.b) * self.h
    def obwod(self):
      return   self.a+ self.b + self.c + self.h

#figura_6  =  TrapezProstokatny(10 , 7 , 4 )
#print(figura_6.obwod())
#print(figura_6.pole())

class A :
    """Rodzic pierwszy"""

    def __init__(self):
       print("A.__init__")
       super().__init__()
       self.a = "A"
class B :
    """Rodzic drugi"""
    def __init__(self):
        print("B.__init__")
        self.b = "B"

        super().__init__()

class Pochodna(B, A):
    """Dziecko"""

    def __init__(self):
        print("Pochodna.__init__")
        super().__init__()

#d = Pochodna()
# print(d.a)
# d.fa ()
# d.fb()
#print(Pochodna.__mro__)

class Pochodna(A,B):
    """Dziecko"""
    def __init__(self):
        self.a = "Pochodna"
        super().__init__()
    def __str__(self):
        return f"Klasa Pochodna {self.a}"

#d = Pochodna()
#print(str(d))
#print(d)
#e = Pochodna
#d > e



konto_1 = BankAccount("Jan Kowalski", 1000)
konto_2 = DebitAccount("Krzysztof Nowak", limit=-100, balance=500)
konto_1.info()
konto_2.info()




class Pochodna(A, B):
    """Dziecko"""
    def __init__(self):
        self.a = "Pochodna"
        super().__init__()

konto_1 = BankAccount("Jan Kowalski",0)
konto_2 = DebitAccount("Krzysztof Nowak", 0, 2000)


print(konto_1 < konto_2)
print(konto_1 <= konto_2)
print(konto_1 == konto_2)
print(konto_1 != konto_2)
print(konto_1 > konto_2)
print(konto_1 >= konto_2)


if konto_1:
    print("konto ma dodatnie saldo")
else:
    print("konto ma zerowe saldo")


import math
class Vector:
   # x = 0
   # y = 0
    def __init__(self,x,y,):
        self.x=x
        self.y =y



    #def __eq__(self, other):
      #  return self.x == other.x and self.y == other.y
  #  def __add__(self, other):
     #   return Vector(self.x + other.x , self.y + other.y)
      #  self.c = (x**2+y**2)**0.5
  #  def __sub__(self, other):
        # return  Vector.__add__(self, - other)
      #   return   self.__add__(-other)

   #sprubuj zaimplementowav za pomoca __neg__(ponizej)
 #   def __neg__(self):
      #  return Vector (- self.x, - self.y)
  #  def __abs__(self): #abs (v)
       # return math.hypot(self.x ** 2 + self.y ** 2)**0,5
   #zadanie z funkcja math.hypot
  # def __mul__(self,other): #vector * liczba
      # return Vector(other * self.y , other * self.y)
   #def __rmul__(self, other): #liczba * vector
     #  return Vector(other * self.x , other * self.y)
      # return self * other
   #def __truediv__(self,other): #vector\liczba
     #  return Vector (self.x / other , self.y / other)
  # def __repr__(self)
      # return
 #  def __str__(self):
      # return  "Vector({},{})".format(self.x, self.y)
  #  def modul(self):
      #  self.c = (self.x**2 + self.y**2)**0.5
#przetestuj metody zaimplementowane
#v1 = Vector (1, 5)
#v2 = Vector(3,1)

#print(v1 + v2)
# print (v1 - v2)
#print (v1 * 2)
#print(v1 / 2)
#print (v1)
#str(v1)


















