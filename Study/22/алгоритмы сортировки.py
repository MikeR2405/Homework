# # import random  # модуль, с помощью которого перемешиваем массив
# #
# # # пусть имеем массив всего лишь из 9 элементов
# # array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# #
# # is_sort = False  # станет True, если отсортирован
# # count = 0  # счетчик количества перестановок
# #
# # while not is_sort:  # пока не отсортирован
# #     count += 1  # прибавляем 1 к счётчику
# #
# #     random.shuffle(array)  # перемешиваем массив
# #
# #     # проверяем, отсортирован ли
# #     is_sort = True
# #     for i in range(len(array) - 1):
# #         if array[i] > array[i + 1]:
# #             is_sort = False
# #             break
# #
# # print(array)
# # # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(count)
# # # 290698
# #
# # import math
# # num = math.factorial(100)
# #
# # num_digits = len(str(num))
# # print(num_digits)
#
# # сортировка выбором
#
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# count = 0
# count1 = 0
#
# for i in range(len(array)):  # проходим по всему массиву
#     idx_min = i  # сохраняем индекс предположительно минимального элемента
#     for j in range(i, len(array)):
#         count +=1
#         if array[j] < array[idx_min]:
#             idx_min = j
#     if i != idx_min:  # если индекс не совпадает с минимальным, меняем
#         array[i], array[idx_min] = array[idx_min], array[i]
# # сортировка по убыванию
# for i in range(len(array)):
#     ind_max = i
#     for j in range(i, len(array)):
#         count1 +=1
#         if array[j] > array[ind_max]:
#             ind_max = j
#     if i != ind_max:
#         array[i], array[ind_max] = array[ind_max], array[i]
#
# # print(array)
# print('сравнения: ', count, count1)
# Сортировка пузырьком
# array = [2,3,1,4,6,5,9,8,7]
# count = 0

# for i in range(len(array)):
#     for j in range(len(array)-i-1):
#         if array[j] > array[j+1]:
#             array[j], array[j+1]= array[j+1], array[j]
#
# print(array)
#
# for i in range(1, len(array)):
#     x = array[i]
#     idx = i
#     while idx > 0 and array[idx-1] > x:
#         count +=1
#         array[idx] = array[idx-1]
#         idx -= 1
#     array[idx] = x
#
# print(array)
# print(count)

# сортировка слиянием
# def merge_sort(array):
#     if len(array) > 1:
#         # Находим середину массива
#         mid = len(array) // 2
#         # Делим массив на две половины
#         left_half = array[:mid]
#         right_half = array[mid:]
#
#         # Рекурсивно сортируем каждую половину
#         merge_sort(left_half)
#         merge_sort(right_half)
#
#         # Итераторы для обхода двух половин
#         i = 0  # для левой половины
#         j = 0  # для правой половины
#         k = 0  # для основного массива
#
#         # Слияние двух половин
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 array[k] = left_half[i]
#                 i += 1
#             else:
#                 array[k] = right_half[j]
#                 j += 1
#             k += 1
#
#         # Копирование оставшихся элементов левой половины, если они есть
#         while i < len(left_half):
#             array[k] = left_half[i]
#             i += 1
#             k += 1
#
#         # Копирование оставшихся элементов правой половины, если они есть
#         while j < len(right_half):
#             array[k] = right_half[j]
#             j += 1
#             k += 1
#
#     return array
#
# # Пример использования функции
# array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# sorted_array = merge_sort(array)
# print(sorted_array)

# БЫСТРАЯ СОРТИРОВКА
#
# def qsort(array, left, right):
#     middle = (left + right) // 2
#
#     p = array[middle]
#     i, j = left, right
#     while i <= j:
#         while array[i] < p:
#             i += 1
#         while array[j] > p:
#             j -= 1
#         if i <= j:
#             array[i], array[j] = array[j], array[i]
#             i += 1
#             j -= 1
#
#     if j > left:
#         qsort(array, left, j)
#     if right > i:
#         qsort(array, i, right)
#
# Добавляем рандомный выбор
import random

def qsort_random(array, left, right):
    if left < right:
        p = random.choice(array[left:right+1])
        i, j = left, right
        while i <= j:
            while array[i] < p:
                i += 1
            while array[j] > p:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        if j > left:
            qsort_random(array, left, j)
        if right > i:
            qsort_random(array, i, right)

array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
qsort_random(array, 0, len(array) - 1)
print(array)
