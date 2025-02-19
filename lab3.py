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
    return [[0 for _ in range(size)] for _ in range(size)]

def matrix_input(mat, i1, i2, j1, j2):
    zero_mat = matzero(len(mat)//2)
    for i in range(i1, i2):
        for j in range(j1, j2):
            zero_mat[i - i1][j - j1] = mat[i][j]
    return zero_mat

def read_matrix_from_file(filename):
    try:
        with open(filename, 'r') as f:
            matrix = [list(map(int, line.split())) for line in f]
        return matrix
    except FileNotFoundError:
        print("Файл не найден.")
        exit(0)
    except ValueError:
        print("Ошибка в формате данных файла.")
        exit(0)

try:
    K = int(input('Введите число K: '))
    filename = input('Введите имя файла с матрицей: ')
    matA = read_matrix_from_file(filename)
    n = len(matA)
except ValueError:
    print('Ошибка ввода. Ожидалось число.')
    exit(0)

print('Матрица A из файла:')
print_matrix(matA)

hn = n // 2
fn = hn + (n % 2)

matC = matrix_input(matA, 0, hn, fn, n)
matE = matrix_input(matA, fn, n, fn, n)
matD = matrix_input(matA, fn, n, 0, hn)
matB = matrix_input(matA, 0, hn, 0, hn)

print('Подматрицы матрицы A:')
print('Подматрица B')
print_matrix(matB)
print('Подматрица C')
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
print('Количество четных чисел в нечетных столбцах в области 1:', odd)

for i in range(n // 4, hn):
    for j in range(hn - i - 1, i + 1):
        if j % 2 != 0:
            summ += matC[i][j]
print('Сумма чисел в нечетных строках в области 4:', summ)

if odd > summ:
    print('Меняем области 1 и 4 в E симметрично')
    for i in range((n // 4) + 1):
        for j in range(i, hn - i):
            matE[i][j], matE[j][i] = matE[j][i], matE[i][j]
else:
    print('Меняем B и E местами')
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

print('Вычисляем A * F – K * AT:')
for i in range(n):
    for j in range(n):
        matFA[i][j] = matF[i][j] * matA[i][j]
print('Результат A * F:')
print_matrix(matFA)

print('Матрица A транспонированная:')
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
