#definicja klasy
class Vector: # nazwa clasy
    pass # pusta klasa
# instancjaobiekt = Vector ()#definicja klasy
instancja = Vector()#(parametry)
#metoda
#class Vector:
   # def nazwa_metody(self):#self wewnatrz metody umozliwia dostep do obiektu
       # pass
#definicja klasy
class Vector:
   # x = 0
   # y = 0
    def __init__(self,x,y):
        self.x=x
        self.y =y
      #  self.c = (x**2+y**2)**0.5
    def modul(self):
        #self.c = (self.x**2 + self.y**2)**0.5
        return (self.x ** 2 + self.y ** 2) ** 0.5
   # def nazwa_metody(self, arg1):
      #  print(arg1)
obiekt = Vector(2,2)
#obiekt.nazwa_metody("Alicja")
instancja = Vector(4,2)
print(obiekt.modul())
print(instancja.modul())
#inplementacja konta bankowego

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
konto_1 = BankAccount("Jan Kowalski", 1000)
konto_2 = DebitAccount("Krzysztof Nowak", limit=-100, balance=500)
konto_1.info()
konto_2.info()
konto_2.transfer(konto_1, 601)



#

#konto testowe
#jk = BankAccount("Jan Kowalski",1000)
#jk.info()
#jk.deposit(2000)
#jk.withdraw(2500)
#jk.info()
#jk.balance = 0
#jk.info()
#fn = BankAccount("Franek Nowak")
#jk.transfer(fn, 100)
#jk.info()
#fn.info()
#kt2 = BankAccount(1000)
#kt2.info()
#kt.info()








