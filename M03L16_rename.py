### 🔴 Ćwiczenie

# Rozwiń program z M03L121 tak, aby program najpierw wyświetlił jakie nastąpią zmiany plików, następnie poprosił użytkownika o potwierdzenie i dopiero potem dokonał zmiany nazw.
# W tym celu potrzebujesz listę zmian. Każda zmiana będzie dwuelementową listą zawierającą starą i nową nazwę pliku. Będziesz mieć do czynienie z listą list.

import glob
import os

NEW_EXTENSION = '.bak'

pattern = input("Podaj szablon pliku: ")  # Przykład: *.txt lub ./folder/*.txt
filenames = glob.glob(pattern) #moduł glob.metodaglob(wzorzec)
operations = []#tworzymu pustą listę

for filename in filenames:
        # Sprawdzanie, czy plik ma rozszerzenie
        if '.' in filename:
            tokens = filename.rsplit('.', maxsplit=1) #[0]  # dzieli ciąg od prawej strony przy użyciu separatora '.'
            # pobieramy pierwszy element listy, czyli fragment przed ostatnią kropką.
            name, extension = tokens #rozpakowanie elementów listy tokens na dwie zmienne: name (nazwa pliku) i extension (rozszerzenie).tzw unpacking
        else:
            name = filename  # Brak rozszerzenia
            extension=""
        new_filename = name + NEW_EXTENSION
        operation = [filename, new_filename]
        operations.append(operation)# Dodaj parę jako listę

print("Zostana dokonane następujace zmiany")
for old, new in operations: # operations jest iterowalnym obiektem, zawiera elementy, a każdy element ma dwie wartości old new 
     #Pierwsza wartość zostanie przypisana do zmiennej old druga do new
     print(old,"->",new)
#poniżej nie chcemy powtarzać generowania nazw plików - dlatego wyżej zapisalismy nowe nazwy + oryginalne w zmiennej 'operations'
choise=input("Czy kontynuować zmianę nazw plików?:  [t/n]: ")
if choise.lower()=="t":
    for old, new in operations:# unpacking w pętli
         os.rename(old,new)
         print(old, "->", new)
    print('Sukses :)')  # operacja zakończona sukcesem  
else:
    print("Operacja anulowana.")