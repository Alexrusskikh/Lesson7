#импорт модулей
import datetime
import json
import os

#печать текущей даты
data = (datetime.date.today().strftime("%d/%m/%Y"))
print("Сегодня", data)

#переменные для текущих данных
traffic_money = []  # общий список
balance_old = []  # только баланс
buys_all = []  # только покупки

#открытие файлов на чтение
if os.path.exists('traffic_money.json'):#проверка наличия файла
    with open('traffic_money.json',
              'r') as file_read:  # файл всех танзакций открывается на чтение и передает данные в traffic_money
        traffic_money = json.load(file_read)
        # print(*traffic_money, sep="\n")

if os.path.exists('balance.txt'):  # проверка наличия файла
    with open('balance.txt', 'r') as file_read:  # файл баланса, открывается на чтение и передает данные в balance_old
        balance_old = [int(file_read.read())]


if os.path.exists('buys.txt'):#проверка наличия файла
    with open('buys.txt', 'r', encoding='utf-8') as file_read:#файл buys, открывается на чтение и передает данные в buys_all
        for buy in file_read:
            buys_all.append(buy.replace('\n', ' '))
            # print(*buys_all, sep="\n")

#все функции
def put_cash(traffic_money, balance_old):# функция пополнения  счета через traffic_money и balance_old
    amount = int(input('Введите сумму для пополнения: '))
    traffic_money.append(
        ('Поступление средств ' + data, int(amount)))#добавляет в traffic_money кортеж из 2 элементов
    balance_old.append(int(amount))#добавляет в balance_old элемент число


def removal_cash(balance_old):#функция снятия со счета через traffic_money и balance_old
    amount = int(input('Введите сумму для снятия: '))
    traffic_money.append(
        ('Снятие средств ' + data, -int(amount)))  # добавляет в traffic_money кортеж из 2 элементов
    balance_old.append(-int(amount))


def balance(balance_old):  # вычисляет в balance_old баланс
    balance = sum(balance_old)
    return balance

def buy(traffic_money, balance_old, buys_all):# функция покупки и ее суммы
    product_name = input('Введите название продукта: ')
    amount = input('Введите сумму покупки: ')
    traffic_money.append(
        ('Покупка ' + data + ' ' + product_name, -int(amount)))  # добавляет в traffic_money покупку и ее суммы
    buys_all.append(
        ('Покупка ' + data + ' , ' + product_name, -int(amount)))  # добавляет в buys_all покупку и ее суммы
    balance_old.append(
        (-int(amount)))  # добавляет в balance_old покупки и ее суммы

def history_buys(buys_all):  # функция истории покупок
    n = 0
    print('История покупок:')
    for buy in buys_all:
        n+= 1
        print(f'  {n}).  {buy}УЕ')  # вывод истории построчно
    input('\nНажмите Enter чтобы продолжить ')

def history_all(traffic_money):  # функция истории транзакций
    print('История транзакций:')
    for name, amount in traffic_money:
        print(f'      {name}: {amount} УЕ')  # перебор кортежей и вывод их элементов через ":"
    input('\nНажмите Enter чтобы продолжить ')

def simple_separator():#разделитель
    return ('*' * 20)

while True:
    print(simple_separator())
    print("Балланс счета: ", balance(balance_old))
    print(simple_separator())
    print('1. пополнение счета')
    print('2. покупка')
    print('3. снятие средств')
    print('4. история транзакций')
    print('5. история покупок')
    print('6. выход')
    print(simple_separator())

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        put_cash(traffic_money, balance_old)#добавляет в traffic_money и balance_old
    elif choice == '2':
        buy(traffic_money, balance_old, buys_all) #добавляет в traffic_money и buys_all
    elif choice == '3':
        removal_cash(balance_old)#добавляет с "-" в traffic_money и balance_old
    elif choice == '4':
        history_all(traffic_money)#вывод всей детализации операций
    elif choice == '5':
        history_buys(buys_all)#вывод детализации покупок
    elif choice == '6':
        with open('traffic_money.json', 'w') as f:#содержит все транзакции
            json.dump(traffic_money, f)
        with open('balance.txt', 'w', encoding ='utf-8') as file_write:#содержит баланс
            file_write.write(str(balance(balance_old)))
        with open('buys.txt', 'w', encoding ='utf-8') as file_write:#содержит все покупки
            for buy in buys_all:
                file_write.write(f'{buy}\n')
        break
    else:
        print('Неверный пункт меню')