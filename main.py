# Задание 17.7.3
money=int(input('Введите сумму, которлую хотите инвестировать :'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
A = per_cent.get('ТКБ')
TKB = int(A*(money/100))
B = per_cent.get('СКБ')
CKB = int(B*(money/100))
C= per_cent.get('ВТБ')
BTB = int(C*(money/100))
D = per_cent.get('СБЕР')
CBER = int(D*(money/100))
deposit = [TKB,CKB,BTB,CBER]
print("Накопленные средства вклада за год в каждом из банков =",deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))