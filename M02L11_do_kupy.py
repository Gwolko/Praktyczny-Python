### 🔴 Złóżmy to wszystko do kupy

# Przykład
# counter = 0
# text = "ile liter ma ten napis?"
# for char in text:
#     if char.isalpha():
#         counter = counter + 1
#         # lub prościej:
#         # counter += 1
#         # counter =+ 1  # ❌ częsta pomyłka - nie będzie żadnego błędu!
# print("Ten tekst ma", len(text), "znaków, w tym", counter, "liter.")

### 🔴 Ćwiczenie

# Napisz program, który anonimizuje dane statystyczne w tekstach poprzez zastąpienie wszelkich liczb iksami.


# text = input("podaj tekst  ")
# for digit in "0123456789":
#     text = text.replace(digit, "X")
# print("Zmodyfikowany tekst: " , text)

# wolniejsze rozwiązanie
text = input("Podaj tekst: ")
for char in text:
    if char.isdigit():
        text = text.replace(char, "X")
print(text)


