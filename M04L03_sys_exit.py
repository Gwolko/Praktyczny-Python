### 🔴 Jak przedwcześnie zakończyć działanie programu?

# W tym celu wywołujemy sys.exit() przekazując kod zakończenia programu.

# import sys

# sys.exit(1)

# print("Ten kod nie wykona się nigdy")

# Ten kod jest liczbą od 0 do 255. Jest to informacja dla wiersza polecenia, czy program zakończyć się poprawnie, czy błędem.
# 0 = poprawnie
# Każda inna liczba - błąd. Między różnymi typami błędów można rozróżniać, np. 1 może oznaczać brak pliku, 2 może oznaczać brak uprawnień etc.
# Ten kod w praktyce znaczenie tylko, gdy będziesz pisać skrypty wiersza poleceń (.bat) lub skrypty shella/basha (.sh).

# Ten mechanizm zgłaszania błędów jest zupełnie niezależny od błędów/wyjątków w Pythonie!

# sys.exit wywołujemy tylko gdy zorientujemy się, że argumenty wiersza poleceń są niepoprawne, np. jest ich za mało, mają niepoprawny typ etc. We wszystkich pozostałych sytuacjach korzystamy ze standardowego mechanizmu błędów/wyjątków.

# Na MacOS oraz Linuxie kod błędu możesz sprawdzić w terminalu wpisując:
# $ echo $? 
# Na Windowsie trzeba wpisać w wierszu polecenia:
# echo %errorlevel%

### 🔴 Ćwiczenie

# Rozwiń program z poprzedniej lekcji tak, aby wyświetlał komunikat błędu, gdy użytkownik nie poda nazwy pliku. Wyświetl błąd także wtedy, gdy poda więcej niż jeden plik.

#🔴 rozwiazanie 1
# import sys

# if len(sys.argv) < 2:
#     print("Błąd: Nie podano nazwy pliku.")
#     sys.exit(1)
# elif len(sys.argv) > 2:
#     print("Błąd: Podano więcej niż jeden plik.")
#     sys.exit(1)

# filename = sys.argv[1]

# try:
#     with open(filename) as stream:
#         content = stream.read()
# except FileNotFoundError:
#     print(f"Błąd: Plik {filename} nie został znaleziony.")
#     sys.exit(1)

# lines = content.split('\n')
# lines_counter = len(lines)
# word_counter = len(content.split())
# characters_counter = len(content)

# print(f"\nLiczba znaków: {characters_counter}")
# print(f"Liczba słów: {word_counter}")
# print(f"Liczba linii: {lines_counter}")
# print(f"Nazwa pliku: {filename}")

#🔴 rozwiazanie sys.exit(1) - pierwsza wersja
import sys

if len(sys.argv) < 2:
    print("Błąd: Nie podano nazwy pliku.")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Błąd: Podano więcej niż jeden plik.")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename) as stream:
        content = stream.read()
except FileNotFoundError:
    print(f"Błąd: Plik {filename} nie został znaleziony.")
    sys.exit(1) #rozwiązanie z sys.exit

lines = content.split('\n')
lines_counter = len(lines)
word_counter = len(content.split())
characters_counter = len(content)

print(f"\nLiczba znaków: {characters_counter}")
print(f"Liczba słów: {word_counter}")
print(f"Liczba linii: {lines_counter}")
print(f"Nazwa pliku: {filename}")

#🔴 rozwiazanie sys.exit(1) - druga wersja
import sys

def main():
    """Główna funkcja programu."""
    if len(sys.argv) < 2:
        print("Błąd: Nie podano nazwy pliku.")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Błąd: Podano więcej niż jeden plik.")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename) as stream:
            content = stream.read()
            print(content)  # Dodano wyświetlanie zawartości pliku
    except FileNotFoundError:
        print(f"Błąd: Plik {filename} nie został znaleziony.")
        sys.exit(1)
    except PermissionError:
        print(f"Błąd: Brak uprawnień do odczytu pliku {filename}.")
        sys.exit(1)
    except Exception as e:
        print(f"Błąd: {e}")
        sys.exit(1)
# oddzielić kod, który ma być uruchamiany tylko wtedy, gdy skrypt jest uruchamiany bezpośrednio, od kodu, który może być wykorzystywany jako część innego modułu.
if __name__ == "__main__": 
    main()
lines = content.split('\n')
lines_counter = len(lines)
word_counter = len(content.split())
characters_counter = len(content)

print(f"\nLiczba znaków: {characters_counter}")
print(f"Liczba słów: {word_counter}")
print(f"Liczba linii: {lines_counter}")
print(f"Nazwa pliku: {filename}")