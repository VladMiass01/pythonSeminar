# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

# def sum(number):
#     number = int(number)
#     res = 0
#     while number > 0:
#         digit = number % 10
#         res = res + digit
#         number = number // 10
#     return res

n = input("Введи номер билета: ")
# sum1 = sum(n[:3])
sum1 = int(n[0]) + int(n[1]) + int(n[2])
# sum2 = sum(n[3:])
sum2 = int(n[3]) + int(n[4]) + int(n[5])
if sum1 == sum2:
    print("yes")
else:
    print("no")