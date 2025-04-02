# Określenie wymiarów prostokąta
m = 5  # liczba wierszy  zmienna ilość wierszy
n = 10  # liczba kolumn zmienna

# # Generowanie prostokąta
for i in range(m):  # Pętla dla wierszy  powtarza się m razy, aby wygenerować każdy wiersz.
    print("*" * n)  # Wypisanie linii złożonej z n znaków * Tworzy ciąg składający się z n znaków * drukuj znak

    
######## Napisz program, który wydrukuje tabliczkę mnożenia dla liczb od 1 do 10. Podpowiedź: sprawdź jakie jeszcze argumenty przyjmuje funkcja range


# Generowanie tabliczki mnożenia do 100
for i in range(1, 11):  # Liczby od 1 do 10 (wiersze)
    for j in range(1, 11):  # Liczby od 1 do 10 (kolumny)
        print(f"{i * j:4}", end="\t")  # Wyświetlanie wyniku z wyrównaniem do 4 znaków
    print()  # Przejście do nowej linii po każdym wierszu

