import glob
import os

NEW_EXTENSION = '.bak'

# Pobierz wzorzec pliku od użytkownika
pattern = input("Podaj szablon pliku (np. *.txt lub ./folder/*.txt): ")
filenames = glob.glob(pattern)

if not filenames:
    print("Nie znaleziono plików pasujących do wzorca.")
    exit()

operations = []

# Generowanie nowych nazw plików
for filename in filenames:
    if '.' in filename:
        name, extension = filename.rsplit('.', maxsplit=1)
    else:
        name = filename
        extension = ""
    new_filename = name + NEW_EXTENSION
    operations.append((filename, new_filename))  # Dodaj parę jako krotkę

# Wyświetlenie operacji do wykonania
print("\nZostaną dokonane następujące zmiany:")
for old, new in operations:
    print(f"{old} -> {new}")

# Potwierdzenie operacji
choice = input("\nCzy kontynuować zmianę nazw plików? [t/n]: ").lower()
if choice == "t":
    for old, new in operations:
        os.rename(old, new)
        print(f"Zmieniono: {old} -> {new}")
    print("Sukces :)")
else:
    print("Operacja anulowana.")
