# N_max = int(input("Определите размер очереди:"))
#
# queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
# order = 0  # будем хранить сквозной номер задачи
# head = 0  # указатель на начало очереди
# tail = 0  # указатель на элемент следующий за концом очереди
#
# def is_empty():
#     # Если начало и конец очереди совпадают, и начало указывает на ноль, то очередь пуста
#     return head == tail and queue[head] == 0
#
# def size():
#     # Получаем размер очереди
#     if is_empty():
#         return 0
#     elif head == tail:
#         return N_max
#     elif head > tail:
#         return N_max - head + tail
#     else:
#         return tail - head
#
# def add():
#     # Добавляем задачу в очередь
#     global tail, order
#     order += 1
#     queue[tail] = order
#     print("Задача №%d добавлена" % (queue[tail]))
#     tail = (tail + 1) % N_max
#
# def show():
#     # Выводим задачу в приоритете
#     print("Задача №%d в приоритете" % (queue[head]))
#
# def do():
#     # Выполняем задачу
#     global head
#     print("Задача №%d выполнена" % (queue[head]))
#     queue[head] = 0
#     head = (head + 1) % N_max
#
# # Основной цикл программы
# while True:
#     cmd = input("Введите команду:")
#     if cmd == "empty":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             print("В очереди есть задачи")
#     elif cmd == "size":
#         print("Количество задач в очереди:", size())
#     elif cmd == "add":
#         if size() != N_max:
#             add()
#         else:
#             print("Очередь переполнена")
#     elif cmd == "show":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             show()
#     elif cmd == "do":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             do()
#     elif cmd == "exit":
#         while not is_empty():
#             do()
#         print("Очередь пустая. Завершение работы")
#         break
#     else:
#         print("Введена неверная команда")

# Графы
G = {"Адмиралтейская" :
         {"Садовая" : 4},
     "Садовая" :
         {"Сенная площадь" : 3,
          "Спасская" : 3,
          "Адмиралтейская" : 4,
          "Звенигородская" : 5},
     "Сенная площадь" :
         {"Садовая" : 3,
          "Спасская" : 3},
     "Спасская" :
         {"Садовая" : 3,
          "Сенная площадь" : 3,
          "Достоевская" : 4},
     "Звенигородская" :
         {"Пушкинская" : 3,
          "Садовая" : 5},
     "Пушкинская" :
         {"Звенигородская" : 3,
          "Владимирская" : 4},
     "Владимирская" :
         {"Достоевская" : 3,
          "Пушкинская" : 4},
     "Достоевская" :
         {"Владимирская" : 3,
          "Спасская" : 4}}

D = {k : 100 for k in G.keys()} # расстояния
start_k = 'Адмиралтейская' # стартовая вершина
D[start_k] = 0 # расстояние от нее до самой себя равно нулю
U = {k : False for k in G.keys()} # флаги просмотра вершин
P = {k : None for k in G.keys()} # предки
some_station = "Владимирская"

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])

    for v in G[min_k].keys(): # проходимся по всем смежным вершинам
         if D[v] > D[min_k] + G[min_k][v]: # если расстояние от текущей вершины меньше
            D[v] = D[min_k] + G[min_k][v] # то фиксируем его
            P[v] = min_k # и записываем как предок
    U[min_k] = True # просмотренную вершину помечаем
    pointer = some_station  # куда должны прийти
    while pointer is not None:  # перемещаемся, пока не придём в стартовую точку
        print(pointer)
        pointer = P[pointer]
