import sys

filename = sys.argv[1]
with open(filename) as stream:
    content = stream.read()
lines=content.split('\n')
lines_cunter=len(lines)
word_cunter=len(content.split())
charakters_cunter=len(content)

print(f"\nLiczba znaków: {charakters_cunter}")
print(f"Liczba słów: {word_cunter}")
print(f"Liczba linii: {charakters_cunter}")
print(f"Nazwa pliku: {filename}")