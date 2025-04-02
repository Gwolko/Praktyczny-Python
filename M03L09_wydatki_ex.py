# # ### 🔴 Jak pracować na pojedynczych elementach listy?
#
files = ['plik.txt', 'nowy.txt']
print('type(files) =', type(files))
print(files.upper())  # ❌ lista nie ma metody .upper() - mają ją jej poszczególne elementy

# # # Składnia  lista[index]  pozwala na wyciągnięcie konkretnego elementu. Elementy numerujemy od zera!
file = files[0]
print(file.upper())
# lub krócej:
print(files[0].upper())

# # Ujemny index oznacza weź n-ty element od końca:
print('Ostatni:', files[-1])

# # ### 🔴 Czy lista jest pusta?

# # Pusta lista to lista nie zawierająca żadnych elementów.
empty = []
#
# # # Możesz sprawdzić, czy jest pusta używając len():
if len(empty) == 0:
    print('pusta')

# # Ale preferowany jest poniższy zapis:
if empty:
    print("nie pusta")
else:
    print("pusta")
#
# Pusta lista jest falsy => wykonywany jest else.
# Każda inna lista jest truthy => wykonywany jest if.
    
### 🔴 Ćwiczenie

# Rozwiń program z M03L07. Tym razem format pliku jest następujący: każda linia to jeden wydatek. Najpierw jest kwota wydatku, a po spacji jego opis. Opis może zawierać kolejne spacje. Plik może zawierać puste linie. Przykładowy plik to expenses-ex.txt
# W tym ćwiczeniu nie wystarczy, aby skorzystać ze .split(), dlatego że ono dzieli nie tylko na poszczególne linie, ale także po spacjach w każdej linii. Tutaj konieczne jest dzielenie tylko po znakach nowej linii. Jak to zrobić? Da się to zrobić używając .split(), ale trzeba przekazać pewien parametr. Doczytaj w dokumentacji jak dokładnie to zrobić.
# Mając już pojedynczą linię konieczne będzie dalsze jej podzielenie już po spacjach, tak aby dostać się do kwoty wydatku, która jest na początku każdej linii.

### 🔴 rozwiazanie z lekcji
with open('M03/expenses_ex.txt') as stream:
    content = stream.read()
numbers = content.split(" ")
total=0
for line in numbers:
    total +=float(line)
print('suma wydatków: =' , total)

EXPENSE_FILENAME = 'M03/expenses_ex.txt' # tworzymy stała z nazwa pliku
with open('M03/expenses_ex.txt') as stream:#otwieramy plik,
    content = stream.read() #przypisujemy w zmiennej content streama
lines = content.split("\n")#tworzymy zmienna w której zapisujemy zm. content podzieloną na linie
total = 0 #tworzymy zmienna total
for line in lines:
#To pętla, która przechodzi przez każdy element w liście lines (lub jakimkolwiek innym obiekcie iterowalnym o nazwie lines).
# line to każda pojedyncza linia (element) z kolekcji lines.
    tokens=line.split()
#Dzieli każdą linię na listę słów lub wartości (zwanych "tokenami") na podstawie białych znaków (spacji, tabulatorów itp
    if tokens:
#Sprawdza, czy lista tokens nie jest pusta. Oznacza to, że linia nie była pusta i zawierała coś, co można podzielić.Jeśli # #tokens jest pusta (czyli linia była pusta), to kod wewnątrz bloku if nie zostanie wykonany.J
        expense=tokens[0]
#Przypisuje pierwszy element z listy tokens do zmiennej expense.
        total+=float(expense)
#Konwertuje expense (które jest typu string) na liczbę zmiennoprzecinkową (float) i dodaje tę wartość do zmiennej total.
print('suma wydatków: =', total)
