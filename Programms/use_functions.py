import datetime
import json


def separator(symbol, count):
    """разделитель
    """
    return (symbol * count)


def balance(traffic_money):
    """
    вычисляет в balance_only сумму всех элементов, получаем балланс  счета
    :param balance_only:
    :return:
    """
    # поступление денег, кортеж из даты и суммы
    put_money = [el[2] for el in traffic_money if el[0] == 'put']
    # снятие средств
    withdrawal_money = [el[2] for el in traffic_money if (el[0] == 'removal') or (el[0] == 'buy')]

    balance = sum(put_money) - sum(withdrawal_money)
    return balance


def put_cash(traffic_money, data):
    """
    функция пополнения счета, запись кортежей из даты и суммы
    :return: ничего не  возвращает
    """
    try:
        amount_plus = int(input('Введите сумму для пополнения: '))
    except ValueError:
        print('Вы ввели не число...')
        amount_plus = int(input('Введите сумму для пополнения: '))

    # добавляет в traffic_money кортеж из 3 элементов
    traffic_money.append(('put', data, amount_plus))


def removal_cash(traffic_money, data):
    """
    функция снятия со счета
    :return:  ничего не возвращает
    """
    try:
        amount_minus = int(input('Введите сумму для снятия: '))
    except ValueError:
        print('Вы ввели не число...')
        amount_minus = int(input('Введите сумму для снятия: '))
    # добавляет в traffic_money кортеж из 3 элементов
    traffic_money.append(('removal', data, amount_minus))


def buy(traffic_money, data):
    """
    функция покупки кортеж из 3 элементов
    :return: ничего не  возвращает
    """
    # Ввод данных
    product_name = input('Введите название продукта: ')
    amount_minus = int(input('Введите сумму покупки: '))

    traffic_money.append(('buy', data, amount_minus, product_name))


def history_buys(traffic_money):
    """
    функция истории покупок
    :param buys_only:
    :return:
    """
    buys_only = [el for el in traffic_money if el[0] == 'buy']
    print(buys_only)
    n = 0
    print('История покупок:')
    for buy in buys_only:
        n += 1
        # вывод истории покупок построчно
        print(f'  {n}). Дата покупки: {buy[1]}. Наименование: {buy[3]}. Цена: {buy[2]} УЕ')
    input('\nНажмите Enter чтобы продолжить ')


def history_only(traffic_money):  # функция истории транзакций
    print('История транзакций:')
    for el in traffic_money:
        if len(el) == 3:
            print(f'      {el[0]}: {el[1]}, {el[2]} УЕ')  # перебор кортежей и вывод их элементов через ":"
        if len(el) == 4:
            print(f'      {el[0]}: {el[1]}, {el[3]}, -  {el[2]} УЕ')  # ('buy', data, amount_minus, product_name)

    input('\nНажмите Enter чтобы продолжить ')



def my_money():
    while True:
        print(separator('*', 25))
        data = (datetime.date.today().strftime("%d.%m.%Y"))  # печать текущей даты
        time = (datetime.datetime.now().time())

        print("Сегодня", data)
        print("Время", time)

        print(separator('*', 25))
        print("Балланс счета: ", balance())  # начальное состояние счета

        print(separator('*', 25))
        print('Меню: ')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. снятие средств')
        print('4. история транзакций')
        print('5. история покупок')
        print('6. выход')
        print(separator('*', 25))

        choice = input('Выберите пункт меню: ')

        if choice == '1':  # добавляет в traffic_money и balance_only
            put_cash()

        elif choice == '2':  # добавляет в traffic_money транзакцию и buys_only
            buy()

        elif choice == '3':  # добавляет с "-" в traffic_money и balance_only
            removal_cash()

        elif choice == '4':
            history_only()  # вывод всей детализации операций

        elif choice == '5':
            history_buys()  # вывод детализации покупок

        elif choice == '6':
            with open('../traffic_money.json', 'w', encoding='utf-8') as file_write:  # содержит все транзакции
                json.dump(traffic_money, file_write)
            break
        else:
            print('Неверный пункт меню')
