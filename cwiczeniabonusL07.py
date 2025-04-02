# 🔴 Ćwiczenie Napisz program, który zlicza ile jest słów w pliku tekstowym

# with open('M03/nowy2.txt',encoding='utf-8') as stream:
#     content = stream.read()
# words = content.split()
# print("Liczba wyrazów w pliku", 'nowy2.txt', "wynosi", len(words))

# 🔴 Ćwiczenie 2. Napisz program, który wczytuje z pliku słowaw, a następnie zapisuje w innym pliku tylko te słowa, które są samymi wielkimi literami.

# Definicja nazw plików:
# INPUT_FILENAME = 'input.txt' # INPUT_FILENAME to nazwa pliku wejściowego, z którego zostanie odczytana treść.
# OUTPUT_FILENAME = 'output.txt' # OUTPUT_FILENAME to nazwa pliku wyjściowego, do którego zostaną zapisane przetworzone dane.
# # Odczyt pliku wejściowego:
# with open(INPUT_FILENAME) as reader:
#     content = reader.read()
# #Otwiera plik input.txt w trybie odczytu, Odczytuje całą zawartość pliku do zmiennej content.
# #Przetwarzanie danych i zapis do pliku wyjściowego:
# with open(OUTPUT_FILENAME, 'w') as writer:
# #Otwiera plik output.txt w trybie zapisu ('w'). Jeśli plik nie istnieje, zostanie utworzony. Jeśli istnieje, jego zawartość zostanie nadpisana.
#     words = content.split()
#     for word in words:
#         if word.isupper():
#             writer.write(word + ' ')
#     #Pętla for word in words:Iteruje przez każde słowo z listy words.
#     # if word.isupper():Sprawdza, czy dane słowo składa się wyłącznie z wielkich liter (np. "HELLO", "WORLD").
#     # Jeśli tak, zapisuje je do pliku wyjściowego za pomocą writer.write(word + ' ').
#     # Dodaje spację po każdym zapisanym słowie.

# 🔴 Ćwiczenie Napisz program, który wczytuje z pliku liczby, a następnie zapisuje w innym pliku tylko te liczby, które są dodatnie.
# in_filename = 'numbers.txt'
# out_filename = 'filtered_numbers.txt'

# with open(in_filename, encoding='utf-8') as stream:
#     content = stream.read()
# liczby = content.split()
# with open(out_filename, 'w') as stream:
#     for liczba in liczby:
#         number = int(liczba)
#         if number > 0:
#             stream.write(str(number) + '\n')

in_filename = 'numbers.txt'
out_filename = 'filtered_numbers.txt'

# Otwieranie pliku wejściowego i odczyt zawartości
with open(in_filename, encoding='utf-8') as stream:
    content = stream.read()

# Dzielenie zawartości pliku na listę liczb (jako ciągi znaków)
liczby = content.split()

# Otwieranie pliku wyjściowego do zapisu
with open(out_filename, 'w') as stream:
    for liczba in liczby:
        # Konwersja ciągu znaków na liczbę całkowitą
        number = int(liczba)
        # Sprawdzanie, czy liczba jest dodatnia
        if number > 0:
            # Zapis liczby dodatniej do pliku wyjściowego
            stream.write(str(number) + '\n')

