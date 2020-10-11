"""
Tamagotchi to mała, elektroniczna zabawka pozwalająca "opiekować się" zwierzakiem. Tamagotchi wymaga karmienia, zabawy, czy sprzątania po nim.

Zasady Tamagotchi:

humor określa się na podstawie licznika głodu i znudzenia; dopóki głód jest poniżej określonego poziomu, i dopóki znudzenie jest poniżej określonego poziomu, dopóty Tamagotchi jest szczęśliwy
karmienie zmniejsza poziom głodu o określoną liczbę punktów
nauka nowych słówek lub przywitanie się z Tamagotchi zmniejsza poziom znudzenia o określoną liczbę punktów
znane słówka są listą wyrażeń, które Tamagotchi może wypowiedzieć (np. "Mmmmrrp" albo "Hrrp")
można wywołać metodę, która odpowiada "tyknięciu" zegara - w jej wyniku nuda i głód rosną o jedną jednostkę
Implementacja Tamagotchi:

pola klasy: imie, prog_nudy, prog_glodu, malenie_nudy, malenie_glodu, poziom_nudy, poziom_glodu, slowa (lista)
metoda humor() musi zwracać, na podstawie prog_nudy, prog_glodu, poziom_nudy i poziom_glodu, czy Tamagotchi jest szczęśliwy, głodny lub znudzony
metoda __str__() musi zwracać imię Tamagotchi i jego humor (np. "Jestem Tobi. Czuję się szczęśliwy.")
metoda zegar() musi zwiększać poziom znudzenia i głodu o jedną jednostkę
metody zmniejsz_glod() i zmniejsz_nude() mają zmniejszać odpowiednio poziom_glodu i poziom_nudy o malenie_glodu i malenie_nudy; uwaga: oba poziomy nie mogą spaść poniżej zera
metoda przywitaj_sie() musi wylosować element z listy slowa, zmniejszyć nudę i wypisać na ekranie "{Imię} mówi {słowo}."
metoda naucz_slowo(slowo) dodaje słowo do listy slowa i zmniejsza nudę
metoda karm() zmniejsza głód
metody karm(), naucz_slowo(), przywitaj_sie() oraz __str__() wywołują zegar().
Do losowania elementu z listy slowa użyj funkcji random.choice.

Za wartości początkowe możesz przyjąć:

Pole	Wartość
prog_nudy	5
prog_glodu	10
malenie_nudy	4
malenie_glodu	6
słowa	["Mmmmrrp", "Hrrp"]
#gra tamagotchi :

"""
import random

class Tamagotchi:
    def __init__(self, imie):
        self.prog_nudy = 5
        self.prog_glodu = 10
        self.malenie_nudy = 4
        self.malenie_glodu = 6
        self.imie = imie
        self.poziom_nudy = 0
        self.poziom_glodu = 0
        self.slowa = ["Mmmmrrp", "Hrrp"]

    def __str__(self):
        x = f"Jestem {self.imie}. Czuję się {self.humor()}."
        self.zegar()
        return x

    def humor(self):
        if self. poziom_nudy >= self.prog_nudy:
            return "znudzony"

        elif self.poziom_glodu >= self.prog_nudy:
            return "glodny"
        else:
            return "szczesliwy"
       # if self.poziom_nudy < self.prog_nudy and self.poziom_glodu < self.poziom_glodu:
           # return "szczesliwy"


    def zegar(self):
        self.poziom_nudy += 1
        self.poziom_glodu +=1
        return self.poziom_nudy , self.poziom_glodu

    def zmniejsz_glod(self):
        self.poziom_glodu -= self.malenie_glodu
        if self.poziom_glodu < 0:
            self.poziom_glodu = 0

    def zmniejsz_nude(self):
        self.poziom_nudy -= self.malenie_nudy
        if self.poziom_nudy <0:
            self.poziom_nudy = 0


    def przywitaj_sie(self):
      slowo = random.choice(self.slowa)
      self.zmniejsz_nude()
      self.zegar()
      print(f"{self.imie} mowi{Przywitanie}")


    def naucz_slowo(self, slowo):
        self.slowa.append(slowo)
        self.zegar()
        self.zmniejsz_nude()


    def karm(self):
        self.zmniejsz_glod()
        self.zegar()












tobi = Tamagotchi("Tobi")
print(tobi)
print(tobi)
print(tobi)
print(tobi)
print(tobi)
print(tobi)
tobi. zmniejsz_nude()
print(tobi)
tobi.przywitaj_sie()
print(tobi)
print(tobi)
print(tobi)
print(tobi)
print(tobi)
tobi.karm()
print(tobi)
tobi.naucz_slowo(input("Podaj slowo do nauki:"))
tobi.przywitaj_sie()
print(tobi)







