# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai. Последняя строка содержит число X
import random
N = int(input('input N: '))
A = [random.randint(0, 10) for _ in range(N)]
print(A)
X = int(input('input X: '))
print(A.count(X))
