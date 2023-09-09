# def f(x):
#     return x


# print(f(5))

# f1 = lambda x: x
# print(f1(6))

# print((lambda x: x) (7))

# x = "2 4 5 6 7 8 12"
# print(x)

# x1 = x.split()
# print(x1)

# x2 = list(map(int, x1))
# print(x2)

# x2 = list(map(lambda y: int(y), x.split()))
# print(x2)

# x2 = list(map(lambda y: 2 * y, x.split()))
# print(x2)

# x2 = list(map(lambda y: 2 * y, input().split()))
# print(x2)

# x2 = list(filter(lambda y: int(y) % 2 == 0, x.split()))
# print(x2)

# x2 = list(filter(lambda y: int(y) % 8, x.split()))
# print(x2)

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformation = lambda x: x
# transormed_values = list(map(transformation, values))
# transormed_values = list(map(lambda x: x, values))
# print(values)
# print(transormed_values)

# def find_farthest_orbit(list_of_orbits):
#     filter_orbit = list(filter(lambda x: x[0] != x[1], list_of_orbits))
#     square_orbit = list(map(lambda x: x[0] * x[1], filter_orbit))
#     dict_orbit = dict(zip(square_orbit, filter_orbit))
#     max_orbit = max(dict_orbit.keys())
#     return dict_orbit.get(max_orbit)


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

# print(max(orbits, key = lambda x: x[0] * x[1] * (x[0] != x[1])))

# lst = list(input().split())
# print(lst)
# lst_1 = list(filter(lambda x: len(str(abs(int(x)))) == 2, lst))
# print(lst_1)

sum1 = 0
sum2 = 0
# temp = lambda x: x * x * (x % 9 == 0)
for i in range(10, 100):
    # sum1 = sum1 + temp(i)
    sum1 = sum1 + (lambda x: x * x * (x % 9 == 0)) (i)
    sum2 = sum2 + i * i * (i % 9 == 0)

print(sum1, "  ", sum2)