def calculate_structure_sum(data_structure):
    total_sum = 0
    # Цикл обходит каждый элемент в переданной структуре данных
    for item in data_structure:
        # Если элемент типа int, то прибавляем его значение к общей сумме
        if isinstance(item, int):
            total_sum += item
        # Если элемент типа str, прибавляем длину строки
        elif isinstance(item, str):
            total_sum += len(item)
        # Если элемент типа list или tuple, рекурсивно вызываем функцию для обработки вложенной структуры
        elif isinstance(item, (list, tuple)):
            total_sum += calculate_structure_sum(item)
        # Если элемент типа dict, суммируем длину ключа и рекурсивно вызываем функцию для значения в словаре
        elif isinstance(item, dict):
            total_sum += sum([len(str(key)) + calculate_structure_sum([value]) for key, value in item.items()])
    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [(2, 'Urban', ('Urban2', 35))])
]

# Результат сохраняем в переменной result и выводим на экран
result = calculate_structure_sum(data_structure)
print(result)

