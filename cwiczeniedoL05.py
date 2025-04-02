# Pobranie tekstu od użytkownika
additional_text = input("Podaj tekst, który chcesz dodać: ")
# Pobranie nazwy pliku wejściowego od użytkownika
input_filename = input("Podaj nazwę pliku wejściowego: ")
# Otwarcie pliku wejściowego i odczytanie jego zawartości
with open(input_filename, encoding='utf-8') as stream:
    text = stream.read()  
# Wczytanie całej zawartości pliku
# Anonimizacja cyfr
for digit in "0123456789":
    text = text.replace(digit, "X")
# Dodanie tekstu użytkownika do zawartości pliku
text += "\n" + additional_text
# Pobranie nazwy pliku wyjściowego od użytkownika
output_filename = input("Podaj nazwę pliku wyjściowego (lub naciśnij Enter, aby wyświetlić tekst na ekranie): ")
# Jeżeli użytkownik nie podał nazwy pliku wyjściowego, wyświetlamy tekst na ekranie
if output_filename == "":
    print("Text po anonimizacji:\n")
    print(text)
else:
    # Sprawdzamy, czy plik wyjściowy już istnieje
    try:
        # Próbujemy otworzyć plik w trybie odczytu, aby sprawdzić, czy istnieje
        with open(output_filename, 'r', encoding='utf-8'):
            # Plik istnieje, zapytajmy użytkownika, czy chce dodać tekst
            decision = input(f"Plik {output_filename} już istnieje. Czy chcesz dodać tekst do pliku? (tak/nie): ")
            if decision.lower() == "tak":
                # Otwieramy plik w trybie dołączania ('a'), aby dodać tekst
                with open(output_filename, 'a', encoding='utf-8') as file:
                    file.write("\n" + text)  # Dodajemy nową linię, a następnie tekst
                print(f"Tekst został dodany do pliku {output_filename}.")
            else:
                print("Operacja anulowana. Plik nie został zmieniony.")
    except FileNotFoundError:
        # Plik nie istnieje, więc możemy go utworzyć i zapisać
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Zanonimizowany tekst został zapisany do nowego pliku {output_filename}.")


# ROZWIAZANIE Z LEKCJI
