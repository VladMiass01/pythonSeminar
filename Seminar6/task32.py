lst_in = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
lst_out = []
n_min = int(input("минимум: "))
n_max = int(input("максимум: "))
for i in range(len(lst_in)):
    if lst_in[i] >= n_min and lst_in[i] <= n_max:
        lst_out.append(i)
print(lst_out)