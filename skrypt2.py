import math
import random

'''
#dzialania matematyczne
wartosc = 100
dodawanie = wartosc + 123.15
potega = dodawanie ** 12 #pojawil sie blad zmaina na 12 
tekst = str(potega)
wartosc_pi = math.pi
losowa = random.choice([1, 2, 3, 4, 5])
'''

'''
print("Wartość:", wartosc)
print("Dodawanie:", dodawanie)
print("Potęga:", potega)
print("Tekst:", tekst)
print("Wartość Pi:", wartosc_pi)
print("Losowa:", losowa)
'''

#lancuchy znakow
'''
tekst = f"Wartosc: {tekst}"
print("Długość tekstu:", len(tekst))
print("Część tekstu zawierająca 'art':", tekst[tekst.find("art"):])
print("Wartosc funkcji dir(tekst):", dir(tekst))
print("Tekst w wielkich literach:", tekst.upper())
tekst[2] = "p"
'''
#dzialania na listach
'''
# Zmienna tekst
tekst1 = "Wartosc"
# Rzutowanie na listę i przypisanie do zmiennej lista
lista = list(tekst1)
#Wykorzystując wycinki zrób tak, żeby lista zawierała jedynie litery słowa WARTOSC i później dwukropek
lista = list(tekst1) + [':']
print(lista)
'''
#listy skladane 
lista2 = [1, 2, 3, "banan", 100]
# przeiteruj po każdym wyrazie z listy, do nowej listy zapisz wartość podniesioną do potęgi 2, jeśli wartość jest równa "banan" to ją pomiń.
lista3 = [x**2 for x in lista2 if x != "banan"]
# co druga liczba od 2 do 16 
lista4 = list(range(2, 17, 2))
# Wydrukuj zmienne lista2, lista3 i lista4
'''
print("lista2:", lista2)
print("lista3:", lista3)
print("lista4:", lista4)
'''

'''
#slowniki 
#pusty słownik o nazwie ja
ja = {}
#Dodaj klucze reprezentujące Twoją osobę
ja["imie"] = "Bartosz"
ja["nazwisko"] = "Baran"
ja["wiek"] = 22
ja["rodzice"] = [{"imie": "Anna", "wiek": 55}, {"imie": "Tomasz", "wiek": 60}]
#Wypisz wartość klucza "rodzice"
print(ja["rodzice"])
#Wypisz jedynie imię pierwszego z rodziców
print(ja["rodzice"][0]["imie"])
#Wypisz wszystkie klucze słownika
print(ja.keys())
#Sprawdź czy słownik posiada klucz "rodzenstwo"
czy_ma_rodzenstwo = "rodzenstwo" in ja
print(czy_ma_rodzenstwo)
'''

#krotki
'''
krotka1 = (1, 2, "3", 4, 2, 5)
#Wypisz długość zmiennej i pierwszy wyraz
print("Długość krotki:", len(krotka1))
print("Pierwszy wyraz krotki:", krotka1[0])

#Sprawdź, ile razy występuje wartość 2 i wypisz
ile_razy_wystepuje_2 = krotka1.count(2)
print("Liczba wystąpień wartości 2:", ile_razy_wystepuje_2)

#Spróbuj zmienić pierwszy wyraz na wartość 2
#krotka1[0] = 2
'''

#zbiory 
'''
X = set("kalarepa")
Y = set("lepy")

# Krok 26: Wyświetl część wspólną obu zbiorów
print("Część wspólna zbiorów X i Y:", X.intersection(Y))
'''

#Instrukcje 
#1Napisz program, który iteruje przez listę imion używając pętli for oraz funkcji enumerate(), aby wyświetlić indeks każdego imienia wraz z samym imieniem
# Lista imion
'''
imiona = ["Anna", "Tomasz", "Karolina", "Piotr"]
for indeks, imie in enumerate(imiona):
    print("Indeks:", indeks, "Imię:", imie)
'''

#Stwórz przykłady dla testów if:
'''
#a. Gdzie wystąpią dwa warunki - napisz program sprawdzający czy dana liczba jest dodatnia i parzysta. Jeśli tak, program powinien wydrukować "Liczba jest dodatnia i parzysta".
liczba = int(input("Podaj liczbę: "))

if liczba > 0 and liczba % 2 == 0:
    print("Liczba jest dodatnia i parzysta")
else :
    print("Liczba nie jest dodatnia i parzysta")

#b. Gdzie wykorzystane zostanie zaprzeczenie not lub =! - napisz program, który sprawdza, czy wprowadzona przez użytkownika liczba nie jest równa zero. Jeśli nie jest, wydrukuj "Liczba jest różna od zera".
liczba = float(input("Podaj liczbę: "))

if liczba != 0:
    print("Liczba jest różna od zera")
else :
    print("Liczba równa zero")
#c. Gdzie wykorzystane będzie słowo in - napisz program, który sprawdza, czy wprowadzony przez użytkownika owoc znajduje się na liście dostępnych owoców (np. ['jabłko', 'banan', 'pomarańcza']). Jeśli tak, program powinien wydrukować "Owoc jest dostępny".
owoc = input("Podaj nazwę owocu: ")
dostepne_owoce = ['jabłko', 'banan', 'pomarańcza']

if owoc in dostepne_owoce:
    print("Owoc jest dostępny")
else : 
    print("Owoc nie jest dostępny")

    '''

#Stwórz przykład z pętlą while - Stwórz program, który będzie ciągle prosił użytkownika o wprowadzenie liczby. Program powinien 
#sumować wprowadzone liczby i kończyć działanie, gdy suma przekroczy 100. Po zakończeniu pętli, program powinien wydrukować sumę 
#wprowadzonych liczb
'''
suma = 0
while suma <= 100:
    liczba = float(input("Podaj liczbę: "))
    suma += liczba

print("Suma wprowadzonych liczb przekroczyła 100.")
print("Suma wprowadzonych liczb wynosi:", suma)
'''

#“Dziwactwa”
#w tych przypadkach, zapoznaj się z kodem, wyzwól go i zastanów się co się dzieje>
#1. Przypisanie tworzy referencje, a nie kopie
'''
L = [1,2,3,4]
M = [1,2,3,L,4]
print(f"Wartość zmiennej M przed zmianą L: {M}")
L[1] = "woooow"
print(f"Wartość zmiennej M po zmianie L: {M}")
'''
#2. Powtórzenie dodaje jeden poziom zagłębienia
'''
L = [4,5,6]
X = L * 4
Y = [L] * 4
print(f"X: {X}, Y: {Y}")
L[1] = "wow"
print(f"X: {X}, Y: {Y}")
L = [4,5,6]
Y = [list(L)] * 4
L[1] = "wow"
print(f"Y: {Y}")
Y[0][1] = "wow"
print(f"Y: {Y}")
'''
#Zadanie 1
'''
Wczytaj jako słownik plik z rozszerzeniem JSON (przydatny może okazać się pakiet json). Zapisz do 
zmiennej połączone wszystkie teksty z pliku. Zmodyfikuj następująco ten tekst:
- Zamień wszystkie duże litery na małe,
- Podziel go na wyrazy - będzie to najprawdopodobniej lista,
- Usuń znaki interpunkcyjne – w tekście występują jedynie kropki i przecinki,
- Zmodyfikuj tak każdy wyraz, żeby w każdym ostatni znak był w formacie dużej litery np. 
wyraz KozA,
- Z listy usuń wyrazy, które nie posiadają w sobie znaku a lub A - można wykorzystać składnię 
list składanych,
- Stwórz zmienną, które będzie przechowywać wszystkie unikatowe wyrazy - można 
wykorzystać zbiory,
- Stwórz zmienną, która będzie przetrzymywać ilość wystąpień dla każdego ze słów 
występujących w tekście - można wykorzystać słowniki.
Zapisz stworzone zmienne do pliku JSON, wartości kluczy wybierz samodzielnie
'''
import json
import string

# Wczytanie pliku JSON
with open("teksty.json", "r") as file:
    data = json.load(file)

# Połączenie wszystkich tekstów z pliku
polaczony_tekst = ''
for tekst in data["teksty"]:
    for key, value in tekst.items():
        polaczony_tekst += value

# Zamiana dużych liter na małe
polaczony_tekst = polaczony_tekst.lower()

# Usunięcie znaków interpunkcyjnych
polaczony_tekst = polaczony_tekst.translate(str.maketrans('', '', string.punctuation))

# Podzielenie tekstu na wyrazy
wyrazy = polaczony_tekst.split()

# Modyfikacja każdego wyrazu
wyrazy_modyfikowane = [wyraz[:-1] + wyraz[-1].upper() for wyraz in wyrazy]

# Usunięcie wyrazów, które nie zawierają litery 'a' lub 'A'
wyrazy_filtrowane = [wyraz for wyraz in wyrazy_modyfikowane if 'a' in wyraz or 'A' in wyraz]

# Utworzenie zbioru unikatowych wyrazów
unikatowe_wyrazy = set(wyrazy_filtrowane)

# Utworzenie słownika z ilością wystąpień dla każdego wyrazu
ilosc_wystapien = {wyraz: wyrazy_filtrowane.count(wyraz) for wyraz in unikatowe_wyrazy}

# Zapisanie stworzonych zmiennych do pliku JSON
with open("wyniki.json", "w") as file:
    json.dump({
        "polaczony_tekst": polaczony_tekst,
        "wyrazy_modyfikowane": wyrazy_modyfikowane,
        "wyrazy_filtrowane": wyrazy_filtrowane,
        "unikatowe_wyrazy": list(unikatowe_wyrazy),
        "ilosc_wystapien": ilosc_wystapien
    }, file, indent=4)