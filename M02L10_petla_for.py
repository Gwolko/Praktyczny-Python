### 🔴 Powtarzam, powtarzam, powtarzam, powtarzam, powtarzam... Pętla for

# Znasz już rozgałęzienia warunkowe (IF) - ale co z powtarzaniem operacji dla każdego X? Np. dla każdego pliku, dla każdego znaku w napisie etc.

# Przykład
# text = "mój tekst"
# for char in text:
#     # przy pierwszym iteracji char = "m"
#     # przy drugiej iteracji char = "ó" itd.
#     print(char)

# Składnia: for zmienna in wyrażenie :
# for char in text:  # ✅ ok
# for char + 2 in text:  # ❌ źle
# for char in "mój tekst":  # ✅ ok
# for char in text.lower():  # ✅ ok
# for char in text.lower().replace(' ', '_') + "_sufix":  # ✅ ok
# for char in text  # ❌ brakujący dwukropek

# Nie po każdym obiekcie można ITEROWAĆ, czyli użyć w pętli for. Na ten moment są to tylko stringi.
# number = 1234
# for char in number:  # ==> TypeError: 'int' object is not iterable
#     print(char)

### 🔴 Ćwiczenie
# Napisz program, który prosi użytkownika o hasło, a następnie dla każdego znaku wyświetla jakiego typu jest to znak (litera vs cyfra vs biały znak vs znak specjalny).
## 🔴 Ćwiczenie
# haslo = input("Wprowadź HASŁO: ")

# Przejście przez każdy znak w haśle
# for char in haslo:
#     if char.isalpha():
#         print(f"{char}: litera")
#     # Sprawdza, czy jest liczbą
#     elif char.isdigit():
#         print(f"{char}: liczba")
#     # Sprawdza białe znaki (np. spacja, tabulator, nowa linia)
#     elif char.isspace():
#         print(f"{char}: biały znak")
#     else:
#         print(f"{char}: znak specjalny")

# password = input("Wprowadz Haslo:  ")
# for char in password:
#     if char.isalpha():
#         type_ = "litera"
#         # print(f"{char}: litera")
#     # Sprawdza, czy jest liczbą
#     elif char.isdigit():
#         type_ = "liczba"
#         # print(f"{char}: liczba")
#     # Sprawdza białe znaki (np. spacja, tabulator, nowa linia)
#     elif char.isspace():
#         type_ = "biały znak"
#         # print(f"{char}: biały znak")
#     else:
#         type_ = "znak specjalny"
#     print(char, type_)
#         # print(f"{char}: znak specjalny")
###################
# haslo = input("Wprowadź HASŁO: ")

# Przejście przez każdy znak w haśle
# for char in haslo:
#     if char.isalpha():
#         typ = "litera"
#     elif char.isdigit():
#         typ = "liczba"
#     elif char.isspace():
#         typ = "biały znak"
#     else:
#         typ = "znak specjalny"
    
#     # Jeden print dla wyświetlenia znaku i jego typu
#     print(f"{char}: {typ}")


    

## 🔴 Bonusowe minićwiczenia do zrobienia przed głównym ćwiczeniem:

# 1. Napisz program, który wyświetla w kolejnych liniach liczby 0, 1, 2, 3 itd. aż do 10. Użyj konstrukcji `for i in range(11)`.

# 2. Fizzbuzz. Rozwiń poprzedni program tak, aby jeżeli liczba jest podzielna przez 3 (co sprawdzisz warunkiem `i % 3 == 0`, czyli reszta z dzielenia przez 3 równa 0), to wypisz "fizz", a jeśli podzielna przez 5, to wypisz "buzz".
numeral =range(11) 
for numeral in numeral:
    if numeral % 3 ==0:
        print(f"liczba podzielna pzez 3")
    else:
        print(f"{numeral}")
        