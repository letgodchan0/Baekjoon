lst_0 = [0] * 41
lst_1 = [0] * 41
lst_0[0], lst_0[1] = 1, 0
lst_1[0], lst_1[1] = 0, 1
for i in range(2, 41):
    lst_0[i] += lst_0[i-1] + lst_0[i-2]
    lst_1[i] += lst_1[i-1] + lst_1[i-2]
for _ in range(int(input())):
    n = int(input())
    print(lst_0[n], lst_1[n])