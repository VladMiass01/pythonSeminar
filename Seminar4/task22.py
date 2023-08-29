array1 = set(map(int, input().split()))
array2 = set(map(int, input().split()))
s_set = sorted(array1.intersection(array2))
print(*s_set)