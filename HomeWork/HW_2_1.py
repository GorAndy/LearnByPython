

def add_to(recipe):
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
    dish_recipe = {}
    name_dish = recipe[0]
    dish_recipe[name_dish] = []
    for ingridient in recipe[2::]:
        ingridient = ingridient.split('|')
        dish_recipe[name_dish].append({'ingridient_name': ingridient[0].strip(),\
                                       'quantity': int(ingridient[1]), 'measure': ingridient[2].strip()})
    return dish_recipe
=======
>>>>>>> Stashed changes
    book = {}
    name_dish = recipe[0]
    book[name_dish] = []
    for i in range(int(recipe[1])):
        ingrid = recipe[i+2].split('|')
        book[name_dish].append({'ingridient_name': ingrid[0], 'quantity': int(ingrid[1]), 'measure': ingrid[2]})
    return book
<<<<<<< Updated upstream
=======
>>>>>>> origin/master
>>>>>>> Stashed changes


def get_cook_book():
    recipe = []
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
    cook_book = {}
    with open('2_1_cook_book.txt', 'r') as cook:
        for line in cook:
            line = line.strip()
            if not line:
=======
>>>>>>> Stashed changes
    with open('2_1_cook_book.txt', 'r') as cook:
        for line in cook:
            line = line.strip()
            if line == '':
<<<<<<< Updated upstream
=======
>>>>>>> origin/master
>>>>>>> Stashed changes
                cook_book.update(add_to(recipe))
                recipe = []
            else:
                recipe.append(line)
        cook_book.update(add_to(recipe))
    return cook_book

<<<<<<< Updated upstream
def get_shop_list_by_dishes(dishes, person_count):
=======
<<<<<<< HEAD

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book()
=======
def get_shop_list_by_dishes(dishes, person_count):
>>>>>>> origin/master
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        # print(shop_list)
=======
<<<<<<< HEAD
=======
        # print(shop_list)
>>>>>>> origin/master
>>>>>>> Stashed changes
        print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))


def create_shop_list():
<<<<<<< Updated upstream
    cook_book = get_cook_book()
=======
<<<<<<< HEAD
=======
    cook_book = get_cook_book()
>>>>>>> origin/master
>>>>>>> Stashed changes
    person_count = int(input('Введите количество едоков: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую):').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

<<<<<<< Updated upstream
=======
<<<<<<< HEAD
=======
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
=======
>>>>>>> origin/master
>>>>>>> Stashed changes
create_shop_list()