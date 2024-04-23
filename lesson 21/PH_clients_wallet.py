class Client:
    def __init__(self, name='', surname='', city='', balance= ''):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'''"{self.name}{self.surname}". {self.city}. Баланс:{self.balance} rubles.'''
    def get_gest(self):
        return f'{self.name} {self.surname}. {self.city}'

client_1 = Client('Иван ', 'Петров','Москва',
                  '50')
client_2 = Client('Ivan', 'Ivankkov', 'Novgorod', 100)
client_3 = Client('John', 'Smith', 'London', 200)
# создаем лист гостей
guest_list = [client_1,client_2,client_3]
for guest in guest_list:
    print(guest.get_gest())



