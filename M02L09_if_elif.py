### 🔴 Kierowniku, wszystko może się wydarzyć, i co teraz?

# Instrukcja IF-ELIF-...-ELIF
command = input("Polecenie: ")  
if command == "help":
    print("Wyświetlam pomoc!")
elif command == "version":
    print("Program wersja 1.0")
elif command == "calculator":
    first = float(input("Podaj pierwszą liczbę: "))
    second = float(input("Podaj drugą liczbę: "))
    sum_ = first + second
    print(first, "+", second, "=", sum_)

# Różnica między IF-ELIF a IF-IF
text = "help"

if text.startswith("h"):
    print("h")
if text.startswith("he"):
    print("he")  # zadziała

if text.startswith("h"):
    print("h")
elif text.startswith("he"):
    print("he")  # nie zadziała
    
# Instrukcja IF-ELIF-...-ELIF-ELSE
text = "asDF"
if text.isupper():
    print("Wszystkie litery wielkie!")
elif text.islower():
    print("Wszystkie litery są małe!")
else:
    print("Inna sytuacja")

### 🔴 Ćwiczenie
# Napisz program, który prosi o jeden, pojedynczy znak, a następnie wyświetla, czy jest to liczba, litera, biały znak czy znak specjalny.
# Białe znaki to spacja, tabulacja i nowa linia.

char = input("wprowadz jakiś znak: ")
if len(char) != 1:
        print("Proszę podać dokładnie jeden znak.")
# Sprawdź, czy znak jest literą
if char.isalpha():
    print("Wpisano jeden znak: ")
# sprawdza czy jest liczbą
elif char.isdigit():
        print("To jest liczba.")
# sprawdza białe znaki
# elif char in (" ","\t", "\n"):
#     print("to jest biały znak: ")
elif char.isspace():
    print("to jest biały znak: ")
    

