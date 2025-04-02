### 🔴 Jakie przewagi mają skrypty uruchamiane z linii poleceń?

# Zazwyczaj nasz program potrzebuje danych wejściowych, takich jak tekst, liczby czy pliki, na których ma pracować nasz program. Do tej pory pytaliśmy o nie użytkownika przy pomocy funkcji input(). To podejście na dłuższą metę jest niewygodne, bo wymaga za każdym razem ręcznego podawania tych danych.

# Jest lepszy sposób, dzięki któremu można to zautomatyzować. Takie dane podamy w terminalu (= wierszu polecenia), w tej samej linii, w której określamy nazwę skryptu. Te dane będziemy teraz nazywać ARGUMENTAMI WIERSZA POLECEŃ. Przykładowe uruchomienie tego skryptu w terminalu:

# $ python M04/M04L02_sys_argv.py nazwa_pewnego_pliku.txt 1234 "tekst i nazwy plików zawierające spacje muszą być w cudzysłowach"

# Jednak jak można odczytać te argumenty w programie?

# import sys

# print('sys.argv =', sys.argv)
# print()

# for el in sys.argv:
#     print(type(el), el)

# Zwróć uwagę, że napisy możemy przekazywać także bez cudzysłowów jeśli tylko nie zawierają spacji. 

# sys.argv to lista stringów, nawet jeśli któryś argument jest liczbą! Trzeba ręcznie konwertować!

# sys.argv jako pierwszy element zawiera nazwę skryptu, a dopiero potem trzy argumenty!

### 🔴 Ćwiczenie

# Napisz program, który otwiera wskazany przez użytkownika plik (wskazany jako argument linii poleceń, a nie przez input()) i zlicza ile jest w nim znaków, słów i linii.
# import sys

# filepath = r"C:\Users\Użytkownik\Documents\praktyczny python\Praktyczny_Python\M04\another.txt"

# try:
#     # Otwieranie pliku i przypisanie zawartości do zmiennej
#     with open(filepath, "r", encoding="utf-8") as file:
#         content = file.read()  # Wczytaj całą zawartość pliku do zmiennej
    
#     # Liczenie znaków, słów i linii
#     chars = len(content)  # Liczba wszystkich znaków w pliku
#     words = len(content.split())  # Liczba słów (podział po białych znakach)
#     lines = content.splitlines()  # Lista linii w pliku
    
#     # Wyświetlanie zawartości pliku z numeracją linii
#     for i, line in enumerate(lines, start=1):  
#     # Enumeracja z numeracją od 1 - iterowanie po liniach z jednoczesnym przypisaniem numeru linii.
#         print(f"Linia {i}: {line}")

#     # Wyświetlenie wyników
#     print(f"\nLiczba znaków: {chars}")
#     print(f"Liczba słów: {words}")
#     print(f"Liczba linii: {len(lines)}")
    
# except FileNotFoundError:
#     print("Plik nie istnieje. Sprawdź ścieżkę.")
# except PermissionError:
#     print("Brak uprawnień do odczytu pliku.")
# except Exception as e:
#print(f"Wystąpił nieoczekiwany błąd: {e}")

##########################
import sys
import re

if len(sys.argv) < 2:
    print("Użycie: python skrypt.py nazwa_pliku")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r', encoding='utf-8') as stream:
        content = stream.read()
except FileNotFoundError:
    print(f"Nie znaleziono pliku: {filename}")
    sys.exit(1)

lines = content.split('\n')
lines_counter = len(lines)
words = re.findall(r'\w+', content)
word_counter = len(words)
characters_counter = len(content)

print(f"\nLiczba znaków: {characters_counter}")
print(f"Liczba słów: {word_counter}")
print(f"Liczba linii: {lines_counter}")
print(f"Nazwa pliku: {filename}")
