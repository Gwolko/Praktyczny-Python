### 🔴 Jak jeszcze można stworzyć listę? O pracy na stringach

# content = '1234 9878\n5678 3456'
# numbers = content.split()  # .split() dzieli po dowolnych białych znakach, zarówno po spacjach, znakach tabulacji jak i znakach nowych linii
# print('numbers =', numbers)
# print('type(numbers) =', type(numbers))
# numbers jest listą string'ów, nie int'ów!

### 🔴 Ćwiczenie

# # Otwarcie pliku z nazwą podaną przez użytkownika
# with open('expenses.txt', encoding='utf-8') as stream:
#     content = stream.read()  # Wczytanie całej zawartości pliku
#     print(content)

# # Iteracja po elementach pliku
# # content = text
# numbers = content.split()  # Podział tekstu na listę ciągów znaków
# print('numbers =', numbers)
# print('type(numbers) =', type(numbers))

# # Iteracja po numbers i zamiana na float
# for i in range(len(numbers)):
#     numbers[i] = float(numbers[i])  # Zamiana elementów na float
#     print(numbers)
# # numbers = [float(num) for num in numbers] stworzyć nową listę za pomocą list comprehension:

# # Obliczenie sumy
# suma_numbers = 0
# for number in numbers:
#     suma_numbers += number  # Dodawanie kolejnych liczb

# print("Suma wydatków:", suma_numbers)

#  otrzymuję bład!!! File "c:\Users\Użytkownik\Documents\praktyczny python\Praktyczny_Python_materialy-2022-08-23\M03\M03L07_split.py", line 12, in <module>      
#     with open('expenses.txt', encoding='utf-8') as stream:
#          ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'expenses.txt

### 🔴 rozwiazanie z lekcji
with open('M03/expenses.txt') as stream:
    content = stream.read()
numbers = content.split()
total=0
for line in numbers:
    total +=float(line)
print('suma wydatków: =' , total)




    