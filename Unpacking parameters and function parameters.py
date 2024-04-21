print("Функция с параметрами по умолчанию:")
def print_params(a=1, b='строка 1', c=True):
    print(a, b, c)

print_params()
print_params(2)
print_params(b=25)
print_params(c=[1,2,3])
print_params(2, 25, [1,2,3])

print("Распаковка параметров:")
values_list = [3, 'строка 2', False]
values_dict = {'a': 4, 'b': 'строка 3', 'c': False}
print_params(*values_list)
print_params(**values_dict)

print("Распаковка + отдельные параметры:")
values_list_2 = [5, 'строка 4']
print_params(*values_list_2, 42)
