# Напишите программу, которая на вход принимает # два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии
def res(a, b):
    if b == 0:
        return 1
    return a * res(a, b - 1)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
print(res(a, b))