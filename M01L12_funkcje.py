### 🔴 Co mają wspólnego przepisy kulinarne i programowanie?

# 👉 Skończyłæś większość tego tygodnia - gratulacje! Masz już wszystko skonfigurowane.
# 👉 Przechodzimy do drugiej, krótszej części tego tygodnia - do kodowania.

### 🔴 Funkcje

# 👉 Funkcje są jak przepisy kulinarne. DEFINIOWANIE własnych funkcji w kolejnych modułach.
# 👉 Dzisiaj jak WYWOŁYWAĆ (=używać) wbudowane funkcje

### 🔴 Niezbędnik

# Składnia wywołania: nazwa_funkcji ( argumenty )

print(1234)

print("tekst")

text = "tekst"
print(text)

# Niektóre funkcje mogą przyjmować więcej argumentów - rozdziel je przecinkiem.
print("tekst", "wiecej tekstu")

# Niektóre funkcje nie przyjmują żadnych argumentów - wtedy nawiasy też są konieczne!
print()  # print bez argumentów przechodzi do następnej linii

# ❌ Typowa pułapka - brakuje nawiasów okrągłych, w efekcie ta linia kodu nie robi nic, ale nie ma błędu!
print

# Parametry funkcji to to samo co jej argumenty. Jest to synonim. (ok, zgoda, jest subtelna różnica o której w jednym z kolejnych modułów).

# Funkcje mogą zwracać wartość - rezultat swojego działania.
dlugosc = len(text)  # Funkcja len zwraca długość napisu przekazanego jako argument.
print(dlugosc)

# W jednej linii można złożyć kilka wywołań funkcji (tzw. composability)
print(len(text))

# ❌ Nie można zagnieżdżać przypisania.
# print(text = "tekst")

# Niektóre argumenty przekazujemy w sposób nazwany (więcej w module o funkcjach).
# W takiej sytuacji znak równości nie ma nic wspólnego z przypisaniem!
print("liczba:", end=" ")
print(1234)
print(2345)

# Funkcja input wyświetla tekst (tak samo jak print) i prosi użytkownika o jedną linię tekstu. Użytkownik zatwierdza tekst enterem.
tekst = input("Tekst: ")
print("Wpisałeś:", tekst)

### 🔴 Ćwiczenie: Napisz program, który prosi użytkownika o tekst i wyświetla ile ma on liter.

# Wyślij nam swoje zadanie domowe, a zobaczysz rozwiązanie, jego omówienie, na co dobrze było zwrócić uwagę, a także najczęstsze błędy.
# moje cwiczenie
# sposob pierwszy
tekst_artykulu = input("Wpisz tekst artykułu: ")
print(len(tekst_artykulu))
# sposob drugi lepszy
tekst_artykulu = input("Wpisz tekst artykułu: ")
characters = len(tekst_artykulu)
print("tekst ma" ,characters, "znaków" )


# #1
text = print("Wypisuję tekst")  # ❌ print nic nie zwraca, dlatego nie ma sensu przypisywać rezultatu do zmiennej; pomimo tego program zadziała, bo w Pythonie każda funkcja musi coś zwrócić, nawet jeśli nie ma to sensu; w takiej sytuacji pojawia się None - czyli informacja o braku informacji :)
print(text)

# #2
print("tekst", "wiecej tekstu"  # ❌ brakuje nawiasu zamykającego

# #3
print(len(text)  # ❌ znowu brakuje nawiasu zamykającego

# #4
print("tekst, "wiecej tekstu")  # ❌ tym razem brakuje zamykającego cudzysłowu po `"tekst,`, zauważ też, że kolorowanie składni bardzo ułatwia dostrzeżenie tego typu błędów

# #5
print("liczba:" end=" ")  # ❌ brakuje przecinka
print(1234)
