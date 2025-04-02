import os
import glob 

#deklaracja stałych
POZYTYWNW_PLIKI_PATTERN = 'M03/data/aclImdb/test/pos/*.txt'
NEGATYWNE_PLIKI_PATTERN = 'M03/data/aclImdb/test/neg/*.txt'
# zaladunek pozytywnych recenzji
pozytywne_files=glob.glob(POZYTYWNW_PLIKI_PATTERN) #listę nazw plików i katalogow  pasujących do podanego wzorca.
pozytywne=[] #pustą listę o nazwie pozytywne.
for file in pozytywne:
    with open(file, 'r', encoding='utf-8') as stream:
        content=stream.read()
        words=content.lower().replace('<br />', ' ').split()
        #Zamiana tekstu na małe litery.Usunięcie znaczników HTML.Podział tekstu na listę słów
        pozytywne.append(words)
# zaladunek negatywnych recenzji
pozytywne_files=glob.glob(NEGATYWNE_PLIKI_PATTERN) #listę nazw plików i katalogow  pasujących do podanego wzorca.
negatywne=[] #pustą listę o nazwie pozytywne.
for file in negatywne:
    with open(file, 'r', encoding='utf-8') as stream:
        content=stream.read()
        words=content.lower().replace('<br />', ' ').split()
        #Zamiana tekstu na małe litery.Usunięcie znaczników HTML.Podział tekstu na listę słów
        negatywne.append(words)
sentencja=input('podaj sentencje/komentarz: ') 
words=sentencja.lower().replace('<br />', ' ').split()

#obliczanie sentymenty w daniach
sentyment_zdania=0
for word in words:
    positive=0
    negative=0
    for recenzja in pozytywne:
        positive += 1
    for recenzja in negatywne:
        negative += 1
all_= positive + negative #LICZNI WSZYSTKICH KOMENTARZY
if all_ !=0: # sprawdzenie czy zmienna all_ nie jest równa 0!
    slowa_sentencje = (positive-negative)/all_
else:
    slowa_sentencje=0.0
    print(words, slowa_sentencje )
    sentyment_zdania += slowa_sentencje
slowa_sentencje/=len(words)

#podsumowanie

if sentyment_zdania > 0:
    ocena = 'pozytywne'
else:
    ocena = 'negatywne'
print()
print("to zdanie jest", ocena, ', sentyment =' , sentyment_zdania)
    

