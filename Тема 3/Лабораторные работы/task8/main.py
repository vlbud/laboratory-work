money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
def month(money_capital , salary, spend, increase):
    n = 0
    while money_capital > 0:
        money_capital = money_capital - (spend * (1 + increase)**n - salary)
        n += 1
    return n - 1

print(month(money_capital, salary, spend, increase))
