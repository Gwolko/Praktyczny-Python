### 🔴 Stałe

# Stałe to specjalne zmienne, których wartości nie zamierzasz zmieniać i które mają "zahardcodowane" wartości.
# Odróżniamy je od zwykłych zmiennych używająć WIELKICH_LITER i umieszczając je na samym początku skryptu.
# Takie stałe to np. umieszczona w kodzie nazwa pliku.

# ✅ Dobrze

# EXPENSES_FILENAME = 'expenses.txt'

# with open(EXPENSES_FILENAME) as stream:
#     content = stream.read()

# # ❌ Źle

# with open('expenses.txt') as stream:
#     content = stream.read()

# Stałe są przez Pythona traktowane tak jak zwykłe zmienne - a więc dalej można je nadpisać.

# CONST = 50
# CONST = 80

# Jednak nie powinniśmy tak robić. WIELKIE_LITERY to pewna konwencja, czyli umowa między programistami.
    
### 🔴 Ćwiczenie

# Napisz program, który ocenia jak bardzo "naukowo" brzmi dany tekst. W tym celu policz jak często w tym zdaniu pojawiają się liczby. Wyświetl jaki procent wszystkich "słów" to właśnie liczby.
# Postaraj się, aby program nie zwracał uwagi na interpunkcję. To znaczy, że w zdaniu "Numer 1234." drugie słowo to "1234.". Potraktuj je jako liczbę, pomimo że zawiera kropkę.
# To oznacza, że zdefiniujesz stałą zawierającą kilka znaków interpunkcyjnych.
# Samodzielnie znajdź metodę do określania, czy dany string jest liczbą.



# Stała z podstawowymi znakami interpunkcyjnymi
# INTERPUNKCJA = ",.!?;:%"

# # Program główny
# text = input("Wprowadź tekst: ")
# # Usuwanie interpunkcji zamieniamy na spacje
# for znak in INTERPUNKCJA:
#     text = text.replace(znak, "")

# slowa = text.split()  # Dzielimy tekst na słowa

# # Filtrujemy liczby, sprawdzając, czy każde słowo składa się z cyfr lub jest w formacie zmiennoprzecinkowym
# # liczby = [slowo for slowo in slowa if (slowo.replace('.', '', 1).isdigit() and slowo.count('.') <= 1)]

# # liczby = [] #Tworzymy listę
# # for slowo in slowa:
# #     # Sprawdź, czy słowo zawiera co najwyżej jedną kropkę
# #     if slowo.count('.') <= 1:
# #         # Usuń jedną kropkę i sprawdź, czy pozostała część to cyfry
# #         if slowo.replace('.', '', 1).isdigit():
# #             liczby.append(slowo)
# liczby = []

# for slowo in slowa:
#     # Sprawdź, ile kropek znajduje się w słowie
#     ma_jedna_kropke = slowo.count('.') <= 1

#     # Usuń jedną kropkę (jeśli istnieje) i sprawdź, czy pozostały ciąg to cyfry
#     jest_liczba = slowo.replace('.', '', 1).isdigit()

#     # Jeśli oba warunki są spełnione, dodaj słowo do listy liczb
#     if ma_jedna_kropke and jest_liczba:
#         liczby.append(slowo)


# liczba_liczb = len(liczby)
# liczba_slow = len(slowa)
# procent = (liczba_liczb / liczba_slow) * 100 if liczba_slow > 0 else 0

# # Wyświetlanie wyników
# print(f"Liczba liczb w tekście: {liczba_liczb}")
# print(f"Liczba wszystkich słów w tekście: {liczba_slow}")
# print(f"Liczby stanowią {procent:.2f}% wszystkich słów.")

### 🔴 rozwizania z szkolenia
# Stała z podstawowymi znakami interpunkcyjnymi
INTERPUNKCJA = ",.!?;:%"
# Program główny
text = input("Wprowadź tekst: ")
# Usuwanie interpunkcji zamieniamy na spacje
for znak in INTERPUNKCJA:
    text = text.replace(znak, "")
numbers=0
slowa = text.split()  # Dzielimy tekst na słowa
for slowa in text:
    if slowa.isnumeric():
        numbers+=1 # że za każdym razem, gdy zostanie znalezione słowo będące liczbą (if slowo.isnumeric():), zmienna numbers jest zwiększana o 1.
naukowosc=100*numbers /len(slowa)
print (  naukowosc , '%' )
