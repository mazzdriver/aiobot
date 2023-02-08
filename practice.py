# Реализуйте функцию custom_filter(), которая на вход принимает
# список some_list, с любыми типами данных, находит в этом списке
# целые числа, отбирает из них те, что делятся нацело на 7,
# суммирует их, а затем проверяет превышает эта сумма 83 или нет.
# Если НЕ превышает - функция должна вернуть True,
# если превышает - False.

# Примечание. В тестирующую систему сдайте программу, содержащую
# только необходимую функцию custom_filter(), но не код, вызывающий ее.

list1, want1 = ['a', 7, 98, 11], False
list2, want2 = ['b', 7, 49], True
list3, want3 = [2, 4, 'b', 'c'], False
list4, want4 = ['vss', [0, 1, 2], (22, 17)], False
list5, want5 = [7, 14, 28, 32, 32, 56], False
list6, want6 = [7, 14, 28, 32, 32, '56'], True


def custom_filter(some_list: list) -> bool:
    summ = 0
    for elem in some_list:
        if isinstance(elem, int) or isinstance(elem, float):
            if elem % 7 == 0:
                summ += elem
    return 0 < summ < 83


def custom_filter_test(order, want):
    if custom_filter(order) == want:
        print('Test passed')
    else:
        print('Test failed')


custom_filter_test(list1, want1)
custom_filter_test(list2, want2)
custom_filter_test(list3, want3)
custom_filter_test(list4, want4)
custom_filter_test(list5, want5)
custom_filter_test(list6, want6)
