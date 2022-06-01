import math

#zad 1
def ticket_price(age):
    if age < 18:
        print( "Bilet kosztuje 10 zl" )
    elif age >= 18 and age <= 25:
        print( "Bilet kosztuje 16 zl" )
    else:
        print( "Bilet kosztuje 24 zl" )

#zad 2
def square_equation(a, b, c):
    if a == 0:
        print( "Rownanie liniowe ktore ma 1 rozwiazanie: ", c*(-1) / b)
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print( "Rownanie kwadratowe nie ma rozwiazania")
        elif delta == 0:
            print( "Rownanie kwadratowe ma 1 rozwiazanie: ", (-1)*b / 2*a)
        else:
            print( "Rownanie kwadratowe ma 2 rozwiazania: ", (-1)*b - math.sqrt(delta) / 2*a, (-1)*b + math.sqrt(delta) / 2*a )

#zad3
def average(*numbers):
    sum = 0
    i = 0
    for num in numbers:
        sum = sum + num
        i = i + 1
    avg = int(sum / i)
    if(avg % 2 == 0):
        print( "Średnia jest parzysta i wynosi: ", avg)
    else:
        print( "Średnia nie jest parzysta i wynosi: ", avg)


age = int(input( "Podaj wiek: " ))
ticket_price(age)

a=int(input( "Podaj wspolczynnik a: " ))
b=int(input( "Podaj wspolczynnik b: " ))
c=int(input( "Podaj wspolczynnik c: " ))
square_equation(a, b, c)

average(1,2,3,4,5,6)
