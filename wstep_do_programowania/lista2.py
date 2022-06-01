#zad1
print("zad1")

num1 = 5
num2 = 3
num3 = 2
num3 += num1
num4 = pow(num2, num3)
print(num1 * num2)
print(num3 / num4, "\n") 

#zad2
print("zad2")

print("Dodawanie 5+3: %d" %int( num1 + num2 ))
print("Odejmowanie 5-3: %d" %int( num1 - num2 ))
print("Mnozenie 5*3:  %d" %int( num1 * num2 ))
print("Dzielenie calkowite 5/3: %0.2f" %int( num1 / num2 ))
print("Modulo 5 z 3: %d" %int( num1 % num2 ))
print("Potegowanie 50000 do potegi 3: %E" %int( ( num1 * 10000 ) ** num2 ))
print("Dzielenie 5 przez 3 z zaokragleniem w gore: %d" %int(num1 // num2), "\n")

#zad3
print("zad3")

a = 5
b = str(a)
c = float(b)
print("int:", a, "str:", b, "float:", c, "\n" )

#zad4
print("zad4")

firstName = "Adam"
lastName = "Bednarski"
initials = firstName[0] + lastName[0]
personalData = f" {initials.upper()} {firstName} {lastName} "
outcome = f"Dane osobowe:{personalData}"
print(outcome)
