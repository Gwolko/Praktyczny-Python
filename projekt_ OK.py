# def sprawdz_haslo(haslo):
    # raport = []

    # Sprawdzenie długości hasła
    # if len(haslo) < 8:
    #     raport.append("Hasło musi mieć co najmniej 8 znaków.")

    # # Sprawdzenie obecności spacji
    # if " " in haslo:
    #     raport.append("Hasło nie może zawierać spacji.")

    # # Sprawdzenie obecności małej litery
    # if not any(znak.islower() for znak in haslo):
    #     raport.append("Hasło musi zawierać co najmniej jedną małą literę.")

    # # Sprawdzenie obecności wielkiej litery
    # if not any(znak.isupper() for znak in haslo):
    #     raport.append("Hasło musi zawierać co najmniej jedną wielką literę.")

    # # Sprawdzenie obecności znaku specjalnego
    # if not any(znak in "!@#$%^&*()-_+=[]{}|\\:;\"'<>,.?/~`" for znak in haslo):
    #     raport.append("Hasło musi zawierać co najmniej jeden znak specjalny.")

    # # Wyświetlenie raportu
    # if raport:
    #     print("Hasło jest niepoprawne. Oto, co należy poprawić:")
    #     for punkt in raport:
    #         print("- " + punkt)
    # else:
    #    print("Hasło jest poprawne!")

# # Wprowadzenie hasła
# haslo = input("Podaj hasło: ")
# sprawdz_haslo(haslo)
### 🔴 Ćwiczenie 
# 1. Poproś użytkownika o hasło, a następnie sprawdź, czy spełnia ono reguły bezpieczeństwa.
# 2. Hasło powinno mieć minimum jedną małą literę, jedną wielką literę i jeden znak specjalny.
# 3. Hasło nie może zawierać spacji!  (wewnętrzny wymóg klienta wynikający z ograniczeń ich systemu teleinformatycznego)
# 4. Hasło musi mieć minimum 8 znaków.
# 5. Jeśli hasło jest niepoprawne, wyświetl raport w punktach co należy zmienić.

# #Wprowadz hasło - cel sprawdzenie wymagań.
# haslo = input("Wprowadź HASŁO: ")

# # Zmienne na komunikaty
# bledy = ""  # Zbiera komunikaty o błędach
# komunikaty_ok = ""  # Zbiera pozytywne komunikaty

# # Sprawdzanie długości hasła
# if len(haslo) < 8:
#     bledy += "Hasło musi mieć co najmniej 8 znaków.\n"
# else:
#     komunikaty_ok += "Hasło zawiera prawidłową liczbę znaków.\n"

# # Sprawdzanie obecności znaku specjalnego
# if not any(znak in "!@#$%^&*()-_+=[]{}|\\:;\"'<>,.?/~`" for znak in haslo):
#     bledy += "Hasło musi zawierać co najmniej jeden znak specjalny.\n"
# else:
#     komunikaty_ok += "Hasło zawiera znak specjalny.\n"

# # Sprawdzanie obecności spacji
# if " " in haslo:
#     bledy += "Hasło nie może zawierać spacji.\n"
# else:
#     komunikaty_ok += "Hasło nie zawiera spacji.\n"

# # Sprawdzanie obecności małej litery
# if not any(znak.islower() for znak in haslo):
#     bledy += "Hasło musi zawierać co najmniej jedną małą literę.\n"
# else:
#     komunikaty_ok += "Hasło zawiera małą literę.\n"

# # Sprawdzanie obecności wielkiej litery
# if not any(znak.isupper() for znak in haslo):
#     bledy += "Hasło musi zawierać co najmniej jedną wielką literę.\n"
# else:
#     komunikaty_ok += "Hasło zawiera wielką literę.\n"

# # Wyświetlanie komunikatów o błędach
# if bledy:
#     print("Hasło nie spełnia wymagań bezpieczeństwa. Oto, co należy poprawić:")
#     print(bledy)

# # Wyświetlanie komunikatów pozytywnych na końcu
# if komunikaty_ok:
#     print("Hasło spełnia następujące wymagania:")
#     print(komunikaty_ok)

### 🔴 ROZWIAZNIA Z SZKOLENIA nie działa i nie wiem dlaczego?
# haslo=input("Podaj hasło: ")
# # tworzymy zmienne 
# has_lowercase=False
# has_uppercase=False
# has_space=False
# has_special_char=False
# for char in haslo:
#     if char.islower():
#         has_lowercase=True
#     elif char.isspace():
#         has_space=True
#     elif char.upper():
#         has_uppercase=True
#     elif char in has_special_char():
#         has_special_char=True
# long_enought =len (haslo) >= 8

# # Tworzymy zmienną łaczacą wszystkie pozostałe zmienne
# id_correct=(has_lowercase and has_uppercase and has_space and has_special_char and long_enought)
# # Wyświetlamy odpowiedni komunikat
# if id_correct:
#     print("Hasło spełnia wymogi bezpieczeństwa.")
# else:
#     print("Twoje hasło nie jest wystarczająco bezpieczne, zastosuj poniższe reguły:")
#     if not has_lowercase:
#         print("- Hasło musi zawierać co najmniej jedną małą literę.")
#     if not has_uppercase:
#         print("- Hasło musi zawierać co najmniej jedną wielką literę.")
#     if has_space:
#         print("- Hasło nie może zawierać spacji.")
#     if not has_special_char:
#         print("- Hasło musi zawierać co najmniej jeden znak specjalny.")
#     if not long_enought:
#         print("- Hasło musi mieć co najmniej 8 znaków.")

### 🔴 ROZWIAZNIA Z SZKOLENIA poprawiona przez mnie 1
# haslo = input("Podaj hasło: ")

# # Tworzymy zmienne sprawdzające różne wymagania
# has_lowercase = False
# has_uppercase = False
# has_space = False
# has_special_char = False

# # Iterujemy przez każdy znak w haśle, aby sprawdzić różne warunki
# for char in haslo:
#     if char.islower():
#         has_lowercase = True
#     elif char.isspace():
#         has_space = True
#     elif char.isupper():
#         has_uppercase = True
#     elif char in "!@#$%^&*()-_+=[]{}|\\:;\"'<>,.?/~`":
#         has_special_char = True

# # Sprawdzamy, czy hasło ma co najmniej 8 znaków
# long_enough = len(haslo) >= 8

# # Tworzymy zmienną łączącą wszystkie wymagania bezpieczeństwa
# is_correct = (
#     has_lowercase and has_uppercase and not has_space and has_special_char and long_enough
# )

# # Wyświetlamy odpowiedni komunikat
# if is_correct:
#     print("Hasło spełnia wymogi bezpieczeństwa.")
# else:
#     print("Twoje hasło nie jest wystarczająco bezpieczne, zastosuj poniższe reguły:")
#     if not has_lowercase:
#         print("- Hasło musi zawierać co najmniej jedną małą literę.")
#     if not has_uppercase:
#         print("- Hasło musi zawierać co najmniej jedną wielką literę.")
#     if has_space:
#         print("- Hasło nie może zawierać spacji.")
#     if not has_special_char:
#         print("- Hasło musi zawierać co najmniej jeden znak specjalny.")
#     if not long_enough:
#         print("- Hasło musi mieć co najmniej 8 znaków.")


 ### 🔴Inne ROZWIAZNIA projektu
 # wykorzystanie listy
 # Poproś użytkownika o podanie hasła
haslo = input("Podaj hasło: ")

# Lista błędów do wyświetlenia
bledy = []

# Sprawdzanie długości hasła
if len(haslo) < 8:
    bledy.append("Hasło musi mieć co najmniej 8 znaków.")

# Sprawdzanie obecności małej litery
if not any(char.islower() for char in haslo):
    bledy.append("Hasło powinno zawierać minimum jedną małą literę.")

# Sprawdzanie obecności wielkiej litery
if not any(char.isupper() for char in haslo):
    bledy.append("Hasło powinno zawierać minimum jedną wielką literę.")

# Sprawdzanie obecności znaku specjalnego
import re
if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", haslo):
    bledy.append("Hasło powinno zawierać minimum jeden znak specjalny.")

# Sprawdzanie obecności spacji
if " " in haslo:
    bledy.append("Hasło nie może zawierać spacji.")

# Wyświetlanie raportu lub informacji o poprawności hasła
if bledy:
    print("Hasło nie spełnia wymagań bezpieczeństwa. Oto, co należy poprawić:")
    for i, blad in enumerate(bledy, 1):
        print(f"{i}. {blad}")
else:
    print("Hasło spełnia wszystkie wymagania bezpieczeństwa!")
