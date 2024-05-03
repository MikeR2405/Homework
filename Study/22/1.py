# # def bubble_sorting(array):  # Функция сортировки пузырьком
# #     for i in range(len(array) - 1):
# #         for j in range(len(array) - i - 1):
# #             if array[j] > array[j + 1]:
# #                 array[j], array[j + 1] = array[j + 1], array[j]
# #     return array
# #
# # def binary_search(array, element, left, right):
# #     if left > right:  # Если левая граница превысила правую,
# #         return None  # Элемент не найден
# #     middle = (right + left) // 2
# #     if array[middle] < element and (middle == right or array[middle + 1] >= element):
# #         return middle
# #     elif array[middle] < element:
# #         return binary_search(array, element, middle + 1, right)
# #     else:
# #         return binary_search(array, element, left, middle - 1)
# #
# # while True:
# #     try:
# #         raw_input = input("Введите последовательность чисел в любом порядке, через пробел: ")
# #         if not raw_input.strip():
# #             raise ValueError("Массив не может быть пустым.")
# #         array = [int(item) for item in raw_input.split() if item.strip().isdigit()]
# #         if len(array) != len(set(array)):
# #             raise ValueError("Все числа в массиве должны быть уникальными.")
# #         element_input = input("Введите любое число: ")
# #         if not element_input.strip().isdigit():
# #             raise ValueError("Введено не число.")
# #         element = int(element_input)
# #         if element < 0:
# #             raise ValueError("Число не может быть отрицательным.")
# #         break
# #     except ValueError as e:
# #         print(f'Ошибка: {e}')
# #
# # sorted_array = bubble_sorting(array)
# # print('Сортированный список:', sorted_array)
# #
# # index = binary_search(sorted_array, element, 0, len(sorted_array) - 1)
# # if index is None:
# #     print('Нет такого числа')
# # else:
# #     print('Индекс элемента, который меньше введенного числа:', index)
#
#
# def bubble_sorting(array):  # Функция сортировки пузырьком
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#     return array
#
# def binary_search(array, element, left, right):
#     if left > right:  # Если левая граница превысила правую,
#         return None  # Элемент не найден
#     middle = (right + left) // 2
#     if array[middle] < element and (middle == right or array[middle + 1] >= element):
#         return middle
#     elif array[middle] < element:
#         return binary_search(array, element, middle + 1, right)
#     else:
#         return binary_search(array, element, left, middle - 1)
#
# def input_array():
#     while True:
#         try:
#             raw_input = input("Введите последовательность чисел в любом порядке, через пробел: ")
#             if not raw_input.strip():
#                 raise ValueError("Массив не может быть пустым.")
#             # Проверка на буквы в вводе
#             if any(char.isalpha() for char in raw_input.replace(" ", "")):
#                 raise ValueError("Ввод должен содержать только цифры.")
#             array = [int(item) for item in raw_input.split() if item.strip().isdigit()]
#             if len(array) != len(set(array)):
#                 raise ValueError("Все числа в массиве должны быть уникальными.")
#             return array
#         except ValueError as e:
#             print(f'Ошибка: {e}')
#
# def input_element():
#     while True:
#         try:
#             element_input = input("Введите любое число: ")
#             if not element_input.strip().isdigit():
#                 raise ValueError("Введено не число.")
#             element = int(element_input)
#             if element < 0:
#                 raise ValueError("Число не может быть отрицательным.")
#             return element
#         except ValueError as e:
#             print(f'Ошибка: {e}')
#
# array = input_array()
# element = input_element()
#
# sorted_array = bubble_sorting(array)
# print('Сортированный список:', sorted_array)
#
# index = binary_search(sorted_array, element, 0, len(sorted_array) - 1)
# if index is None:
#     print('Нет такого числа')
# else:
#     print('Индекс элемента, который меньше введенного числа:', index)

def bubble_sorting(array):  # Функция сортировки пузырьком
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def binary_search(array, element, left, right):
    if left > right:  # Если левая граница превысила правую,
        return None  # Элемент не найден
    middle = (right + left) // 2
    if array[middle] < element and (middle == right or array[middle + 1] >= element):
        return middle
    elif array[middle] < element:
        return binary_search(array, element, middle + 1, right)
    else:
        return binary_search(array, element, left, middle - 1)

def input_array():
    while True:
        try:
            raw_input = input("Введите последовательность чисел в любом порядке, через пробел: ")
            if not raw_input.strip():
                raise ValueError("Массив не может быть пустым.")
            if any(char.isalpha() for char in raw_input.replace(" ", "")):  # Проверка на буквы
                raise ValueError("Ошибка, ввели некорректное число")
            array = [int(item) for item in raw_input.split() if item.strip().isdigit()]
            if len(array) != len(set(array)):
                raise ValueError("Все числа в массиве должны быть уникальными.")
            return array
        except ValueError as e:
            print(f'Ошибка: {e}')

def input_element():
    while True:
        try:
            element_input = input("Введите любое число: ")
            if not element_input.strip().isdigit():
                raise ValueError("Ошибка, ввели некорректное число")
            element = int(element_input)
            if element < 0:
                raise ValueError("Число не может быть отрицательным.")
            return element
        except ValueError as e:
            print(f'Ошибка: {e}')

array = input_array()
element = input_element()

sorted_array = bubble_sorting(array)
print('Сортированный список:', sorted_array)

index = binary_search(sorted_array, element, 0, len(sorted_array) - 1)
if index is None:
    print('Нет такого числа')
else:
    print('Индекс элемента, который меньше введенного числа:', index)