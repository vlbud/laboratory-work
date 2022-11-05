from random import randint
def get_unique_list_numbers():
    a = []
    while len(a)< 15:
        x = randint(-10, 10)
        if x not in a:
            a.append(x)
    return a


     # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
