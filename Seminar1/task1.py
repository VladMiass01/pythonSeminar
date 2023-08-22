# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

n = int(input("Введи трехзначное число: "))
res = 0

while n > 0:
    digit = n % 10
    res = res + digit
    n = n // 10
print(res)