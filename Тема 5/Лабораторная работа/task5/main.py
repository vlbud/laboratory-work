from random import sample
def get_random_password(n=8) -> str:
    letters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # TODO написать функцию генерации случайных паролей
    password = sample(letters, n)
    s = "".join(password)
    return s

print(get_random_password())
