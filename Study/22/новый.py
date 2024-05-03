def bubble_sorting(array):  # Функция сортировки пузырьком
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def binary_search(array, element, left, right):
    if left > right:
        return None  # Элемент не найден
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif array[middle] > element:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

# Ввод и проверка последовательности чисел
while True:
    try:
        raw_input = input("Введите последовательность чисел в любом порядке, через пробел: ")
        if not raw_input:
            raise ValueError("Массив не может быть пустым.")
        array = list(map(int, raw_input.split()))
        # Проверка на уникальность элементов массива
        if len(array) != len(set(array)):
            raise ValueError("Все числа в массиве должны быть уникальными.")
        break
    except ValueError as e:
        print(f'Ошибка: {e}')

# Ввод и проверка произвольного числа
while True:
    try:
        element = int(input("Введите любое число: "))
        # Проверка на ввод отрицательных чисел, если требуется только положительные
        if element < 0:
            raise ValueError("Число не может быть отрицательным.")
        break
    except ValueError:
        print('Ошибка! Введите корректное целое число.')

# Сортировка массива и вывод отсортированного списка
sorted_array = bubble_sorting(array)
print('Сортированный список:', sorted_array)

# Поиск индекса элемента
index = binary_search(sorted_array, element, 0, len(sorted_array) - 1)
if index is None:
    print('Нет такого числа')
else:
    print('Индекс элемента:', index)