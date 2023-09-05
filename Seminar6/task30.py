first_element = int(input("первый элемент: "))
difference = int(input("разность: "))
quantity = int(input("количество: "))
a = []
a.append(first_element)
for i in range(1, quantity):
    a.append(a[0] + i * difference)
print(a)