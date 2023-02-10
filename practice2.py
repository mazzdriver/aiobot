# Анонимная функция как фильтр
# Напишите функцию anonimous_filter, используя синтаксис
# анонимных функций, которая принимает строковый аргумент и
# возвращает значение True, если количество русских букв я
# не меньше 23 (регистр буквы неважен) и False в противном случае.

# Примечание. Вызывать анонимную функцию не нужно.
# Только дописать ее код.


# anonimous_filter = lambda x: x # продолжите анонимную функцию


# def anonimous_filter(parameter: str) -> bool:

    # return parameter.count('я') >= 23

    # yalist = list(filter( 'я', [let for let in parameter]))
    # return (len(yalist)) >= 23

    # yalist = []
    # for letter in parameter:
    #     if letter == 'я':
    #         yalist.append(letter)
    # return len(yalist) >= 23

    # counter = 0
    # for letter in parameter:
    #     if letter == 'я':
    #         counter += 1
    # return counter >= 23

anonimous_filter = lambda x: x.lower().count('я') >= 23


def anonimous_filter_test(parameter, expected):
    if anonimous_filter(parameter) == expected:
        print('Test passed')
    else:
        print('Test failed')


anonimous_filter_test('Я - последняя буква в алфавите!', False)
anonimous_filter_test('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!', True)
anonimous_filter_test('я' * 13, False)
anonimous_filter_test('я' * 33, True)
anonimous_filter_test('Я' * 33, True)

# def anonimous_filter(parameter: str) -> bool:
#     counter = 0
#     for letter in parameter:
#         if letter == 'я':
#             counter += 1
#     return counter >= 23
