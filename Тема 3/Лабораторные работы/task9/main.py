salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
def need_money(spend, months, increase):
    x = sum([spend * (1 + increase)**i for i in range(months)]) #x-количество денег которые потратит за 10 мес.
    return x - 10*salary
print(round(need_money(spend, months, increase)))
