# Prosty kalkulator dodawania dwóch liczb
# Pobranie pierwszej liczby od użytkownika

# print("Kalkulator")
# first = input("podaj pierwsza liczbe: ")
# second = input("podaj druga liczbe: ")
# lepsze rozwiazanie
# first = float(input("podaj pierwsza liczbe: "))
# second = float(input("podaj druga liczbe: "))
# first = float(first)
# second = float(second)
# suma = (first + second)
# print("Wynik dodawania to:", suma)

# Błąd poprawiony
# division = 2 / 5
# print(division)

# = 2 =Błąd poprawiony
# variable = 1234
# print(variable)
     
# = 3 = Błąd poprawiony
x = "asdf"      
print( type(x))

# = 4 = Błąd poprawiony
# sum_ = 2 + 5
# print(sum_)

# = 5 = Błąd poprawiony
# number = input("Podaj liczbę: ")
# # int(number)
# print("Ta liczba ma", len(number), "cyfr.")


### Rozwizanie L07
# Prośba o jeden znak od użytkownika
# znak = input("Podaj jeden znak: ")
# Sprawdzenie, czy jest to litera
# if len(znak) == 1 and znak.isalpha():
#     print("To jest litera.")
# else:
#     print("To nie jest litera.")
### Rozdział L08
# char = input("Podaj jeden znak: ")
# if len(char) == 1:
#     if char.isalpha():
#           print("to jest litera")
#     else:
#         print("to nie jest litera")
# else:
#      print("Należało podać znak")

### 🔴 Ćwiczenie
# Napisz program, który prosi o jeden, pojedynczy znak, a następnie wyświetla, czy jest to liczba, litera, biały znak czy znak specjalny.
# Białe znaki to spacja, tabulacja i nowa linia.

# char = input("wprowadz jakiś znak: ")
# if len(char) != 1:
#         print("Proszę podać dokładnie jeden znak.")
# Sprawdź, czy znak jest literą
# if char.isalpha():
#     print("Wpisano literę: ")
# # sprawdza czy jest liczbą
# elif char.isdigit():
#         print("To jest liczba.")
# # sprawdza białe znaki
# elif char in (" ","\t", "\n"):
#     print("to jest biały znak: ")
### 🔴 Ćwiczenie 1a
# Napisz kalkulator BMI. Użytkownik podaje wagę i wzrost, a program wyświetla wynik wraz z komentarzem. BMI jest liczone jako waga podzielona przez wzrost w metrach do kwadratu. Jeśli BMI jest między 18.5 a 25, to napisz, że jest ono w normie. W przeciwnym razie napisz, że jest to niedowaga lub nadwaga, a dla BMI > 30 otyłość.
### 🔴 Ćwiczenie 1b
# Kalkulator wieku psa. Napisz program, który na podstawie wieku psa podanego przez użytkownika wyliczy jego wiek w latach ludzkich. Pierwsze dwa lata życia psa zawsze odpowiadają ok. 10,5 ludzkich lat (1 psi rok = 10.5 ludzkich lat, 2 psie lata = 21 ludzkich lat), a każdy kolejny rok życia psa to ok. 4 ludzkie lata.

### 🔴Cwiczenie 1a
# Napisz kalkulator BMI. Użytkownik podaje wagę i wzrost, a program wyświetla wynik wraz z komentarzem. BMI jest liczone jako waga podzielona przez wzrost w metrach do kwadratu. Jeśli BMI jest między 18.5 a 25, to napisz, że jest ono w normie. W przeciwnym razie napisz, że jest to niedowaga lub nadwaga, a dla BMI > 30 otyłość.
# Pobierz wagę i wzrost od użytkownika
# weight = float(input("Podaj swoją wagę w kilogramach: "))
# height = float(input("Podaj swój wzrost w metrach: "))
# Oblicz BMI
# BMI = weight/(height**2)
# # Wyświetl wynik BMI z komentarzem
# print(f"Twoje BMI wynosi: {BMI:.2f}")
# # Określ kategorię BMI
# if 18.5 <= BMI < 25:
#     print("Twoje BMI jest w normie.")
# elif BMI < 18.5:
#     print("Masz niedowagę.")
# elif 25 <= BMI <= 30:
#     print("Masz nadwagę.")
# else:
#     print("Masz otyłość.")

### 🔴 Cwiczenie 1b
# kalkulator wieku psa. Napisz program, który na podstawie wieku psa podanego przez użytkownika wyliczy jego wiek w latach ludzkich. Pierwsze dwa lata życia psa zawsze odpowiadają ok. 10,5 ludzkich lat (1 psi rok = 10.5 ludzkich lat, 2 psie lata = 21 ludzkich lat), a każdy kolejny rok życia psa to ok. 4 ludzkie lata.

# # dog_age_to_human_years()
#  # Pobierz wiek psa od użytkownika
# dog_age = int(input("Podaj wiek psa w latach: "))
# # Sprawdź, czy wiek jest dodatni
# if dog_age <= 0:
#     print("Wiek psa musi być większy niż zero. Nie masz psa!!!!")
# # Oblicz wiek w latach ludzkich
# if dog_age == 1:
#     human_age = 10.5
# elif dog_age == 2:
#     human_age = 21
# else:
# # Pierwsze dwa lata to 21 ludzkich lat, każdy kolejny rok to 4 ludzkie lata
#     human_age = 21 + (dog_age - 2) * 4
# #Wyświetl wynik
#     print(f"Wiek psa w latach ludzkich wynosi: {human_age:.1f}")

# char = input("wprowadz jakiś znak: ")
# if len(char) != 1:
#         print("Proszę podać dokładnie jeden znak.")
# # Sprawdź, czy znak jest literą
# if char.isalpha():
#     print("Wpisano jeden znak - literę: ")
# # sprawdza czy jest liczbą
# elif char.isdigit():
#         print("To jest liczba.")
# # sprawdza białe znaki
# # elif char in (" ","\t", "\n"):
# #     print("to jest biały znak: ")
# elif char.isspace():
#     print("to jest biały znak: ")
### 🔴 Ćwiczenie
# haslo = input("wprowadz HASŁO: ")
# char = haslo
# typ_znaku = char
# for char in haslo:
#   if char.isalpha():
#     print("char litera: ")
# # sprawdza czy jest liczbą
#   elif char.isdigit():
#     print("char: , liczba.")
# # sprawdza białe znaki
# # elif char in (" ","\t", "\n"):
# #     print("char, to jest biały znak: ")
#   elif char.isspace():
#     print("char: , biały znak: ") 
#   else: 
#     print("char: to jest znak specjalny")
## 🔴 Ćwiczenie      
haslo = input("Wprowadź HASŁO: ")

# Przejście przez każdy znak w haśle
for char in haslo:
    if char.isalpha():
        print(f"{char}: litera")
    # Sprawdza, czy jest liczbą
    elif char.isdigit():
        print(f"{char}: liczba")
    # Sprawdza białe znaki (np. spacja, tabulator, nowa linia)
    elif char.isspace():
        print(f"{char}: biały znak")
    else:
        print(f"{char}: znak specjalny")

# text = input("podaj tekst  ")
# for digit in "0123456789":
#     text = text.replace(digit, "X")
# print("Zmodyfikowany tekst: " , text)