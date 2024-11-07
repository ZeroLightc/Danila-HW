my_list = []

n = int(input("Введите количество символов: "))

for i in range(0, n):
    a = int(input())
    my_list.append(a)

print(my_list)

a = 0

while my_list[a] > 0:
    print(my_list[a])
    if a < n - 1:
        a = a + 1
    else:
        break

