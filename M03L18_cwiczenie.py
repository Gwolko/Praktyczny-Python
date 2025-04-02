# INPUT_FILE = 'M03/comments.txt'
# PUNCTUATIONS = '.,!?'

# with open(INPUT_FILE) as stream:
#     content = stream.read()

# lines = content.split('\n')
# comments = []  # Inicjalizacja listy `comments`

# for line in lines:  # Iteracja przez każdą linię w `lines`
#     line = line.lower()  # Konwersja linii na małe litery
#     for punc in PUNCTUATIONS:
#         line = line.replace(punc, ' ')  # Usuwanie znaków interpunkcyjnych
#     words = line.split()  # Podział linii na słowa
#     comments.append(words)  # Dodanie listy słów do `comments`

# # Pobranie słów do wyszukania od użytkownika
# words = input("Wpisz szukane słowa (oddzielone spacją): ").lower().split()

# # Licznik komentarzy zawierających przynajmniej jedno z podanych słów
# counter = 0
# for comment in comments:  # Iteracja przez każdy komentarz w `comments`
#     if any(word in comment for word in words):  # Sprawdzenie, czy którekolwiek słowo jest w komentarzu
#         counter += 1  # Zwiększenie licznika, jeśli któreś słowo jest znalezione

# print('Przynajmniej jedno z podanych słów pojawiło się w', counter, 'komentarzach.')

### ROZWIĄZANIE Z LEKCJI
INPUT_FILE = 'M03/comments.txt'
PUNCTUATIONS = '.,!?'

with open(INPUT_FILE) as stream:
    content = stream.read()

lines = content.split('\n')
comments = []  # Inicjalizacja listy `comments`

for line in lines:  # Iteracja przez każdą linię w `lines`
    line = line.lower()  # Konwersja linii na małe litery
    for punc in PUNCTUATIONS:
        line = line.replace(punc, ' ')  # Usuwanie znaków interpunkcyjnych
    words = line.split()  # Podział linii na słowa
    comments.append(words)  # Dodanie listy słów do `comments`

# Pobranie słów do wyszukania od użytkownika
words = input("Wpisz szukane słowa (oddzielone spacją): ").lower().split()

# Licznik komentarzy zawierających przynajmniej jedno z podanych słów
counter = 0
for coment in comments:
    exists = False
    for word in comments:
        exist=True
    if exists:
        counter +=1

print(counter, 'komentarzy zawiera przynajmniej jedno ze słow',end=' ' )
for word in words:
    print(word, end=" ")
print()
