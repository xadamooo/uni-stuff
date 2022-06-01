import numpy as np
import random

'''1'''

grades = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
matrix = []
size = 4  #zmienic w przypadku innego rozmiaru
for i in range(size):
    row = []
    for k in range(size):
        row.append(random.choice(grades))
    matrix.append(row)
print(np.array(matrix))
avgs = []
hnotes = []
n = int(input("1:\nPodaj liczbe, by sprawdzic ile studentow nie zaliczylo co najmniej takiej liczby przedmiotow\n"))
pktA1 = 0
maks = 2.0
for student in matrix:
    if max(student) > maks:
        maks = max(student)
    k = suma = j = 0
    for grade in student:
        if grade < 3.0:
            k = k + 1
        suma = suma + grade
    avgs.append(suma/size)
    if k >= n:
        pktA1 = pktA1 + 1
print(f'Tylu uczniów nie zaliczyło {n} przedmiotu/ów: {pktA1}')
for student in matrix:
    p = j = 0
    for grade in student:
        if grade == maks:
            p = p + 1
        j = j + 1
    hnotes.append(p)
i = r = 0
subjectnr = [1, 2, 3, 4]
print('Histogramy:')
for a in np.array(matrix).T.tolist():
    np.histogram(a, bins=[2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5])
    hist, bins = np.histogram(a, bins=[2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5])
    print(f'Przedmiot {subjectnr[r]}:')
    print(hist)
    print(bins)
    r = r + 1
print('Oceny studenta/ow z najwyzsza srednia:')
for i in avgs:
    if i == max(avgs):
        print(matrix[avgs.index(i)])
print('Oceny studenta/ow z najnizsza srednia:')
for i in avgs:
    if i == min(avgs):
        print(matrix[avgs.index(i)])
print('Student/ci z najwieksza liczba ocen najwyzszych ma/mają oceny:')
for k in hnotes:
    if k == max(hnotes):
        print(matrix[hnotes.index(k)])
print('Studenci ze srednia nie nizsza niz 4.0:')
for avg in avgs:
    if avg >= 4:
        print(matrix[avgs.index(avg)])


'''2'''


m1 = np.random.rand(3, 3)
m2 = np.random.rand(3, 3)
print(f'2:\nOdleglosc dwoch macierzy:\n{m1}\noraz\n{m2}\nwynosi: {abs(m1-m2).sum()}')


'''3'''


def gauss(mat):
    k = 0
    row, col = np.shape(mat)
    for r in range(row):
        if k >= col:
            return
        i = r
        while (mat[i][k] == 0):
            i += 1
            if (i == row):
                i = r
                k += 1
                if (col == k):
                    return
        mat[[r, i]] = mat[[i, r]]

        if (mat[r][k] != 0):
            mat[r] = mat[r]/mat[r][k]
        for i in range(row):
            if (i != r):
                mat[i] = mat[i] - mat[i][k]*mat[r]
        k += 1


mat = np.array([[9, 3, 4, 7],
                [4, 3, 4, -8],
                [1, 1, 1, 3]])
print(f'Macierz początkowa:\n{mat}')
mat = mat.astype(np.float)
gauss(mat)
print(f'Macierz schodkowa zredukowana:\n{mat}')


'''4'''

rec = np.array([[1, 151, 3],
                [2, 44, 10],
                [1, 18, 1]])
desc = np.array([[44, 15, 'sztuki'],
                 [151, 10, 'sztuki'],
                 [18, 5, 'waga']])

print(f'3:\n{rec}\n{desc}')
product_ids = []
for i in rec:
    product_ids.append(i[1])
product_ids2 = []
for i in desc:
    product_ids2.append(int(i[0]))
for prod_id in product_ids:
    try:
        a = product_ids2.index(prod_id)
    except ValueError:
        thirdOK = False
    else:
        continue
for i in desc:
    isError = False
    if i[2] == 'sztuki':
        for j in rec:
            if isinstance(j[2], np.int32):
                continue
            else:
                print('bledne dane')
                isError = True
                break
    if isError:
        thirdOK = False
        break
    else:
        thirdOK = True
        break
if thirdOK:
    print('Dane są poprawne')
else:
    print('Dane są niepoprawne')


def desc_get_by_key(desc, key):
    for record in desc:
        if int(record[0]) == key:
            return record[1], record[2]
    return None, None


def increase_expense(user_total_expense, user_id, value):
    for user in user_total_expense:
        if user_id == int(user[0]):
            user[1] += value
            return user_total_expense
    return np.append(user_total_expense, [[user_id, value]], axis=0)


user_total_expense = np.array([[rec[0][0], 0]])

for client in rec:
    user_id, product_id, amount = client
    price, unit = desc_get_by_key(desc, product_id)
    user_total_expense = increase_expense(user_total_expense, user_id, int(amount) * int(price))
print(f'PARAGONY:\n{user_total_expense}')
