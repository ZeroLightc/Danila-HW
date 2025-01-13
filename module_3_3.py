def print_params(a = 1, b = 'строка',c = True):
    print(a,b,c)

print_params()


print_params(0,'привет',False)

print_params(1,2,3)
print_params(b = "Два")
print_params(a = "Один")
print_params(c = 'Три')

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [5.19, 'строка', True]
values_dict = {'a': 'привет', 'b': True, 'c': 0}

print_params(*values_list)
print_params(**values_dict)


values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)