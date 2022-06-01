'''zad1'''

file1 = open('zad1.txt', 'w')
while (len((text := input('PODAJ TEKST' + ' '))) > 0):
    file1.write(text + '\n')
file1.close()
file1 = 'zad1.txt'
with open(file1, 'a') as file1_obj:
    file1_obj.write(input('PODAJ 2 TEKST ' + ' ') + '\n')
with open(file1, 'a') as file1_obj:
    file1_obj.write(input('PODAJ 3 TEKST ' + ' ') + '\n')

'''zad2'''

try:
    number = int(input('PODAJ LICZBE '))
except ValueError:
    print('BLEDNY TYP DANYCH')

'''zad3'''

try:
    open('zad1.txt', 'r')
except FileNotFoundError:
    print('Nie znaleziono pliku')
else:
    text2 = open(file1, 'r').read()
    length = sum(1 for c in text2 if c != ' ' and c != '\n')
    print(length)
    try:
        text2.index(input('PODAJ WYSZUKIWANA FRAZE: '))
    except ValueError:
        print('SZUKANA FRAZA NIE ISTNIEJE')
    else:
        print('SZUKANA FRAZA ISTNIEJE')
