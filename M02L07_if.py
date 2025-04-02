### 🔴 Mamy dwie możliwości, którą wybierasz?

# Znasz już typy str, int i float. Pora na bool!

character = "A"
isupper = character.isupper()
print(isupper)  # ==> True
print(type(isupper))  # ==> <class 'bool'>

# Nie ma kolizji nazewnictwa między metodą .isupper() a zmienną isupper.

# .isupper() sprawdza, czy WSZYSTKIE litery są wielkie - sprawdź w dokumentacji
text = "ASdf"
print(text.isupper())

# Są tylko dwie wartości typu bool: True oraz False.
print(True)
false_or_true = False

# ❌ Częsta pomyłka - False i True musi być z wielkiej litery, a nie z małej, inaczej Python traktuje to jako zmienną!
print(false)  # ==> NameError: name 'false' is not defined

# Najprostsze rozgałęzienie warunkowe - instrukcja IF.
# Składnia: if warunek :
text = "ASDF"
if text.isupper():  # dwukropek konieczny zawsze, gdy poniżej masz wcięty blok kodu
    print("Wszystkie litery wielkie!")  # wykona się (= zadziała)
    # Wcięcia to zawsze 4 spacje.

# WARUNKIEM if'a może być False/True, zmienna, wywołanie funkcji, metody, porównanie lub inne złożone tzw. WYRAŻENIE:    
# if True:  # ✅ ok
# if false_or_true:  # ✅ ok
# if len(text) == 0:  # równy  # ✅ ok
# if len(text) != 0:  # różny  # ✅ ok
# if 2 + len(text) == 5:  # ✅ ok
# if isupper = text.isupper():  # ❌ przypisanie nie może być w if'ie
# if len(text) = 0:  # ❌ częsty błąd - do porównywania służy podwójny znak równości (==), natomiast pojedynczy znak równości (=) służy do przypisania

# Co gdy warunek nie jest spełniony?
text = "asDF"
if text.isupper():
    print("Wszystkie litery wielkie!")  # nie wykona się (= nie zadziała)
    print("To również się nie wykona")
print("Ale to już zadziała")
    
# Instrukcja IF-ELSE
if text.isupper():
    print("Wszystkie litery wielkie!")
else:  # bez wcięcia, dwukropek
    print("Nie wszystkie litery wielkie!")
print("To zadziała zawsze")

### 🔴 Ćwiczenie
# Napisz program, który prosi o jeden, pojedynczy znak, a następnie sprawdza, czy jest to litera, czy coś innego. Ponownie, tak jak w jednym z poprzednich ćwiczeń, musisz znaleźć odpowiednią metodę, która sprawdza, czy dany napis to litera.
#### Rozwizanie 🔴 Ćwiczenia
# Prośba o jeden znak od użytkownika
znak = input("Podaj jeden znak: ")
# Sprawdzenie, czy jest to litera
# if len(znak) == 1 and znak.isalpha():
#     print("To jest litera.")
# else:
#     print("To nie jest litera.")
# .isalpha -Return True if the string is an alphabetic string, False otherwise.
# A string is alphabetic if all characters in the string are alphabetic and there
# is at least one character in the string.
char = input("Podaj jeden znak")
if len(char) == 1:
    if char.isalpha():
          print("to jest litera")
    else:
        print("to nie jest litera")
else:
     print("Należało podać znak")

