#функция P(n) лрассчитываем алгоритм снятия тарелок в стеке:)
# def p(n):
#     if n ==0:
#         return
#     else:
#         p(n-1)
#         print(n)
# p(5)
# функция которая проверяет строку на корректность
pars = {')': '(', ']': "["}

def par_checker(string):
    stack = []   # инициализируем стэк

    for s in string: # для эелемнта в строке
        if s in "([":
            stack.append(s) # то добавляем ее в стэк
        elif s in ")]": # то проверяем пустой ли наш стэк и является ли верхний элелмент "("
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop() # тогда удаляем из стэка
            else:
                return False
# если стэк пустой  -> незакрытых скобок не осталось
# возвращаем TRUE, если нет то False
    return len(stack) == 0
print(par_checker("(5+6)*(7+8)/(4+3"))