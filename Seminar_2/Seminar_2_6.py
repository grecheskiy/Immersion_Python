# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снить, выйти
# Сумма пополнеиня и снятия кратны 50 y.e.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 y.e.
# После каждой третьей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять большк, чем на счете
# При привышении суммы в 5 млн., вычитать налог на богатсятво 10% перед каждой операцией, даже ошибочной
# Любое действие, выводить сумму денег

import decimal

#decimal.getcontext().prec = 2
CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXIT = 'в'
RICHNESS_SUM = decimal.Decimal(5_000_000)
RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100)
WITHDRAW_PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(100)
MULTIPLICITY = 50
MIN_REMOVAL = 30
MAX_REMOVAL = 600
COUNT_OPER = 3

account = decimal.Decimal(0)
count = 0

while True:
    command = input(f'Пополнить - "{CMD_DEPOSIT}", Снять -"{CMD_WITHDRAW}", Выйти - "{CMD_EXIT}"')
    if command == CMD_EXIT:
        print(f'Возьмите карту, на которой {account} y.e.')
        break
    elif account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        print(f'Удержан налог на богатство {RICHNESS_TAX}% в размере {percent} y.e.\n'
              f'Итого на карте {account} y.e. ')
    if command in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while amount % 50 != 0:
            amount = int(input(f'Введите сумму, кратную {MULTIPLICITY}:'))
    if command == CMD_DEPOSIT:
        account += amount
        count += 1
        print(f'Пополнение карты на {amount} y.e.\nИтого на карте {account} y.e. ')
    elif command == CMD_WITHDRAW:
        withdraw_tax = amount * WITHDRAW_PERCENT
        withdraw_tax = (MIN_REMOVAL if withdraw_tax < MIN_REMOVAL else
                        MAX_REMOVAL if withdraw_tax > MAX_REMOVAL else withdraw_tax)
        if account >= amount + withdraw_tax:
            count += 1
            account -= (amount + withdraw_tax)
            print(f'Снятие с карты {amount} y.e.\nКомиссия за снятие {withdraw_tax} y.e.\n'
                  f'На карте {account} y.e. ')
        else:
            print(f'Недостаточно денег для выполнения операции\n'
                  f'Затребованная сумма {amount} y.e., Комиссия составила {withdraw_tax} y.e.\n'
                  f'На карте {account} y.e. ')
    if count and count % COUNT_OPER == 0:
        bonus_percent = account * ADD_PERCENT
        account += bonus_percent
        print(f'На счет начислено {ADD_PERCENT}%, составляющие {bonus_percent} y.e.\n'
              f'Итого на карте {account} y.e. ')

