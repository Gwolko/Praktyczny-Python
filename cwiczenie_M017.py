# INPUT_FILE='M03/komentarze.txt'
# PUNCTUATIONS='.,!?'vv                                                          
# with open('komentarze.txt', "r", encoding="utf-8") as stream:
#     lines = stream.readlines()

# # Sprawdzenie, czy plik jest pusty
# if not lines:  # Jeśli `lines` jest pustą listą
#     print("Plik 'komentarze.txt' jest pusty. Dodaj komentarze i spróbuj ponownie.")
#     exit()  # Kończy działanie programu

# # Tworzymy listę list w bardziej rozbudowany sposób
# comments_as_lists = []  # Pusta lista na komentarze jako listy słów
# for line in lines:  # Iterujesz przez każdą linię wczytaną z pliku
#     stripped_line = line.strip()  # Usuwam zbędne znaki nowej linii (\n) oraz inne białe znaki na początku i końcu linii
#     words = stripped_line.split()  # Dzielimy linijkę na słowa
#     comments_as_lists.append(words)  # Dodajemy listę słów do głównej listy

# # Wyświetlamy wynik
# print(comments_as_lists)

# word = input("Podaj słowo: ").lower  # Pobierz słowo od użytkownika

# count = 0  # Licznik komentarzy zawierających dane słowo
# for comment in comments_as_lists:
#     if word in comment:  # Sprawdź, czy słowo jest w komentarzu
#         count += 1

# if count > 0:
#     print(f"Słowo '{word}' występuje w {count} komentarzach.")
# else:
#     print(f"Słowo '{word}' nie występuje w żadnym komentarzu.")

#rozwiązanie z lekcji
INPUT_FILE='M03/comments.txt'
PUNCTUATIONS='.,!?'

with open(INPUT_FILE) as stream:
    content = stream.read()

lines=content.split('\n')
comments=[]#Inicjalizacja listy `comments
for line in lines:#Iteracja przez każdą linię w `lines
    line = line.lower()#Konwersja linii na małe litery
    for punc in PUNCTUATIONS:
        line = line.replace(punc,' ')#Usuwanie znaków interpunkcyjnych
    words = line.split()#Podział linii na słowa
    comments.append(words)#Dodanie listy słów do `comments
    comments.append(line.lower().split())#Dodanie linii podzielonej na słowa (ponownie)
word = input('wpisz szukane słowo ')#Pobranie słowa do wyszukania od użytkownika
counter = 0#nicjalizacja licznika
for coment in comments:#Iteracja przez każdy komentarz w `comments
    if word in comments:#Sprawdzenie, czy słowo jest w komentarzu
        counter+=1#Zwiększenie licznika, jeśli słowo jest znalezione
print('slowo', word, 'pojawiło się' , counter, 'komentarzach')# Wydrukowanie wyniku