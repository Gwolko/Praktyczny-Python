### 🔴 Budowanie listy od zera z .append()

# text = 'Lorem ipsum przykładowy tekst'
# words = text.split()
# print('words =', words)

# Jak dostać listę [5, 5, 11, 5] czyli długości słów?

# lengths = [len(words[0]), len(words[1]), len(words[2]), len(words[3])]
# print('lengths =', lengths)

# Potrzebujemy metody .append()

# my_list = [5, 10]
# print('my_list =', my_list)
# my_list.append(7)
# print('my_list =', my_list)
# my_list.append(3)
# print('my_list =', my_list)

# Bardzo często spotykany idiom:
# lengths = []
# for word in words:
#     word_length = len(word)
#     lengths.append(word_length)
# print('lengths =', lengths)

### 🔴 Ćwiczenie

# Popraw kod z M03L09 tak, aby wczytać wydatki do listy, a następnie wylicz sumę i średnią wydatków, a także jakiej kwoty był najmniejszy i największy wydatek. Użyj wbudowanych funkcji sum, min oraz max.


# EXPENSE_FILENAME = 'M03/expenses_ex.txt'  # Stała z nazwą pliku

# with open(EXPENSE_FILENAME) as stream:  # Otwieramy plik
#     content = stream.read()  # Czytamy zawartość pliku
# lines = content.split("\n")  # Dzielimy zawartość na linie
# total = 0  # Zmienna do sumowania wydatków
# expenses = []  # Lista do przechowywania wszystkich wydatków
# for line in lines:
#     tokens = line.split()  # Dzielimy linie na tokeny
#     if tokens:  # Sprawdzamy, czy linia nie jest pusta
#         expense = float(tokens[0])  # Konwertujemy pierwszy token na float
#         expenses.append(expense)  # Dodajemy wydatek do listy
#         total += expense  # Dodajemy do sumy
# # Wyświetlamy wyniki
# if expenses:  # Sprawdzamy, czy lista wydatków nie jest pusta
#     average_expense = total / len(expenses)  # Obliczamy średni wydatek
#     print('Suma wydatków:', total)
#     print('Najmniejszy wydatek:', min(expenses))
#     print('Największy wydatek:', max(expenses))
#     print('Średni wydatek:', average_expense)
# else:
#     print('Brak wydatków do analizy.')

# CWICZENIE Z SZKOLENIA
EXPENSE_FILENAME = 'M03/expenses_ex.txt'  # Stała z nazwą pliku

with open(EXPENSE_FILENAME) as stream:  # Otwieramy plik
    content = stream.read()  # Czytamy zawartość pliku
lines = content.split("\n")  # Dzielimy zawartość na linie
expenses = []  # Lista do przechowywania wszystkich wydatków
# Iterujemy przez każdą linię tekstu w liście lines. len(lines) zwraca liczbę elementów w liście lines.
# range(len(lines)) tworzy zakres indeksów, 
for i in range(len(lines)):
    tokens=lines[i].split()# Dzielimy tekst z lines[i] na listę słów lub wartości za pomocą metody split().
    if tokens:#Upewniamy się, że tokens nie jest pustą listą
        expense=float(tokens[0])#Pobieramy pierwszy element z tokens (tokens[0]) i konwertujemy go na liczbę zmiennoprzecinkową #(float).
        expenses.append(expense)#Dodanie wartości do listy
total =sum(expenses)
minimum=min(expenses)
maximum=max(expenses)
averge=total/len(expenses)
print('wszystkie wydatki wynoszą: ',total)
print('najnizszy wydatek: ', minimum)
print('maxymalny wydatek: ', maximum)
print('srednia wydatków to: ', averge)
