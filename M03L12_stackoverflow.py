### 🔴 Gdzie szukać informacji?

# W pierwszej kolejności to, co można znaleźć bezpośrednio w Visual Studio Code:
# 1. dokumentacja poszczególnych funkcji i metod
# 2. listowanie dostępnych funkcji i metod 

# W dalszej kolejności:
# 1. Jeżeli interesuje Cię lista i dokumentacja poszczególnych funkcji i metod ze standardowej biblioteki => oficjalna dokumentacja Pythona, sekcja "Library Reference". Albo prościej: Google "Python + nazwa_biblioteki" (to działa także dla third-party libraries)
# 2. Jeżeli interesuje Cię rozwiązanie typowego problemu => Google i w szczególności StackOverflow

### 🔴 Ćwiczenie

# Poszukaj w Google i w szczególności na StackOverflow jak w Pythonie zmienić nazwę pliku.
# Rozwiń program z poprzedniego ćwiczenia tak, aby faktycznie zmieniał nazwę pliku.


import glob
import os
NEW_EXTENSION = '.bak'
pattern = input("Podaj szablon pliku: ")  # Przykład: *.txt lub ./folder/*.txt
filenames = glob.glob(pattern)

if not filenames:
    print("Nie znaleziono plików pasujących do wzorca:", pattern)
else:
    for filename in filenames:
        # Sprawdzanie, czy plik ma rozszerzenie
        if '.' in filename:
            name = filename.rsplit('.', maxsplit=1)[0]  # Nazwa pliku bez ostatniego rozszerzenia
        else:
            name = filename  # Brak rozszerzenia

        new_filename = name + NEW_EXTENSION
        os.rename(filename,new_filename)
        print(filename, "->", new_filename)