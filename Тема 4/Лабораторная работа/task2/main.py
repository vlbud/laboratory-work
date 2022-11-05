def get_count_char(str_):
    letters = []
    symbols = ' !@#$%^&*()[]{}.,-='
    for i in str_: # TODO посчитать количество каждой буквы в строке в аргументе str_
        if i.isalpha() and i not in letters and i not in symbols:
            letters.append(i.lower())
    d = dict.fromkeys(letters, 0)
    for i in str_:
        d[i.lower()] = d.get(i.lower(), 0) + 1
    return d
def get_procent(str_):
    d2 = {}
    letters = []
    for i in str_:
        if i.isalpha() and i not in letters:
            letters.append(i.lower())
    d = dict.fromkeys(letters, 0)
    for i in str_:
        d[i.lower()] = d.get(i.lower(), 0) + 1
    summa = 0
    for i in d.values():
        summa += i
    for k,v in d.items():
        d2[k] = round(v / summa * 100, 2)
    return d2
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
#  print(get_procent(main_str))