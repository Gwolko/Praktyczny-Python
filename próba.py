haslo = input("Podaj hasło: ")

# tworzymy zmienne 
has_lowercase = False
has_uppercase = False
has_space = False
has_special_char = False
special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"

for char in haslo:
    if char.islower():
        has_lowercase = True
    elif char.isupper():
        has_uppercase = True
    elif char.isspace():
        has_space = True
    elif char in special_characters:
        has_special_char = True

long_enough = len(haslo) >= 8

# Tworzymy zmienną łaczacą wszystkie pozostałe zmienne
is_correct = has_lowercase and has_uppercase and not has_space and has_special_char and long_enough

# Wyświetlamy odpowiedni komunikat
if is_correct:
    print("Hasło spełnia wymogi bezpieczeństwa.")
else:
    print("Twoje hasło nie jest wystarczająco bezpieczne, zastosuj poniższe reguły:")
    if not has_lowercase:
        print("- Hasło musi zawierać co najmniej jedną małą literę.")
    if not has_uppercase:
        print("- Hasło musi zawierać co najmniej jedną wielką literę.")
    if has_space:
        print("- Hasło nie może zawierać spacji.")
    if not has_special_char:
        print("- Hasło musi zawierać co najmniej jeden znak specjalny.")
    if not long_enough:
        print("- Hasło musi mieć co najmniej 8 znaków.")
