import json
import yaml


def get_cook_book(file_name):
    with open(file_name, encoding='utf8') as cook:
        if '.json' in file_name:
            cook_book = json.load(cook)
        elif '.yml' in file_name:
            cook_book = yaml.load(cook)
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_books = get_cook_book(fname)
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_books[dish]:
            new_shop_list = dict(ingridient)
            new_shop_list['quantity'] *= person_count
            if new_shop_list['ingridient_name'] not in shop_list:
                shop_list[new_shop_list['ingridient_name']] = new_shop_list
            else:
                shop_list[new_shop_list['ingridient_name']]['quantity'] += new_shop_list['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))


def request_for_shop_list():
    person_count = int(input('Введите количество едоков: '))
    dishes = input('Введите блюда в расчете на одного человека (через пробел):').lower().split(' ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


# Для рецептов в yaml изменить раcширение в переменной на .yml
fname = 'cook_book.json'
request_for_shop_list()
