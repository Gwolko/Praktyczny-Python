### 🔴 Rozpakowywanie list

line = '123,Jan,Kowalski'
columns = line.split(',')
print('columns =', columns)

# Ręczne rozpakowanie listy do kilku zmiennych:
id_ = columns[0]
first_name = columns[1]
last_name = columns[2]

# Automatyczne rozpakowanie:
id_, first_name, last_name = columns

# Jeśli jest za mało elementów, to dostaniesz błąd.
two_elements = ['X', 'Y']
# a, b, c = two_elements  # ==> ValueError: not enough values to unpack (expected 3, got 2)

# Jeśli za dużo elementów, to też dostaniesz błąd.
four_elements = ['X', 'Y', 'Z', 'T']
# a, b, c = four_elements  # ==> ValueError: too many values to unpack (expected 3)

# Z unpackingu możesz korzystać także w pętli for:
list_of_lists = [
    ['plik.txt', 'plik.bak'],
    ['inny plik.csv', 'inny plik.bak'],
    ['jeszcze inny.txt', 'jeszcze inny.bak'],
]

for item in list_of_lists:
    print(item)
    old, new = item
    print(old, '->', new)

for old, new in list_of_lists:
    print(old, '->', new)

### 🔴 Ćwiczenie

# Popraw kod z M03L12 tak, aby wykorzystać unpacking.

# Podpowiedź: w Twoim programie wykorzystujesz metodę `split()`, aby podzielić nazwę pliku na dwie części: nazwę i rozszerzenie. Przypisz te dwie informacje do dwóch osobnych zmiennych w JEDNEJ linii.
import glob
import os
NEW_EXTENSION = '.bak'
pattern = input("Podaj szablon pliku: ")  # Przykład: *.txt lub ./folder/*.txt M03/*.old
filenames = glob.glob(pattern)

for filename in filenames:
        if '.' in filename:
            tokens = filename.rsplit('.',maxsplit=1)
            name, extension = tokens # stosujemy unpacking
        else:
            name = filename  # Brak rozszerzenia
            extension =''
            name, extension = [filename,''] #też wporządku

        new_filename = name + NEW_EXTENSION
        os.rename(filename,new_filename)
        print(filename, "->", new_filename)