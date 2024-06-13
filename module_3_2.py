#  1.Функция с параметрами по умолчанию

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(77)
print_params(33, 55)
print_params(11, 22, 33)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(b=25, c=[1, 2, 3])
print()


#  2.Распаковка параметров


values_list = ['student', [3, 5, 7], True]
values_dict = {'a': 333, 'b': 'children', 'c': [22, 44, 66]}
print_params(*values_list)
print_params(**values_dict)
print()


#  3.Распаковка + отдельные параметры


values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)



