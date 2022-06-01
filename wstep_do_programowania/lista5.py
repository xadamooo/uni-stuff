import math
#zad1
class LogExp:
    def __init__(self, a):
        self.a = a
    def logarithm(self, x):
    #obliczanie logarytmu
        return(math.log(x, self.a))
    def exponential(self, x):
    #obliczanie funkcji wykladniczej
        return(pow(x, self.a))

result = LogExp(3)
print("Logarytm o podstawie 3 i liczbie logarytmowanej 9 wynosi:")
print(int(result.logarithm(9)))
print("Wynik funkcji wykładniczej o podstawie 3 i potędze 9 wynosi:")
print(result.exponential(9), "\n")

#zad2
class Prostokat:
#obliczanie pola prostokata i kwadratu
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return(self.a * self.b)

class Kwadrat(Prostokat):
    def __init__(self, a):
        super().__init__(a, a)

sides1 = Prostokat(3, 5)
side2 = Kwadrat(3)
print("Pole prostokata o bokach 3 i 5 wynosi:")
print(sides1.area())
print("Pole kwadratu o boku 3 wynosi:")
print(side2.area(), "\n")

#zad3
subject_1 = "Analiza Matematyczna"
subject_2 = "Wstep do inzynierii systemow"
subject_3 = "Wstep do programowania"
class Student:
    def __init__(self, name, last_name, index_number):
        #dane studenta
        self.name = name
        self.last_name = last_name
        self.index_number = index_number
        self.grades = { subject_1 : [], subject_2 : [], subject_3 : [] }
    def AddGrade(self, subject, grade):
        #dodanie studentowi oceny z danego przedmiotu
        self.grades[subject].append(grade)
    def RemoveGrade(self, subject, grade):
        #usuniecie studentowi oceny z danego przedmiotu
        self.grades[subject].remove(grade)
    def ChangeGrade(self, subject, grade_before, grade_changed):
        #zmiana oceny studenta z danego przedmiotu
        self.grades[subject].remove(grade_before)
        self.grades[subject].append(grade_changed)
    def ShowGrade(self, subject):
        #wyswietlenie ocen studenta z danego przedmiotu
            print(self.grades[subject])
      

student1 = Student("Adam", "Bednarski", "123456")
student2 = Student("Kamil", "Speda", "654321")
student1.AddGrade(subject_1, 6)
student2.AddGrade(subject_2, 4)
student1.AddGrade(subject_2, 1)
student1.AddGrade(subject_2, 5)
student1.AddGrade(subject_1, 3)
student2.AddGrade(subject_1, 5)
student2.AddGrade(subject_1, 6)
student1.AddGrade(subject_3, 2)
student1.AddGrade(subject_3, 3)
student2.AddGrade(subject_3, 5)
student2.AddGrade(subject_3, 3)
print("Oceny studenta nr 1 z przedmiotu: Analiza Matematyczna:")
student1.ShowGrade(subject_1)
print("Oceny studenta nr 1 z przedmiotu: Wstep do inzynierii systemow:")
student1.ShowGrade(subject_2)
print("Oceny studenta nr 1 z przedmiotu: Wstep do programowania:")
student1.ShowGrade(subject_3)
print("Oceny studenta nr 2 z przedmiotu: Analiza Matematyczna:")
student2.ShowGrade(subject_1)
print("Oceny studenta nr 2 z przedmiotu: Wstep do inzynierii systemow:")
student2.ShowGrade(subject_2)
print("Oceny studenta nr 2 z przedmiotu: Wstep do programowania:")
student2.ShowGrade(subject_3)
student2.ChangeGrade(subject_3, 5, 2)
student1.AddGrade(subject_1, 1)
print("Oceny studenta nr 2 PO ZMIANIE z przedmiotu: Wstep do inzynierii systemow:")
student2.ShowGrade(subject_3)
print("Oceny studenta nr 1 PO DODANIU OCENY z przedmiotu: Analiza Matematyczna:")
student1.ShowGrade(subject_1)





        

