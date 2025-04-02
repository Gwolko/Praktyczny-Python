### 🔴 Co gdy potrzebujesz przechować wiele danych?

# Listy to najczęściej wykorzystywany sposób na zebranie wielu danych w jedną całość, np. wiele plików pod jedną zmienną.
# Inne opcje to: słowniki (dict), zbiory (set), krotki (tuple), a także własne klasy.

### 🔴 Tworzenie listy
files = ['plik.txt', 'nowy.txt']
print('files =', files)

phones = [123456789, 3746736473]
print('phones =', phones)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # listy można zagnieżdżać
print('list_of_lists =', list_of_lists)

mixed = [1, 'plik.txt', ['nested', True]]  # w ramach listy można mieszać obiekty różnych typów, chociaż rzadko ma to praktyczne zastosowanie
print(mixed)

# ✅ Używaj liczby mnogiej w nazwach zmiennych, pod którymi kryją się listy.

### 🔴 Pętla for

print("Numery telefonów:")
for phone in phones:
    print('-', phone)

### 🔴 Ćwiczenie

# Napisz program, w którym definiujesz listę wydatków (w postaci listy liczb), a następnie wyświetlasz ile wyniosły Cię wszystkie wydatki razem.

# tworzeni listy wydatków
expenses = [120.20, 500.00, 6.00, 12000.00, 453.00 ]
print('expenses =', expenses)
# #worzymy zmienną i ustawiamy wartosc początkową na 0
sum_expenses=0
# # używamy pętli for do zsumowania wydatków
for expens in expenses:
    sum_expenses += expens
print("Suma wydatków: ",  sum_expenses)

# Inna wersja
wydatki = [100, 50, 75, 200, 30]  # przykładowa lista wydatków
suma_wydatków = 0  # zmienna do przechowywania sumy
# Pętla for, która przechodzi przez każdy wydatek w liście i dodaje go do sumy
for wydatek in wydatki:
    suma_wydatków += wydatek

print("Suma wydatków:", suma_wydatków)

