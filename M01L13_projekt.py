### 🔴 Projekt

# Napisz dla BBC program sprawdzający złożoność artykułów i wpisów, dzięki czemu pracę dziennikarzy będzie można sparametryzować i automatycznie ustalić, czy piszą teksty proste i łatwe w zrozumieniu. Policz jaka jest średnia długość słów i wyświetl rezultat.

# Podpowiedzi:

# words = len(text.split())  # liczba słów

# a = 9
# b = 3
# division = a / b
# print(division)

# Aby policzyć średnią długość słowa, możesz bazować na liczbie wszystkich znaków oraz liczbie słów.


# rozwiązanie projektu bbc

#tekst = input("Wpisz tekst artykułu: ")
#characters = len(tekst)
#word: int = len(tekst.split()) #liczba słów
#average_word_length: int = (characters - word/word)
#print("tekst_artykulu ma srednio" ,division, "znaków" )

#tekst = input("Wpisz tekst artykułu: ")
#characters = len(tekst)
#word = len(tekst.split()) #liczba słów
#average_word_length = (characters - word/word) -1 # bo odejmujemy #spacje ktore sie wliczaja
#average_word_length = (characters - word/word)
#print("tekst_artykulu ma srednio" ,average_word_length, "znaków" )

tekst = input("Wpisz tekst artykułu: ")
characters = len(tekst)
word = len(tekst.split()) #liczba słów
average_word_length = (characters - word/word) -1 # bo odejmujemy # spacje ktore sie wliczaja
#average_word_length = (characters - word/word)
print("tekst_artykulu ma srednio" ,average_word_length, "znaków" )

