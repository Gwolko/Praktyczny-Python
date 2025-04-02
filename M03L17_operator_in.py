### 🔴 Szukanie słów w zdaniu

# Wiesz już, że możesz sprawdzić obecność pojedynczego znaku w stringu:
filename = 'plik.txt'
if '.' in filename:
    print("Ma kropkę!")
    
# W ten sam sposób można sprawdzić występowanie całego podstringa:
pattern = "ma"
text = "Ala ma kota"
if pattern in text:
    print("Tak, tekst zawiera słowo 'ma'")

# Jednak tutaj tkwi pułapka:
pattern = "ma"
text = "Ala to mama"
if pattern in text:
    print("Tak, tekst zawiera słowo 'ma' (ups..., jednak nie)")
    
# Na szczęście operator in pozwala także na sprawdzenie, czy lista zawiera konkretny element:
words = ['ala', 'to', 'mama']
if 'ma' in words:
    print("Jest słowo 'ma'")
else:
    print("Nie ma słowa 'ma'")

if 'mama' in words:
    print("Jest słowo 'mama'")
    
### 🔴 Ćwiczenie

# Wczytaj listę komentarzy z pliku comments.txt. Każdy komentarz to osobna linia. Zapisz komentarze w zmiennej, pod którą kryje się lista list. Każdy komentarz reprezentuj jako listę słów, a nie jako string.
# Następnie pozwól użytkownikowi wprowadzić słowo i wyświetl w ilu komentarzach pojawia się to słowo?
# Wielkość liter nie powinna mieć znaczenia.
# Pozbądź się znaków interpunkcji.

# Na przykład:
# jest -> 3
# komen -> 0

## Otwieramy plik i wczytujemy linie z pliku
#with open('komentarze.txt', "r", encoding="utf-8") as stream:
with open(r"C:\Users\Użytkownik\Documents\praktyczny python\Praktyczny_Python\M03\komentarz.txt", "r", encoding="utf-8") as stream:
    lines = stream.readlines()
# Tworzymy listę list w bardziej rozbudowany sposób
comments_as_lists = []  # Pusta lista na komentarze jako listy słów
for line in lines:  #Iterujesz przez każdą linię wczytaną z pliku.
    stripped_line = line.strip()  # Usuwam zbędne znaki nowej linii (\n) oraz inne białe znaki na początku i końcu linii
    words = stripped_line.split()  # Dzielimy linijkę na słowa
    comments_as_lists.append(words)  # Dodajemy listę słów do głównej listy
# Wyświetlamy wynik
print(comments_as_lists)
