# Формируется матрица F следующим образом: если в С  количество четных чисел в нечетных столбцах в области 1 больше,
# чем сумма чисел в нечетных строках в области 4, то поменять в Е симметрично области 1 и 4 местами, иначе В и Е
# поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: A*А– K*AT.
# Выводятся по мере формирования А, F и все матричные операции последовательно.

import random
from copy import deepcopy

def print_matrix(mat):
    for row in mat:
        for elem in row:
          print('{:4}'.format(elem), end=' ')
        print()


def pastemat(matF, matrix, column_index, row_index):
    a = column_index
    for row in matrix:
      for element in row:
        matF[row_index][column_index] = element
        column_index += 1
      row_index += 1
      column_index = a


def matzero(size):
    return [[0 for i in range(size)] for j in range(size)]


def matrix_input(mat, i1, i2, j1, j2):
    zero_mat = matzero(len(mat)//2)
    for i in range(i1, i2):
        for j in range(j1, j2):
            zero_mat[i - i1][j - j1] = mat[i][j]
    return zero_mat


try:
    K = int(input('Введите число K: '))
    n = int(input('Введите число число N, больше или равное 5: '))
    while n < 5:
        n = int(input('Введите число N, большее или равное 5: '))
except ValueError:
    print('Введенный символ не является числом.')
    exit(0)

ans = input('Для использование единичной матрицы напишите 1, для использования случайно сгенерированной напишите 2: ')
if ans not in ['1', '2']:
    print('Попробуйте ещё')
    while ans not in ['1', '2']:
        n = int(input('Для использование единичной матрицы напишите 1, для использования случайно сгенерированной напишите 2: '))
if ans == '1':
    matA = [[(1) for i in range(n)] for j in range(n)]
elif ans == '2':
    matA = [[random.randint(-10, 10) for i in range(n)] for j in range(n)]


print('Матрица А изначальная:')
print_matrix(matA)

hn = n//2
fn = hn
if n % 2 != 0:
    fn += 1

matC = matrix_input(matA, 0, hn, fn, n)
matE = matrix_input(matA, fn, n, fn, n)
matD = matrix_input(matA, fn, n, 0, hn)
matB = matrix_input(matA, 0, hn, 0, hn)

print('Подматрицы матрицы A:')
print('Подматрица B')
print_matrix(matB)
print('Подматрица С')
print_matrix(matC)
print('Подматрица D')
print_matrix(matD)
print('Подматрица E')
print_matrix(matE)

odd, summ = 1, 0
for i in range((n // 4) + 1):
    for j in range(i, hn - i):
        if i % 2 == 0 and matC[j][i] % 2 == 0:
            odd += 1
print('количество четных чисел в нечетных столбцах в области 1:', odd)

for i in range(n // 4, hn):
    for j in range(hn - i - 1, i + 1):
        if j % 2 != 0:
            summ += matC[i][j]
print('сумма чисел в нечетных строках в области 4:', summ)


if odd > summ:
    print('количество четных чисел в нечетных столбцах в области 1 больше, чем сумма чисел в нечетных строках')
    print('Начальная подматрциа E:')
    print_matrix(matE)
    for i in range((n // 4) + 1):
        for j in range(i, hn - i):
            matE[i][j], matE[j][i] = matE[j][i], matE[i][j]
    print('Получившаяся подматрица E:')
    print_matrix(matB)
else:
    print('количество четных чисел в нечетных столбцах в области 1 меньше, чем сумма чисел в нечетных строках')
    matE, matB = matB, matE

matF = deepcopy(matA)
pastemat(matF, matB, 0, 0)
pastemat(matF, matC, fn, 0)
pastemat(matF, matE, fn, fn)
pastemat(matF, matD, 0, fn)

print('Матрица F:')
print_matrix(matF)

matAt = matzero(n)
matFA = matzero(n)

print('Вычисляем A*F– K*AT:')

for i in range(n):
    for j in range(n):
        matFA[i][j] = matF[i][j] * matA[i][j]
print('Результат A * F:')

print_matrix(matFA)
print("Матрица A транспонированая:")
for i in range(n):
    for j in range(n):
        matAt[i][j] = matA[j][i]
print_matrix(matAt)

for i in range(n):
    for j in range(n):
        matAt[i][j] *= K
print('Результат K * AT:')
print_matrix(matAt)

res = matzero(n)
for i in range(n):
    for j in range(n):
        res[i][j] = matFA[i][j] - matAt[i][j]
print('Результат (A*F) – (K * AT):')
print_matrix(res)