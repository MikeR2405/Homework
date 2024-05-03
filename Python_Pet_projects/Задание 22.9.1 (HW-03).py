# Функция сортировки пузырьком
def bubble_sorting(array):
    for i in range(len(array) - 1):  # Проходим по всему массиву
        for j in range(len(array) - i - 1):  # Сравниваем элементы внутри неотсортированной части массива
            if array[j] > array[j + 1]:  # Если текущий элемент больше следующего
                array[j], array[j + 1] = array[j + 1], array[j]  # Меняем их местами
    return array  # Возвращаем отсортированный массив

# Функция бинарного поиска
def binary_search(array, element, left, right):
    if left > right:  # Если левая граница превысила правую
        return None  # Элемент не найден
    middle = (right + left) // 2  # Находим середину диапазона
    # Проверяем, находится ли искомый элемент в середине
    if array[middle] < element and (middle == right or array[middle + 1] >= element):
        return middle  # Возвращаем индекс элемента, если он меньше искомого
    elif array[middle] < element:  # Если элемент больше элемента в середине
        return binary_search(array, element, middle + 1, right)  # Ищем в правой половине
    else:  
        return binary_search(array, element, left, middle - 1)  # Ищем в левой половине

# Функция для ввода массива чисел
def input_array():
    while True:  
        try:
            raw_input = input("Введите последовательность чисел в любом порядке, через пробел: ")
            if not raw_input.strip():  # Если строка пустая
                raise ValueError("Массив не может быть пустым.")
            if any(char.isalpha() for char in raw_input.replace(" ", "")):  # Если есть буквы
                raise ValueError("Ошибка, ввели некорректное число")
            array = [int(item) for item in raw_input.split() if item.strip().isdigit()]  # Преобразуем строку в массив чисел
            if len(array) != len(set(array)):  # Если есть дубликаты
                raise ValueError("Все числа в массиве должны быть уникальными.")
            return array  # Возвращаем массив
        except ValueError as e:  # Обработка исключений
            print(f'Ошибка: {e}')

# Функция для ввода искомого числа
def input_element():
    while True:  
        try:
            element_input = input("Введите любое число: ")
            if not element_input.strip().isdigit():  # Если введено не число
                raise ValueError("Ошибка, ввели некорректное число")
            element = int(element_input)  # Преобразуем введенное значение в число
            if element < 0:  # Если число отрицательное
                raise ValueError("Число не может быть отрицательным.")
            return element  # Возвращаем число
        except ValueError as e:  # Обработка исключений
            print(f'Ошибка: {e}')

# Ввод массива и искомого числа
array = input_array()  
element = input_element()  

sorted_array = bubble_sorting(array)  # Сортировка массива
print('Сортированный список:', sorted_array)  # Вывод отсортированного массива

index = binary_search(sorted_array, element, 0, len(sorted_array) - 1)  # Поиск индекса искомого числа
if index is None:  # Если индекс не найден
    print('Нет такого числа')
else:  # Если индекс найден
    print('Индекс элемента, который меньше введенного числа:', index)
