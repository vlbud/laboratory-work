# TODO решить с помощью list comprehension и распечатать его

d = [{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(16)]

for i in d:
    print(i)