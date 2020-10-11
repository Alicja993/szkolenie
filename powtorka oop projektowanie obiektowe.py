import math
# dfinicja klasy python


#class Vector:

#obiekt-instancja klasy - definicja zapisu 2 sposoby
#obiekt = Vector()
#*instancja = Vector()
#metoda do opisania klasy- definicja skladni
# class Vector:
#     #x = 0
#     #y = 0
#     def __init__(self, x , y , c):
#         self.x = x
#         self.y = y
#        # self.c = (x**2 + y**2)**0.5#dlugosc vectora
#
#    # def nazwa_metody(self, arg1):
#     #    print(arg1)#metoda liczaca modul vectora(dlugosc)
#     def modul(self):
#         self.c = (self.x **2 + self.y **2) **0,5
#
# #obiekt = Vector()
# #obiekt.nazwa_metody("Alicja")
####obiekt.modul()
#print(obiekt.x)
#print(obiekt.y)
#print(instancja.c)

#cwiczenie konto bankowe

# class BankAccount:
#     def __init__(self,name, balance=0):
#         self.name = name
#         self.balance = balance
#
#     def info(self):
#         print(f"To jest konto {self.name}, a jego saldo: {self.balance}")
#
#     def withdraw(self,value):#wyplata z konta (withdraw)
#         if self.balance >= value :
#             # self.balance = self.balance - value
#              self.balance -= value# krotszy zapis kodu
#         else :
#             print("Nie mozna wyplacic pieniedzy")
#
#     def deposit (self, value):#wplata na konto (deposit)
#        # self.balance = self.balance + value
#         self.balance += value#krotszy zapis kodu
#
#     def transfer (self, dest , amount):#kwota do przelania amount
#        if self.balance >= amount:
#             # self.balance = self.balance - amount# pomoejszenie kwoty przelewu z konta glownego
#         #dest.balance = dest.balance + amount#przelew na konto
#         dest.balance += amount #krotszy zapis
#        else:
#          print("Nie mozna przelac pieniedzy")
#
#




# implementacja metody zabezpieczajaca konto przed debetem na koncie blokada

# kt = BankAccount("test", 1000)
# kt.info()
# kt.withdraw(1000)
# kt.info()
# kt2 = BankAccount("test2", 0)
# kt2.info()
# kt2.transfer(kt2, 1000)
# kt2.info()



# jk = BankAccount("Jan Kowalski", 1000)
# jk.info()
# jk.deposit(2000)
# jk.withdraw(2500)
# jk.info()
# jk.balance = 0
# jk.info()
# fn  = BankAccount("Franek Nowak")
# jk.transfer (fn, 100 )
# jk.info()
# fn.info()



#dziedziczenie klasy


class KlasaRodzica:
    atrybut = "wartosc"
    def metoda(self):
        print(f"Stara:{self.__class__.__name__}:{self.atrybut}")

class KlasaPochodona(KlasaRodzica):
    def metoda(self):
        print(f"Nowa:{self.__class__.__name__}:{self.atrybut}")


#testujemy
#instancja_rodzica = KlasaRodzica()
#instancja_rodzica.metoda()

#instancja_dziecka = KlasaPochodna()
#instancja_dziecka.metoda()


class BankAccount:
    def __init__(self,name, balance=0):
        self.name = name
        self.balance = balance

    def info(self):
        print(f"To jest konto {self.name}, a jego saldo: {self.balance}")

    def withdraw(self,value):#wyplata z konta (withdraw)
        if self.balance >= value :
            # self.balance = self.balance - value
             self.balance -= value# krotszy zapis kodu
        else :
            print("Nie mozna wyplacic pieniedzy")

    def deposit (self, value):#wplata na konto (deposit)
       # self.balance = self.balance + value
        self.balance += value#krotszy zapis kodu

    def transfer (self, dest , amount):#kwota do przelania amount
       if self.balance >= amount:
            # self.balance = self.balance - amount# pomoejszenie kwoty przelewu z konta glownego
        #dest.balance = dest.balance + amount#przelew na konto
        dest.balance += amount #krotszy zapis
       else:
         print("Nie mozna przelac pieniedzy")


class DebitBankAccount(BankAccount):
    def __init__(self, name ,limit , balance = 0):
        super().__init__(name , balance)
        self.limit = limit # liczba ujemna np . -100
    def info(self):
        super().info()
        print(f"Limit konta to{self.limit}")
    def withdraw(self, value):
        # sprawdzenie czy po wyplacie kwoty stan konta bedzie rowny lub wiekszy limtowi
        if (self.balance - value) >= self.limit:# odejmowanie pieniedzy z konta self.balance-konto value-kwota do wyplaty
            self.balance -= value
        else:
            print("Nie mozna wyplacic - przekorczony limit")

        #przelew pieniedzy z jednego konta na drugie
    def transfer(self, other , value):
        if(self.balance - value) >= self.limit:
            self.balance -= value
            other.balance += value
        else:
            print("Nie mozna zrobic przelewu")



#test klasy dziedziczenie


#dziedziczenie klas dla fiugu
class Figura:
    def obwod(self):
        raise NotImplementedError #wyjatek -raise klasa abstarkcyjna sluzaca do definiowania metod dla kas pochodnych

    def pole(self):
        raise NotImplementedError

class Prostokat(Figura):
    def __init__(self, a , b):
        self.a = a
        self.b = b
    def obwod (self):
        return 2* self.a + 2 * self.b

    def pole(self):
        return self.a * self.b

class Kwadrat(Prostokat):
    def __init__(self, a):
        self.a = a
        self.b = a

class Kolo(Figura):
    def __init__(self,r ):
        self.r = r

    def obwod(self, r):
        return 2 * math.pi * self.r #obwod kola 2 pi r 2*3,14*r

    def pole(self,):
        return math.pi * (self.r ** 2)

# p3 = Kolo(10)
# print(p3.obwod())
# print(p3.pole())






#testujemy

# p1= Prostokat(10, 20)
# print(p1.obwod())
# print(p1.pole())
# p2 =Kwadrat (10)
# print(p2.obwod())
# print(p2.pole())
#

class TrojkatRownoboczny(Figura):
    def __init__(self ,a , h):
        self.a = a
        self.h = h
        return 





