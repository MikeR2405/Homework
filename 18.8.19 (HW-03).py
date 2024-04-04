N = (int(input("введите нужное количество билетов: \n")))
cost1 = 0  #  стоимость для лиц младше 18 лет
cost2 = 990  # стоимость для лиц 18 - 25
cost3 = 1390  # стоимость для лиц от 25
price = 0  # стоимость билетов в заказе

for age in range(N):
    age = (int(input("Введите возраст посетителя : ")))
    if age < 18:
        price += cost1
    elif age >= 18 and age <= 25:
        price += cost2
    elif age >= 25:
        price += cost3
if N > 3:
     price = price - (price * 0.1)
     # discount = price * 0.1
     # print("Скидка составляет:", discount, "рублей")
     print("К оплате, с учетом скидки: ", price, "рублей")
else:
    print("К оплате: ", price, "рублей")



