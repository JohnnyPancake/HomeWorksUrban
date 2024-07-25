def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [5, 'Столбец', False]
values_dict = {'a': 7, 'b': 'высота', 'c': False}

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

# print_params(3, c=False)  # работает
# print_params(10)  # работает
# print_params()  # работает

# print_params(b=25)  # работает, но ругается что str заменили на int
# print_params(c=[1, 2, 3])  # работает, но ругается на замену типа параметра, как в предыдущей строке

# print_params(*values_list)  # работает
# print_params(**values_dict)  # работает
