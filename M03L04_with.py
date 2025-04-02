### 🔴 Jak jeszcze prościej otwierać pliki?

# Dotychczasowa wersja
# stream = open('plik.txt')
# content = stream.read()
# stream.close()
# print(content)

# Nowa wersja z użyciem tzw. menadżera kontekstu (instrukcja with).
# with open('plik.txt') as stream:  # oznacza PRAWIE to samo co stream = open('plik.txt')
#     content = stream.read()
#     # implicit stream.close()
# print(content)

### 🔴 Ćwiczenie poprawiony kod z with

# Popraw kod z poprzedniego ćwiczenia tak, aby użyć instrukcji with.
# plik=input("Podaj nazwę pliku:")
# with open('plik.txt', encoding='utf-8') as stream:  # oznacza PRAWIE to samo co stream = open('plik.txt')
#     content = stream.read()
#     # implicit stream.close()
# # print(content)
# wynik = ""
# for znak in content:
#     if znak.isdigit():  # Sprawdza, czy znak jest cyfrą
#         wynik += "X"
#     else:
#         wynik += znak
# print(wynik)



### 🔴 Rozwiązanie z kursu

# filename=input('Podaj nazwę pliku:  ')
# with open('plik.txt', encoding='utf-8') as stream:  # oznacza PRAWIE to samo co stream = open('plik.txt')
#     text = stream.read()
#     # implicit stream.close()
# # cała reszta nie potrzebuje wciecia
# for digit in "0123456789":
#     text = text.replace(digit, "X")
# print('text po anonimizacji: ')
# print()
# print('wynik')

# filename = input('Podaj nazwę pliku: ')

# # try:
#     # Otwarcie pliku z nazwą podaną przez użytkownika
#     with open(filename, encoding='utf-8') as stream:
#         text = stream.read()  # Wczytanie całej zawartości pliku
#
#     # Anonimizacja cyfr
#     for digit in "0123456789":
#         text = text.replace(digit, "X")
#
#     print('Text po anonimizacji:\n')
#     print(text)
# # except FileNotFoundError:
#     print(f'Błąd: Plik o nazwie "{filename}" nie istnieje.')
# # except Exception as e:
#     print(f'Wystąpił nieoczekiwany błąd: {e}')

filename = input('Podaj nazwę pliku: ')

# Otwarcie pliku z nazwą podaną przez użytkownika
with open(filename, encoding='utf-8') as stream:
    text = stream.read()  # Wczytanie całej zawartości pliku

# Anonimizacja cyfr
for digit in "0123456789":
    text = text.replace(digit, "X")

print('Text po anonimizacji:\n')
print(text)

