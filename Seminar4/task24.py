n = int(input('Введите количество кустов черники: '))
arr = list()
for i in range(n):
    a =int(input('Введите количество ягод на кусте: '))
    arr.append(a)
arr.append(arr[0])
arr.append(arr[1])
arr_count = list()
for i in range(1, len(arr) - 1):
       arr_count.append(arr[i - 1] + arr[i] + arr[i + 1 ])
       print(i, arr_count)
print(max(arr_count))
print(arr)