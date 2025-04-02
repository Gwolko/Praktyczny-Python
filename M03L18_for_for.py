### 🔴 Ćwiczenie

# Rozwiń program z poprzedniego ćwiczenia tak, aby użytkownik mógł podać kilka słów (rozdzielając je spacją). Program powinien zliczyć ile jest komentarzy, w których występuje którekolwiek z podanych słów.

# Na przykład:
# jest -> 3
# jest tego -> 4
# jest pliku -> 4


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
    #comments.append(line.lower().split())#Dodanie linii podzielonej na słowa (ponownie)


words = input("Wpisz szukane słowa (oddzielone spacją): ").lower().split()

# word = input('wpisz szukane słowo ')#Pobranie słowa do wyszukania od użytkownika
counter = 0#nicjalizacja licznika
for coment in comments:#Iteracja przez każdy komentarz w `comments
     if any(word in coment for word in words):  # Sprawdzenie, czy którekolwiek słowo jest w komentarzu
    #if word in comments:#Sprawdzenie, czy słowo jest w komentarzu
        counter+=1#Zwiększenie licznika, jeśli słowo jest znalezione
#print('slowo', words, 'pojawiło się' , counter, 'komentarzach')# Wydrukowanie wyniku
print('Przynajmniej jedno z podanych słów pojawiło się w', counter, 'komentarzach.')