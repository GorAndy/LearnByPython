

def add_to(recipe):
    book = {}
    name_dish = recipe[0]
    book[name_dish] = []
    for i in range(int(recipe[1])):
        ingrid = recipe[i+2].split('|')
        book[name_dish].append({'ingridient_name': ingrid[0], 'quantity': int(ingrid[1]), 'measure': ingrid[2]})
    return book


def get_cook_book():
    recipe = []
    with open('2_1_cook_book.txt', 'r') as cook:
        for line in cook:
            line = line.strip()
            if line == '':
                cook_book.update(add_to(recipe))
                recipe = []
            else:
                recipe.append(line)
        cook_book.update(add_to(recipe))
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list = dict(ingridient)
            new_shop_list['quantity'] *= person_count
            if new_shop_list['ingridient_name'] not in shop_list:
                shop_list[new_shop_list['ingridient_name']] = new_shop_list
            else:
                shop_list[new_shop_list['ingridient_name']]['quantity'] += new_shop_list['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        # print(shop_list)
        print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))


def create_shop_list():
    cook_book = get_cook_book()
    person_count = int(input('Введите количество едоков: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую):').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


# cook_book = {
#     'яичница': [
#         {'ingridient_name': 'eggs', 'quantity': 2, 'measure': 'шт'},
#         {'ingridient_name': 'tomat', 'quantity': 100, 'measure': 'гр'}
#     ],
#     "стейк": [
#         {'ingridient_name': 'мясо', 'quantity': 300, 'measure': 'гр'},
#         {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр'},
#         {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'гр'}
#     ],
#     "салат": [
#         {'ingridient_name': 'tomat', 'quantity': 100, 'measure': 'гр'},
#         {'ingridient_name': 'огрурцы', 'quantity': 100, 'measure': 'гр'},
#         {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'гр'},
#         {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт'}
#     ]
# }
cook_book = {}
create_shop_list()