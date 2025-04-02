### 🔴 Ćwiczenie

# Poniżej widzisz program, który wyświetla pierwszą linię wszystkich plików pasujących do wzorca podanego przez użytkownika.
# Zmodyfikuj ten program tak, aby najpierw wyświetlił listę wszystkich plików, następnie poprosił użytkownika o potwierdzenie, a dopiero potem wyświetlił po jednej linii z każdego z tych plików.

# import glob

pattern = input("Podaj pattern: ")
filenames = glob.glob(pattern)
for filename in filenames:
    with open(filename, 'r') as stream:
        content = stream.read()
        lines = content.split('\n')
        first_line = lines[0]
    print(filename, ':', first_line)

### 🔴modyfikacja

import glob

# Pobranie wzorca od użytkownika
pattern = input("Podaj pattern: ")

# Znalezienie plików pasujących do wzorca
filenames = glob.glob(pattern)

# Wyświetlenie listy plików
if filenames:
    print("Znalezione pliki:")
    for filename in filenames:
        print("-", filename)

# Prośba o Pobranie decyzji użytkownika:
choise= input("Czy chcesz wyświetlić pierwsze linie tych plików? [t/n]: ")
if choise.lower() == 't':#Porównanie odpowiedzi użytkownika:
    for filename in filenames:#Przetwarzanie każdego pliku:
        with open(filename, 'r') as stream:#Otwieranie i czytanie pliku:
            content = stream.read()#Odczyt zawartości pliku:
            lines = content.split('\n')#Podział zawartości na linie:
            first_line = lines[0]#Pobranie pierwszej linii:
            print(filename, "->", first_line)
    print('Sukses :)')    
else:
    print("Operacja anulowana.")

