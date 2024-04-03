#1

from random import randint

def generate_random_num():
    number_list = []
    for i in range(21):
        number_list.append(randint(1, 21))

    return number_list

def filter_number_list(number_list):
    
    if isinstance(number_list, str) or \
        isinstance(number_list, int) or \
            isinstance(number_list, bool):
        return 'Работаем только со списком чисел'

    result = []
    for number in number_list:
        if number % 2 == 0:
            result.append(number)

    return result

#2

def get_intersection_lists(list_one, list_two):

    if isinstance(list_one, str) or isinstance(list_two, str):
        return 'Работаем только со списками'

    return list(set(list_one).intersection(set(list_two)))


#3

def check_palindrom(text):
    if str(text) == str(text)[::-1]:
        return True
    else:
        return False
    

